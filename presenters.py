from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import QThread
import subprocess
import requests
from network_scanner import Scanner
from arp_spoofer import ARPSpoofer
from dns_spoofer import DNSSpoofer
from code_injector import CodeInjector
from sniffer import Sniffer
from web_tester import WebTester


class PortScannerPresenter:
    def __init__(self, view):
        self.view = view
        self.view.scan_signal.connect(self.scan)

    def scan(self):
        try:
            ip = self.view.get_ip()
            ports = self.view.get_ports()
            ports_list_str = ports.split(",")
            ports_list_int = []
            for port in ports_list_str:
                ports_list_int.append(int(port))
            scanner = Scanner()
            clients_ports = scanner.scan(ip, ports_list_int)
            self.load_data(clients_ports)

        except ValueError:
            QMessageBox.warning(None, 'Error', 'Invalid port number!')

    def load_data(self, clients_ports):
        row_count = 0
        for entry in clients_ports:
            row_count = row_count + len(entry["ports_services"])
        self.view.results_table.setRowCount(row_count)
        row = 0
        for entry in clients_ports:
            for port_service in entry["ports_services"]:
                self.view.results_table.setItem(row, 0, QTableWidgetItem(entry["client"]["ip"]))
                entry["client"]["ip"] = ""
                self.view.results_table.setItem(row, 1, QTableWidgetItem(entry["client"]["mac"]))
                entry["client"]["mac"] = ""
                self.view.results_table.setItem(row, 2, QTableWidgetItem(str(port_service["port_number"])))
                self.view.results_table.setItem(row, 3, QTableWidgetItem(port_service["service"]))
                row = row+1

        self.view.results_table.resizeColumnsToContents()


class SnifferThread(QThread):
    def __init__(self, parent, view, arp_spoofer):
        super(SnifferThread, self).__init__(parent)
        self.view = view
        self.arp_spoofer = arp_spoofer

    def run(self):
        try:
            interface = self.view.get_network_interface()
            self.sniffer = Sniffer(interface, self.view.textBrowser)
            self.sniffer.sniff()
        except OSError:
            QMessageBox.warning(None, "Error", "Invalid network interface!")
            self.view.arp_spoofing_running_label.setText("Not running.")
            self.arp_spoofer.stop_spoofing()


class ARPSpooferThread(QThread):
    def __init__(self, parent, arp_spoofer):
        super(ARPSpooferThread, self).__init__(parent)
        self.arp_spoofer = arp_spoofer

    def run(self):
        self.arp_spoofer.spoof()


class DNSSpooferThread(QThread):
    def __init__(self, parent, dns_spoofer):
        super(DNSSpooferThread, self).__init__(parent)
        self.dns_spoofer = dns_spoofer

    def run(self):
        self.dns_spoofer.spoof_dns()


class CodeInjectorThread(QThread):
    def __init__(self, parent, code_injector):
        super(CodeInjectorThread, self).__init__(parent)
        self.code_injector = code_injector

    def run(self):
        self.code_injector.inject_code()


class MITMPresenter:
    def __init__(self, view, window):
        self.view = view
        self.window = window
        self.view.start_arp_spoofing_signal.connect(self.start_arp_spoofing)
        self.view.stop_arp_spoofing_signal.connect(self.stop_arp_spoofing)
        self.view.start_dns_spoofing_signal.connect(self.start_dns_spoofing)
        self.view.stop_dns_spoofing_signal.connect(self.stop_dns_spoofing)
        self.view.start_code_injection_signal.connect(self.start_code_injection)
        self.view.stop_code_injection_signal.connect(self.stop_code_injection)

    def start_arp_spoofing(self):
        self.view.arp_spoofing_running_label.setText("Running.")
        target1 = self.view.get_target1()
        target2 = self.view.get_target2()
        self.arp_spoofer = ARPSpoofer(target1, target2, self.view.textBrowser)
        spoofer_thread = ARPSpooferThread(self.window, self.arp_spoofer)
        sniffer_thread = SnifferThread(self.window, self.view, self.arp_spoofer)
        spoofer_thread.start()
        sniffer_thread.start()

    def stop_arp_spoofing(self):
        self.view.arp_spoofing_running_label.setText("Not running.")
        self.arp_spoofer.stop_spoofing()

    def start_dns_spoofing(self):
        self.view.dns_spoofing_running_label.setText("Running.")
        from_targets = self.view.get_redirect_from_targets()
        to_targets = self.view.get_redirect_to_targets()
        from_targets_list_raw = from_targets.split(",")
        from_targets_list = []
        for target in from_targets_list_raw:
            from_targets_list.append(target.replace(" ", ""))
        self.dns_spoofer = DNSSpoofer(from_targets_list, to_targets)
        self.dns_spoofer_thread = DNSSpooferThread(self.window, self.dns_spoofer)
        self.dns_spoofer_thread.start()

    def stop_dns_spoofing(self):
        self.view.dns_spoofing_running_label.setText("Not running.")
        self.dns_spoofer.stop_spoofing_dns()
        self.dns_spoofer_thread.quit()
        subprocess.call("iptables --flush", shell=True)

    def start_code_injection(self):
        self.view.label_code_injection_running.setText("Running.")
        code_to_inject = self.view.get_code_to_inject()
        self.code_injector = CodeInjector(code_to_inject)
        self.code_injector_thread = CodeInjectorThread(self.window, self.code_injector)
        self.code_injector_thread.start()

    def stop_code_injection(self):
        self.view.label_code_injection_running.setText("Not running.")
        self.code_injector.stop_injecting()
        self.code_injector_thread.quit()


class WebTesterPresenter:
    def __init__(self, view):
        self.view = view
        self.view.scan_signal.connect(self.scan_url)

    def scan_url(self):
        try:
            url = self.view.get_url()
            urls_to_ignore = self.view.get_urls_to_ignore()
            urls_to_ignore_list_raw = urls_to_ignore.split(",")
            urls_to_ignore_list = []
            for ignore_url in urls_to_ignore_list_raw:
                urls_to_ignore_list.append(ignore_url.replace(" ", ""))
            login_url = self.view.get_login_url()
            login_data = self.view.get_login_info()

            web_tester = WebTester(url, login_url, urls_to_ignore_list)
            vulns = web_tester.start(login_data)
            self.view.results_table.setRowCount(len(vulns))
            row = 0
            for entry in vulns:
                self.view.results_table.setItem(row, 0, QTableWidgetItem(entry["vulnerability"]))
                self.view.results_table.setItem(row, 1, QTableWidgetItem(entry["url"]))
                self.view.results_table.setItem(row, 2, QTableWidgetItem(entry["form_or_url"]))
                self.view.results_table.setItem(row, 3, QTableWidgetItem(entry["injection_string"]))
                row = row+1

            self.view.results_table.resizeColumnsToContents()
        except requests.exceptions.MissingSchema:
            QMessageBox().warning(None, 'Error', 'Unable to scan this URL!')