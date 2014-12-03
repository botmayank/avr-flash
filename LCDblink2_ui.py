# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LCDblink2.ui'
#
# Created: Tue Jun 24 02:05:49 2014
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
        Dialog.resize(315, 117)
        self.LCDButton = QtGui.QPushButton(Dialog)
        self.LCDButton.setGeometry(QtCore.QRect(220, 30, 75, 23))
        self.LCDButton.setObjectName(_fromUtf8("LCDButton"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 60, 274, 28))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.blinkDoubleSpinBox = QtGui.QDoubleSpinBox(self.widget)
        self.blinkDoubleSpinBox.setMaximum(10000.0)
        self.blinkDoubleSpinBox.setProperty("value", 0.2)
        self.blinkDoubleSpinBox.setObjectName(_fromUtf8("blinkDoubleSpinBox"))
        self.horizontalLayout.addWidget(self.blinkDoubleSpinBox)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.blinkButton = QtGui.QPushButton(self.widget)
        self.blinkButton.setObjectName(_fromUtf8("blinkButton"))
        self.horizontalLayout.addWidget(self.blinkButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.LCDButton)
        Dialog.setTabOrder(self.LCDButton, self.blinkButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "AVRFlasher", None))
        self.LCDButton.setText(_translate("Dialog", "Burn!", None))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter your text here...", None))
        self.label.setText(_translate("Dialog", "Show Text on the LCD:", None))
        self.label_2.setText(_translate("Dialog", "Blink an LED \n"
"with delay", None))
        self.label_3.setText(_translate("Dialog", "seconds", None))
        self.blinkButton.setText(_translate("Dialog", "Blink!", None))

