import sys
from detect_auto import *
import login_mod
import rec_mod


class Detect(QtGui.QDialog):
    def __init__(self, parent=None, yes=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pb_detect, QtCore.SIGNAL('clicked()'), self.run)
        QtCore.QObject.connect(self.ui.pb_login, QtCore.SIGNAL('clicked()'), self.login)

    def send(self):
        pass

    def login(self):
        m = login_mod.Login()
        m.show()
        self.close()
        m.exec_()

    def run(self):
        text = self.ui.le_data.text()
        r = rec_mod.Rec()
        r.setText(text)
        r.show()
        r.exec_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Detect()
    myapp.show()
    sys.exit(app.exec_())
