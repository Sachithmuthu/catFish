from xlutils.copy import copy
from xlrd import *
from data_excel_read import*

file_loc= '/home/sachith/catFish/catFish_excel.xlsx' 

data_excel_read=data_excel_read()

class data_excel_write():

	def __init__(self):
		self.position=data_excel_read.numSensors()+1
		self.workbook = copy(open_workbook(file_loc))

	def addNew(self,sensor,actuator):
		self.workbook.get_sheet(0).write(self.position,0,sensor)
		self.workbook.get_sheet(0).write(self.position,1,actuator)
		self.workbook.save(file_loc)
		self.position=self.position+1