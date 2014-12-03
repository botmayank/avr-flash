# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LCDblink3.ui'
#
# Created: Tue Jun 24 03:00:13 2014
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
        Dialog.resize(307, 231)
        self.LCDButton = QtGui.QPushButton(Dialog)
        self.LCDButton.setGeometry(QtCore.QRect(220, 30, 75, 23))
        self.LCDButton.setObjectName(_fromUtf8("LCDButton"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 181, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 274, 28))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.blinkDoubleSpinBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.blinkDoubleSpinBox.setMaximum(10000.0)
        self.blinkDoubleSpinBox.setProperty("value", 0.2)
        self.blinkDoubleSpinBox.setObjectName(_fromUtf8("blinkDoubleSpinBox"))
        self.horizontalLayout.addWidget(self.blinkDoubleSpinBox)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.blinkButton = QtGui.QPushButton(self.layoutWidget)
        self.blinkButton.setObjectName(_fromUtf8("blinkButton"))
        self.horizontalLayout.addWidget(self.blinkButton)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 131, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.PIRButton = QtGui.QPushButton(Dialog)
        self.PIRButton.setGeometry(QtCore.QRect(220, 100, 75, 23))
        self.PIRButton.setObjectName(_fromUtf8("PIRButton"))
        self.metalButton = QtGui.QPushButton(Dialog)
        self.metalButton.setGeometry(QtCore.QRect(220, 130, 75, 23))
        self.metalButton.setObjectName(_fromUtf8("metalButton"))
        self.soundButton = QtGui.QPushButton(Dialog)
        self.soundButton.setGeometry(QtCore.QRect(220, 160, 75, 23))
        self.soundButton.setObjectName(_fromUtf8("soundButton"))
        self.flexButton = QtGui.QPushButton(Dialog)
        self.flexButton.setGeometry(QtCore.QRect(220, 190, 75, 23))
        self.flexButton.setObjectName(_fromUtf8("flexButton"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 151, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 160, 141, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 190, 121, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))

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
        self.label_4.setText(_translate("Dialog", "Detect Human Presence:", None))
        self.PIRButton.setText(_translate("Dialog", "PIR Sensor", None))
        self.metalButton.setText(_translate("Dialog", "Metal Sensor", None))
        self.soundButton.setText(_translate("Dialog", "Sound Sensor", None))
        self.flexButton.setText(_translate("Dialog", "Flex Sensor", None))
        self.label_5.setText(_translate("Dialog", "Check if object is metallic:", None))
        self.label_6.setText(_translate("Dialog", "Measure Noise Level:", None))
        self.label_7.setText(_translate("Dialog", "Check Flex:", None))

