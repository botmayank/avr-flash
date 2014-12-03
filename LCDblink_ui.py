# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LCDblink.ui'
#
# Created: Mon Jun 23 20:21:32 2014
#      by: PyQt4 UI code generator 4.10
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
        Dialog.resize(324, 117)
        self.LCDButton = QtGui.QPushButton(Dialog)
        self.LCDButton.setGeometry(QtCore.QRect(190, 30, 75, 23))
        self.LCDButton.setObjectName(_fromUtf8("LCDButton"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 161, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.blinkButton = QtGui.QPushButton(Dialog)
        self.blinkButton.setGeometry(QtCore.QRect(190, 60, 75, 23))
        self.blinkButton.setObjectName(_fromUtf8("blinkButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.LCDButton)
        Dialog.setTabOrder(self.LCDButton, self.blinkButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "AVRFlasher", None))
        self.LCDButton.setText(_translate("Dialog", "Burn!", None))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter your text here", None))
        self.label.setText(_translate("Dialog", "Show Text on the LCD:", None))
        self.label_2.setText(_translate("Dialog", "Blink an LED:", None))
        self.blinkButton.setText(_translate("Dialog", "Blink!", None))

