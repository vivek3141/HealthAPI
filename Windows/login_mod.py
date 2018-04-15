import sys
from PyQt4 import QtCore, QtGui, uic
import sqlite3
from login_auto import *
import sign_mod
import detect_mod as dd

  

class Login(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pb_login, QtCore.SIGNAL('clicked()'), self.login)
        QtCore.QObject.connect(self.ui.pb_signup, QtCore.SIGNAL('clicked()'), self.sign)

    def sign(self):
        m = sign_mod.Sign(None)
        m.show()
        self.close()
        m.exec_()

    def login(self):
        t = self.ui.le_login.text()
        user = t
        c = sqlite3.connect("data.db")
        cur = c.cursor()
        cur.execute("select * from user where username='" + user + "'")
        li = cur.fetchall()
        if li == [()]:
            return False
        if self.ui.cb_r.isChecked():
            with open("user.txt", "w") as f:
                for x in li[0]:
                    f.writelines(str(x) + "\n")
        s = dd.Detect()
        s.show()
        s.exec_()
        return True


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = Login(None)
    myWindow.show()
    app.exec_()
