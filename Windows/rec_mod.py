import sys
from rec_auto import *
from bs4 import BeautifulSoup
import urllib.request, urllib.error
import get_ingredients as g


class Rec(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # QtCore.QObject.connect()
        self.text = ""

    def setText(self, text):
        self.text = text
        print(text)
        self.run(text)

    def run(self, barcode):
        try:
           code = g.Barcode()
           ret = code.barcode(barcode)
           self.ui.label.setText(ret)
        except urllib.error.HTTPError:
            self.ui.label.setText("Internet connection is not working or an invalid barcode detected!")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Rec()
    myapp.show()
    sys.exit(app.exec_())
