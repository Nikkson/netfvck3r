from PyQt5 import QtCore, QtGui, QtWidgets
from ui_port_scanner import PortScannerView
from ui_mitm import MITMView
from ui_web_tester import WebTesterView
from presenters import PortScannerPresenter, MITMPresenter, WebTesterPresenter


class MainWindowView(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def setupUi(self, MainWindow):
        print("[+] Launching GUI...")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 420, 801, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gridLayoutWidget)
        self.horizontalLayout.setContentsMargins(40, 0, 40, 0)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scanner_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.scanner_btn.setObjectName("scanner_btn")
        self.horizontalLayout.addWidget(self.scanner_btn)
        self.mitm_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.mitm_btn.setObjectName("mitm_btn")
        self.horizontalLayout.addWidget(self.mitm_btn)
        self.web_tester_btn = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.web_tester_btn.setObjectName("web_tester_btn")
        self.horizontalLayout.addWidget(self.web_tester_btn)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 60, 411, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ascii_art_cat.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NETFVCK3R"))
        self.scanner_btn.setText(_translate("MainWindow", "Port Scanner"))
        self.scanner_btn.clicked.connect(self.open_port_scanner)
        self.mitm_btn.setText(_translate("MainWindow", "Man in the Middle"))
        self.mitm_btn.clicked.connect(self.open_mitm)
        self.web_tester_btn.setText(_translate("MainWindow", "Website Tester"))
        self.web_tester_btn.clicked.connect(self.open_web_tester)

    def open_web_tester(self):
        self.window = QtWidgets.QMainWindow()
        self.web_tester_view = WebTesterView()
        self.presenter = WebTesterPresenter(self.web_tester_view)
        self.web_tester_view.setupUi(self.window)
        self.window.show()

    def open_port_scanner(self):
        self.window = QtWidgets.QMainWindow()
        self.port_scanner_view = PortScannerView()
        self.presenter = PortScannerPresenter(self.port_scanner_view)
        self.port_scanner_view.setupUi(self.window)
        self.window.show()

    def open_mitm(self):
        self.window = QtWidgets.QMainWindow()
        self.mitm_view = MITMView()
        self.presenter = MITMPresenter(self.mitm_view, self.window)
        self.mitm_view.setupUi(self.window)
        self.window.show()