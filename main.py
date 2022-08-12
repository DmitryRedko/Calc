from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from calc import Ui_MainWindow
from calcwidget import Ui_Form

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MW = Ui_MainWindow()
MW.setupUi(MainWindow)
MainWindow.show()

#

def openOtherWindow():
    global Form
    Form = QtWidgets.QWidget()
    WDG = Ui_Form()
    WDG.setupUi(Form)
    Form.show()
    WDG.add_functions(MW)


MW.consts.clicked.connect(openOtherWindow)


sys.exit(app.exec_())
