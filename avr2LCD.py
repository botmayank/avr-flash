# -*- coding: utf-8 -*-
#Blink using SpinBox for adjusting the delay using LCDblink2_ui

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import sys
import LCDblink2_ui

class MainDialog(QDialog, LCDblink2_ui.Ui_Dialog):

	def __init__(self, parent= None):
		super(MainDialog, self).__init__(parent)
		self.setupUi(self)
		self.workerThread1 = workerThread1()
		self.workerThread2 = workerThread2()

		self.LCDButton.setFocus()

		self.connect(self.blinkDoubleSpinBox, SIGNAL("valueChanged(QString)"),self.workerThread2.ReplaceDelay)
		self.connect(self.lineEdit, SIGNAL("textEdited(QString)"),self.workerThread1.ReplaceText)
		self.connect(self.LCDButton, SIGNAL("clicked()"), self.workerThread1.start)
		self.connect(self.blinkButton, SIGNAL("clicked()"),self.workerThread2.start)
	
class workerThread1(QThread):
	def __init__(self, parent = None):
		super(workerThread1, self).__init__(parent)

	dir = 	"C:\RobotechAVRGui"
	dirLCD = dir + "\LCDString"
	
	text1 = "TEXT"

	def ReplaceText(self, QString):
		self.text1 = QString
		with open(self.dirLCD + "\main.c", "wt") as fout:
			with open(self.dirLCD + "\Shifting_Text_in_LCD_Module.c", "rt") as fin:
				for line in fin:
					fout.write(line.replace('Hello World', QString))

	def run(self):
		print "\nChanging Text now!"
		os.chdir(self.dirLCD)
		self.ReplaceText(self.text1)
		print "\nText changed!\n"
		print "Flashing LCD Code now!" 
		os.system('make all')
		os.system('avrdude -p atmega8 usb -c usbasp    -U flash:w:main.hex')
		os.system('make clean')
		print "LCD Code Flashed!"
		


class workerThread2(QThread):
	def __init__(self, parent = None):
		super(workerThread2, self).__init__(parent)
	
	dir = 	"C:\RobotechAVRGui"
	dirBlink = dir + "\Blink1"
	delay = 200

	def ReplaceDelay(self, value):

		self.delay = value.toDouble()[0]*1000
		print QString(self.delay)

		with open(self.dirBlink + "\main.c", "wt") as fout:
			with open(self.dirBlink + "\BlinkTemp.c", "rt") as fin:
				for line in fin:
					#print QString(self.delay)
					fout.write(line.replace("200", QString(self.delay)))

	def run(self):
		print "\nChanging delay now!"
		os.chdir(self.dirBlink)
		self.ReplaceDelay(QString(self.delay))
		print "\nDelay changed!\n"
		print "Flashing Blink Code now!"    
		# os.chdir(self.dirBlink)
		os.system('make all')
		os.system('avrdude -p atmega8 usb -c usbasp    -U flash:w:main.hex')
		os.system('make clean')
		print "Blink Code Flashed!"
		



app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()

