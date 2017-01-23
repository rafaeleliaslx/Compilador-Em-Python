from rayide import Ui_rayide
from PyQt4 import QtGui, QtCore
import sys, syntax
from rayide import _translate

class MyWindow(QtGui.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_rayide()
        self.ui.setupUi(self)

def main():
    app = QtGui.QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle(_translate("RayIDE", "RayIDE", None))
    highlight = syntax.PortugolHighlighter(w.ui.textEdit.document())
    # w.ui.textEdit.setFontFamily("monospace")
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()