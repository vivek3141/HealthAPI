import sys
from PyQt4 import QtCore, QtGui, uic 
import sqlite3
from sign_auto import *
import login_mod

class Sign(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pb_sign, QtCore.SIGNAL('clicked()'), self.sign)

    def sign(self):
        if self.ui.rb_y.isChecked():
            lactose = 1
        elif self.ui.rb_n.isChecked():
            lactose = 0
        if self.ui.rb_y_2.isChecked():
            diab = 1
        elif self.ui.rb_n_2.isChecked():
            diab = 0
        if self.ui.rb_y_3.isChecked():
            heart = 1
        elif self.ui.rb_n.isChecked():
            heart = 0
        else:
            QtGui.QMessageBox.warning(self, "Warning!",  "Please select the radiobuttons!")
            return False
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO username VALUES(?,?,?,?)", (self.ui.le_user.text(),lactose, heart, diab))
        except sqlite3.Error as e:
            if str(e).rstrip() == "UNIQUE constraint failed: username.username":
                QtGui.QMessageBox.warning(self, "Warning!", "Username already taken!")
                return False
            print(e)
            return False
        conn.commit()
        cursor.close()
        QtGui.QMessageBox.about(self, "Success!", "Successfully created account!")
        m = login_mod.Login()
        m.show()
        self.close()
        m.exec_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = Sign(None)
    myWindow.show()
    app.exec_()
