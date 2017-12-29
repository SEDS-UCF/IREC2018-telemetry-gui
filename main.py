from PyQt5 import QtWidgets
import sys

# Local Module Imports
import app as a

# Create GUI application
app = QtWidgets.QApplication(sys.argv)
view = a.MyApp()
view.show()
app.exec_()
