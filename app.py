from PyQt5.QtWidgets import QApplication, QMainWindow
import gui


class MyApp(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
