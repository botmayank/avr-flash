from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import sys
import LCDblink_ui

class MainDialog(QDialog, LCDblink_ui.Ui_Dialog):

	def __init__(self, parent= None):
		super(MainDialog, self).__init__(parent)
		self.setupUi(self)
		self.workerThread1 = workerThread1()
		self.LCDButton.setFocus()
		self.connect(self.lineEdit, SIGNAL("textEdited(QString)"),self.workerThread1.ReplaceText)
		self.connect(self.LCDButton, SIGNAL("clicked()"), self.workerThread1.start)
		
	
class workerThread1(QThread):
	def __init__(self, parent = None):
		super(workerThread1, self).__init__(parent)
	
	dir1 = "C:\RobotechAVRGui\LCDString"
	text1 = "TEXT"
	def ReplaceText(self, QString):
		self.text1 = QString
		with open(self.dir1 + "\main.c", "wt") as fout:
			with open(self.dir1 + "\Shifting_Text_in_LCD_Module.c", "rt") as fin:
				for line in fin:
					fout.write(line.replace('Hello World', QString))

	def run(self):
		print "Changing Text now!"
		os.chdir(self.dir1)
		self.ReplaceText(self.text1)
		print "Text changed!\n"
		print "Flashing Code now!" 
		os.system('make all')
		os.system('avrdude -p atmega8 usb -c usbasp    -U flash:w:main.hex')
		os.system('make clean')
		print "LCD Code Flashed!"
		


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()

