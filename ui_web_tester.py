from PyQt5 import QtCore, QtGui, QtWidgets


class WebTesterView(QtWidgets.QWidget):
    scan_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.results_table = QtWidgets.QTableWidget(self.centralwidget)
        self.results_table.setGeometry(QtCore.QRect(370, 20, 901, 661))
        self.results_table.setWordWrap(True)
        self.results_table.setObjectName("results_table")
        self.results_table.setColumnCount(4)
        self.results_table.setRowCount(0)
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 111, 19))
        self.label_2.setObjectName("label_2")
        self.url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(60, 120, 221, 33))
        self.url_input.setObjectName("url_input")
        self.scan_btn = QtWidgets.QPushButton(self.centralwidget)
        self.scan_btn.setGeometry(QtCore.QRect(70, 510, 221, 31))
        self.scan_btn.setObjectName("scan_btn")
        self.urls_to_ignore_input = QtWidgets.QLineEdit(self.centralwidget)
        self.urls_to_ignore_input.setGeometry(QtCore.QRect(60, 190, 221, 33))
        self.urls_to_ignore_input.setObjectName("urls_to_ignore_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 90, 161, 19))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 270, 141, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 340, 81, 19))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 340, 81, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 370, 81, 19))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 410, 71, 19))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 450, 64, 19))
        self.label_8.setObjectName("label_8")
        self.username_input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input_name.setGeometry(QtCore.QRect(102, 360, 121, 33))
        self.username_input_name.setObjectName("username_input_name")
        self.username_input_value = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input_value.setGeometry(QtCore.QRect(230, 360, 121, 33))
        self.username_input_value.setObjectName("username_input_value")
        self.password_input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input_name.setGeometry(QtCore.QRect(102, 400, 121, 33))
        self.password_input_name.setObjectName("password_input_name")
        self.password_input_value = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input_value.setGeometry(QtCore.QRect(230, 400, 121, 33))
        self.password_input_value.setObjectName("password_input_value")
        self.submit_input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.submit_input_name.setGeometry(QtCore.QRect(102, 440, 121, 33))
        self.submit_input_name.setObjectName("submit_input_name")
        self.submit_input_value = QtWidgets.QLineEdit(self.centralwidget)
        self.submit_input_value.setGeometry(QtCore.QRect(230, 440, 121, 33))
        self.submit_input_value.setObjectName("submit_input_value")
        self.login_url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.login_url_input.setGeometry(QtCore.QRect(100, 300, 121, 33))
        self.login_url_input.setObjectName("login_url_input")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 310, 91, 19))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Web Tester"))
        item = self.results_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Vulnerability"))
        item = self.results_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "URL"))
        item = self.results_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Found in"))
        item = self.results_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Injection string"))
        self.results_table.resizeColumnsToContents()
        self.label_2.setText(_translate("MainWindow", "URLs to ignore:"))
        self.scan_btn.setText(_translate("MainWindow", "Scan"))
        self.scan_btn.clicked.connect(self.scan)
        self.label.setText(_translate("MainWindow", "URL:"))
        self.label_3.setText(_translate("MainWindow", "Login data (optional):"))
        self.label_4.setText(_translate("MainWindow", "Input name"))
        self.label_5.setText(_translate("MainWindow", "Value"))
        self.label_6.setText(_translate("MainWindow", "Username"))
        self.label_7.setText(_translate("MainWindow", "Password"))
        self.label_8.setText(_translate("MainWindow", "Submit"))
        self.label_9.setText(_translate("MainWindow", "Login URL"))

    def scan(self):
        self.scan_signal.emit()

    def get_url(self):
        return self.url_input.text()

    def get_urls_to_ignore(self):
        return self.urls_to_ignore_input.text()

    def get_login_url(self):
        return self.login_url_input.text()

    def get_login_info(self):
        return {self.username_input_name.text(): self.username_input_value.text(),
                self.password_input_name.text(): self.password_input_value.text(),
                self.submit_input_name.text(): self.submit_input_value.text()}
