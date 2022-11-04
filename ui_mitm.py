from PyQt5 import QtCore, QtGui, QtWidgets


class MITMView(QtWidgets.QWidget):
    start_arp_spoofing_signal = QtCore.pyqtSignal()
    stop_arp_spoofing_signal = QtCore.pyqtSignal()
    start_dns_spoofing_signal = QtCore.pyqtSignal()
    stop_dns_spoofing_signal = QtCore.pyqtSignal()
    start_code_injection_signal = QtCore.pyqtSignal()
    stop_code_injection_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 64, 19))
        self.label.setObjectName("label")
        self.target_1_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.target_1_ip.setGeometry(QtCore.QRect(10, 60, 113, 33))
        self.target_1_ip.setObjectName("target_1_ip")
        self.target_2_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.target_2_ip.setGeometry(QtCore.QRect(150, 60, 113, 33))
        self.target_2_ip.setObjectName("target_2_ip")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 40, 64, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 200, 101, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 101, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 230, 101, 19))
        self.label_5.setObjectName("label_5")
        self.redirect_from = QtWidgets.QLineEdit(self.centralwidget)
        self.redirect_from.setGeometry(QtCore.QRect(10, 250, 113, 33))
        self.redirect_from.setObjectName("redirect_from")
        self.redirect_to = QtWidgets.QLineEdit(self.centralwidget)
        self.redirect_to.setGeometry(QtCore.QRect(150, 250, 113, 33))
        self.redirect_to.setObjectName("redirect_to")
        self.arp_spoofing_running_label = QtWidgets.QLabel(self.centralwidget)
        self.arp_spoofing_running_label.setGeometry(QtCore.QRect(170, 110, 91, 19))
        self.arp_spoofing_running_label.setObjectName("arp_spoofing_running_label")
        self.arp_spoof_start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.arp_spoof_start_btn.setGeometry(QtCore.QRect(10, 100, 71, 31))
        self.arp_spoof_start_btn.setObjectName("arp_spoof_start_btn")
        self.dns_spoofing_running_label = QtWidgets.QLabel(self.centralwidget)
        self.dns_spoofing_running_label.setGeometry(QtCore.QRect(170, 300, 91, 19))
        self.dns_spoofing_running_label.setObjectName("dns_spoofing_running_label")
        self.label_code_injection_running = QtWidgets.QLabel(self.centralwidget)
        self.label_code_injection_running.setGeometry(QtCore.QRect(170, 660, 91, 19))
        self.label_code_injection_running.setObjectName("label_code_injection_running")
        self.code_to_inject = QtWidgets.QTextEdit(self.centralwidget)
        self.code_to_inject.setGeometry(QtCore.QRect(10, 450, 251, 191))
        self.code_to_inject.setObjectName("code_to_inject")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(90, 10, 101, 19))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(90, 400, 101, 19))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 430, 131, 19))
        self.label_11.setObjectName("label_11")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(320, 50, 931, 631))
        self.textBrowser.setObjectName("textBrowser")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 20, 131, 19))
        self.label_6.setObjectName("label_6")
        self.arp_spoof_stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.arp_spoof_stop_btn.setGeometry(QtCore.QRect(90, 100, 71, 31))
        self.arp_spoof_stop_btn.setObjectName("arp_spoof_stop_btn")
        self.dns_spoof_start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dns_spoof_start_btn.setGeometry(QtCore.QRect(10, 290, 71, 31))
        self.dns_spoof_start_btn.setObjectName("dns_spoof_start_btn")
        self.dns_spoof_stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dns_spoof_stop_btn.setGeometry(QtCore.QRect(90, 290, 71, 31))
        self.dns_spoof_stop_btn.setObjectName("dns_spoof_stop_btn")
        self.code_inject_start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.code_inject_start_btn.setGeometry(QtCore.QRect(10, 650, 71, 31))
        self.code_inject_start_btn.setObjectName("code_inject_start_btn")
        self.code_inject_stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.code_inject_stop_btn.setGeometry(QtCore.QRect(90, 650, 71, 31))
        self.code_inject_stop_btn.setObjectName("code_inject_stop_btn")
        self.network_interface = QtWidgets.QLineEdit(self.centralwidget)
        self.network_interface.setGeometry(QtCore.QRect(460, 10, 113, 33))
        self.network_interface.setObjectName("network_interface")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Man in the Middle"))
        self.label.setText(_translate("MainWindow", "Target 1:"))
        self.label_2.setText(_translate("MainWindow", "Target 2:"))
        self.label_3.setText(_translate("MainWindow", "DNS Spoofing"))
        self.label_4.setText(_translate("MainWindow", "Redirect from:"))
        self.label_5.setText(_translate("MainWindow", "Redirect to:"))
        self.arp_spoofing_running_label.setText(_translate("MainWindow", "Not running."))
        self.arp_spoof_start_btn.setText(_translate("MainWindow", "Start"))
        self.arp_spoof_start_btn.clicked.connect(self.start_arp_spoofing)
        self.dns_spoofing_running_label.setText(_translate("MainWindow", "Not running."))
        self.label_code_injection_running.setText(_translate("MainWindow", "Not running."))
        self.label_9.setText(_translate("MainWindow", "ARP Spoofing"))
        self.label_10.setText(_translate("MainWindow", "Code Injection"))
        self.label_11.setText(_translate("MainWindow", "Code to inject:"))
        self.label_6.setText(_translate("MainWindow", "Network interface:"))
        self.arp_spoof_stop_btn.setText(_translate("MainWindow", "Stop"))
        self.arp_spoof_stop_btn.clicked.connect(self.stop_arp_spoofing)
        self.dns_spoof_start_btn.setText(_translate("MainWindow", "Start"))
        self.dns_spoof_start_btn.clicked.connect(self.start_dns_spoofing)
        self.dns_spoof_stop_btn.setText(_translate("MainWindow", "Stop"))
        self.dns_spoof_stop_btn.clicked.connect(self.stop_dns_spoofing)
        self.code_inject_start_btn.setText(_translate("MainWindow", "Start"))
        self.code_inject_start_btn.clicked.connect(self.start_code_injection)
        self.code_inject_stop_btn.setText(_translate("MainWindow", "Stop"))
        self.code_inject_stop_btn.clicked.connect(self.stop_code_injection)

    def start_arp_spoofing(self):
        self.start_arp_spoofing_signal.emit()

    def stop_arp_spoofing(self):
        self.stop_arp_spoofing_signal.emit()

    def start_dns_spoofing(self):
        self.start_dns_spoofing_signal.emit()

    def stop_dns_spoofing(self):
        self.stop_dns_spoofing_signal.emit()

    def start_code_injection(self):
        self.start_code_injection_signal.emit()

    def stop_code_injection(self):
        self.stop_code_injection_signal.emit()

    def get_target1(self):
        return self.target_1_ip.text()

    def get_target2(self):
        return self.target_2_ip.text()

    def get_network_interface(self):
        return self.network_interface.text()

    def get_redirect_from_targets(self):
        return self.redirect_from.text()

    def get_redirect_to_targets(self):
        return self.redirect_to.text()

    def get_code_to_inject(self):
        return self.code_to_inject.toPlainText()