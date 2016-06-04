import xlrd
file_location= '/home/sachith/catFish/catFish_excel.xlsx'

class data_excel_read():

	def __init__(self):
		workbook=xlrd.open_workbook(file_location)
		sheet=workbook.sheet_by_index(0)

		self.cols=sheet.ncols
		self.rows=sheet.nrows
		self.sens=0
		self.act=0
		self.number_of_sensors=self.rows-1

		self.data=[[sheet.cell_value(r,c) for c in range(self.cols)] for r in range(self.rows)]


	def numSensors(self):
		return self.number_of_sensors
