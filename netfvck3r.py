import sys
from ui_main_window import MainWindowView
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QWidget


def get_qapplication_instance():
    if QApplication.instance():
        app = QApplication.instance()
    else:
        app = QApplication(sys.argv)
    return app


if __name__ == '__main__':

    print("[+] Starting...")
    app = get_qapplication_instance()
    view = MainWindowView()
    window = QMainWindow()
    view.setupUi(window)
    window.show()
    sys.exit(app.exec_())



