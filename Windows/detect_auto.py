# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detect.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(497, 370)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.pb_detect = QtGui.QPushButton(Dialog)
        self.pb_detect.setGeometry(QtCore.QRect(100, 120, 291, 151))
        self.pb_detect.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.pb_detect.setObjectName(_fromUtf8("pb_detect"))
        self.pb_login = QtGui.QPushButton(Dialog)
        self.pb_login.setGeometry(QtCore.QRect(20, 20, 112, 34))
        self.pb_login.setObjectName(_fromUtf8("pb_login"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 300, 351, 41))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 501, 371))
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(:/newPrefix/back.jpg) 0 0 0 0 stretch stretch;"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.le_data = QtGui.QLineEdit(Dialog)
        self.le_data.setGeometry(QtCore.QRect(130, 310, 113, 27))
        self.le_data.setObjectName(_fromUtf8("le_data"))
        self.graphicsView.raise_()
        self.pb_detect.raise_()
        self.pb_login.raise_()
        self.label.raise_()
        self.le_data.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Detect", None))
        self.pb_detect.setText(_translate("Dialog", "Detect", None))
        self.pb_login.setText(_translate("Dialog", "Login", None))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

