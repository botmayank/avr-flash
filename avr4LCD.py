#Normal Code for Blink@200ms on all of PortB and LCD String using LCDblink_ui

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import sys
import subprocess
import LCDblink3_ui

class MainDialog(QDialog, LCDblink3_ui.Ui_Dialog):

	def __init__(self, parent= None):
		super(MainDialog, self).__init__(parent)
		self.setupUi(self)
		self.workerThread1 = workerThread1()
		self.workerThread2 = workerThread2()
		self.workerThread3 = workerThread3()
		self.workerThread4 = workerThread4()
		self.workerThread5 = workerThread5()
		self.workerThread6 = workerThread6()

		self.LCDButton.setFocus()

		self.connect(self.lineEdit, SIGNAL("textEdited(QString)"),self.workerThread1.ReplaceText)
		self.connect(self.LCDButton, SIGNAL("clicked()"), self.workerThread1.start)
		self.connect(self.blinkButton, SIGNAL("clicked()"),self.workerThread2.start)
		self.connect(self.PIRButton, SIGNAL("clicked()"), self.workerThread3.start)
		self.connect(self.metalButton, SIGNAL("clicked()"), self.workerThread4.start)
		self.connect(self.soundButton, SIGNAL("clicked()"), self.workerThread5.start)
		self.connect(self.flexButton, SIGNAL("clicked()"), self.workerThread6.start)
	
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
		subprocess.call('make all', shell = True) #To hide the command shell :D
		subprocess.call('avrdude -p atmega8 usb -c usbasp    -U flash:w:main.hex', shell = True)
		subprocess.call('make clean', shell = True)
		print "LCD Code Flashed!"
		


class workerThread2(QThread):
	def __init__(self, parent = None):
		super(workerThread2, self).__init__(parent)
	
	dir = 	"C:\RobotechAVRGui"
	dirBlink = dir + "\Blink1"

	def run(self):
		print "Flashing Blink Code now!"    
		os.chdir(self.dirBlink)
		subprocess.call('make all', shell = True)
		subprocess.call('avrdude -p atmega8 usb -c usbasp    -U flash:w:main.hex', shell = True)
		subprocess.call('make clean', shell = True)
		print "Blink Code Flashed!"

class workerThread3(QThread):
	def __init__(self, parent = None):
		super(workerThread3, self).__init__(parent)
	
	dir = 	"C:\RobotechAVRGui"
	dirPIR = dir + "\PIR"

	def run(self):
		print "Flashing PIR Code now!"    
		os.chdir(self.dirPIR)
		subprocess.call('make all', shell = True)
		subprocess.call('avrdude -p atmega8 usb -c usbasp    -U flash:w:main.hex', shell = True)
		subprocess.call('make clean', shell = True)
		print "PIR Code Flashed!"

class workerThread4(QThread):
	def __init__(self, parent = None):
		super(workerThread4, self).__init__(parent)
	
	dir = 	"C:\RobotechAVRGui"
	dirMetal = dir + "\MetalSensor"

	def run(self):
		print "Flashing Metal Code now!"    
		os.chdir(self.dirMetal)
		subprocess.call('make all', shell = True)
		subprocess.call('avrdude -p atmega8 usb -c usbasp    -U flash:w:main.hex', shell = True)
		subprocess.call('make clean', shell = True)
		print "Metal Code Flashed!"

class workerThread5(QThread):
	def __init__(self, parent = None):
		super(workerThread5, self).__init__(parent)
	
	dir = 	"C:\RobotechAVRGui"
	dirSound = dir + "\SoundSensor"

	def run(self):
		print "Flashing Sound Sensor Code now!"    
		os.chdir(self.dirSound)
		subprocess.call('make all', shell = True)
		subprocess.call('avrdude -p atmega8 usb -c usbasp    -U flash:w:main.hex', shell = True)
		subprocess.call('make clean', shell = True)
		print "Sound Sensor Code Flashed!"

class workerThread6(QThread):
	def __init__(self, parent = None):
		super(workerThread6, self).__init__(parent)
	
	dir = 	"C:\RobotechAVRGui"
	dirFlex = dir + "\FlexSensor"

	def run(self):
		print "Flashing Flex Code now!"    
		os.chdir(self.dirFlex)
		subprocess.call('make all', shell = True)
		subprocess.call('avrdude -p atmega8 usb -c usbasp    -U flash:w:main.hex', shell = True)
		subprocess.call('make clean', shell = True)
		print "Flex Code Flashed!"





app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()

