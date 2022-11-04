from PyQt5 import QtCore, QtGui, QtWidgets


class PortScannerView(QtWidgets.QWidget):
    scan_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("mainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ip_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_input.setGeometry(QtCore.QRect(60, 120, 221, 33))
        self.ip_input.setObjectName("ip_input")
        self.ports_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ports_input.setGeometry(QtCore.QRect(60, 190, 221, 33))
        self.ports_input.setObjectName("ports_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 90, 161, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 64, 19))
        self.label_2.setObjectName("label_2")
        self.results_table = QtWidgets.QTableWidget(self.centralwidget)
        self.results_table.setGeometry(QtCore.QRect(350, 30, 901, 661))
        self.results_table.setWordWrap(True)
        self.results_table.setObjectName("results_table")
        self.results_table.setColumnCount(4)
        self.results_table.setColumnWidth(0, 500)
        self.results_table.setRowCount(0)
        self.results_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(3, item)
        self.results_table.horizontalHeader().setCascadingSectionResizes(False)
        self.results_table.horizontalHeader().setDefaultSectionSize(100)
        self.results_table.horizontalHeader().setMinimumSectionSize(26)
        self.results_table.verticalHeader().setCascadingSectionResizes(False)
        self.scan_btn = QtWidgets.QPushButton(self.centralwidget)
        self.scan_btn.setGeometry(QtCore.QRect(60, 230, 221, 31))
        self.scan_btn.setObjectName("scan_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Port Scanner"))
        self.label.setText(_translate("MainWindow", "IP address or IP range:"))
        self.label_2.setText(_translate("MainWindow", "Ports:"))
        item = self.results_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "IP"))
        item = self.results_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MAC"))
        item = self.results_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Port"))
        item = self.results_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Service"))
        self.scan_btn.setText(_translate("MainWindow", "Scan"))
        self.scan_btn.clicked.connect(self.scan)


    def scan(self):
        self.scan_signal.emit()

    def get_ip(self):
        return self.ip_input.text()

    def get_ports(self):
        return self.ports_input.text()