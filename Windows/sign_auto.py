# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign.ui'
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
        Dialog.resize(550, 457)
        self.pb_sign = QtGui.QPushButton(Dialog)
        self.pb_sign.setGeometry(QtCore.QRect(190, 380, 141, 51))
        self.pb_sign.setStyleSheet(_fromUtf8("font: 16pt \"Segoe UI\";"))
        self.pb_sign.setObjectName(_fromUtf8("pb_sign"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 481, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setStyleSheet(_fromUtf8("font: 10pt \"Segoe UI\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.le_user = QtGui.QLineEdit(self.layoutWidget)
        self.le_user.setObjectName(_fromUtf8("le_user"))
        self.horizontalLayout.addWidget(self.le_user)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 291, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 130, 87, 87))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rb_y = QtGui.QRadioButton(self.groupBox)
        self.rb_y.setObjectName(_fromUtf8("rb_y"))
        self.verticalLayout.addWidget(self.rb_y)
        self.rb_n = QtGui.QRadioButton(self.groupBox)
        self.rb_n.setObjectName(_fromUtf8("rb_n"))
        self.verticalLayout.addWidget(self.rb_n)
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 551, 461))
        self.graphicsView.setStyleSheet(_fromUtf8("border-image: url(:/newPrefix/back.jpg) 0 0 0 0 stretch stretch;"))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(320, 130, 87, 87))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.rb_y_2 = QtGui.QRadioButton(self.groupBox_2)
        self.rb_y_2.setObjectName(_fromUtf8("rb_y_2"))
        self.verticalLayout_2.addWidget(self.rb_y_2)
        self.rb_n_2 = QtGui.QRadioButton(self.groupBox_2)
        self.rb_n_2.setObjectName(_fromUtf8("rb_n_2"))
        self.verticalLayout_2.addWidget(self.rb_n_2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(310, 100, 291, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(200, 260, 87, 87))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.rb_y_3 = QtGui.QRadioButton(self.groupBox_3)
        self.rb_y_3.setObjectName(_fromUtf8("rb_y_3"))
        self.verticalLayout_3.addWidget(self.rb_y_3)
        self.rb_n_3 = QtGui.QRadioButton(self.groupBox_3)
        self.rb_n_3.setObjectName(_fromUtf8("rb_n_3"))
        self.verticalLayout_3.addWidget(self.rb_n_3)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(160, 230, 291, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.graphicsView.raise_()
        self.pb_sign.raise_()
        self.layoutWidget.raise_()
        self.label_2.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.label_3.raise_()
        self.groupBox_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Sign Up", None))
        self.pb_sign.setText(_translate("Dialog", "Sign Up", None))
        self.label.setText(_translate("Dialog", "Enter a username", None))
        self.label_2.setText(_translate("Dialog", "Are you lactose intolerant?", None))
        self.rb_y.setText(_translate("Dialog", "Yes", None))
        self.rb_n.setText(_translate("Dialog", "No", None))
        self.rb_y_2.setText(_translate("Dialog", "Yes", None))
        self.rb_n_2.setText(_translate("Dialog", "No", None))
        self.label_3.setText(_translate("Dialog", "Are you diabetic?", None))
        self.rb_y_3.setText(_translate("Dialog", "Yes", None))
        self.rb_n_3.setText(_translate("Dialog", "No", None))
        self.label_4.setText(_translate("Dialog", "Do you have a heart condition?", None))

import resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

