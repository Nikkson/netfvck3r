import scapy.all as scapy
import socket
from socket import *


class Scanner:
    def __init__(self):
        self.clients_list = []

    def client_scan(self, ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_packets = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        for element in answered_packets:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            self.clients_list.append(client_dict)
        return self.clients_list

    def conn_scan(self, target_host, target_port):
        try:
            conn_socket = socket(AF_INET, SOCK_STREAM)
            conn_socket.connect((target_host, target_port))
            conn_socket.send(bytes('Meowwwww\r\n', encoding='utf-8'))
            results = conn_socket.recv(100)
            conn_socket.close()
            return target_port, results.decode()
        except Exception:
            return target_port, "-"

    def port_scan(self, target_host, target_ports):
        try:
            target_IP = gethostbyname(target_host)
        except:
            return
        ports_services = []
        setdefaulttimeout(1)
        for port in target_ports:
            port_number, service = self.conn_scan(target_host, int(port))
            port_dict = {"port_number": port_number, "service": service}
            ports_services.append(port_dict)
        return ports_services

    def scan(self, ip, target_ports):
        self.client_scan(ip)
        clients_ports = []
        for client in self.clients_list:
            ports_services = self.port_scan(client["ip"], target_ports)
            client_dict = {"client": client, "ports_services": ports_services}
            clients_ports.append(client_dict)
        return clients_ports
