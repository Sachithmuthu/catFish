from data_excel_read import*
from data_excel_write import*

data_excel_write=data_excel_write()

class data_excel():

	def numData(self):
		number_of_data=data_excel_read.numSensors()
		print number_of_data

	def writeExcel(self,x_coordinate,y_coordinate):
		data_excel_write.addNew(x_coordinate,y_coordinate)