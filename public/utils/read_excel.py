# coding=utf-8

from conf.config import data_path
import os
import xlrd
file=os.path.join(data_path,"data.xls")
# book=xlrd.open_workbook(file)
# sheet=book.sheet_by_index(0)
# value=sheet.cell_value(1,0)
# print(value)
class Read_Excel(object):
    def __init__(self,file,index):
        self.book=xlrd.open_workbook(file)
        # self.sheet=self.book.sheet_by_index(index)
        self.sheet=self.book.sheet_by_name(index)
    def get_value(self,rows,cols):
        return self.sheet.cell_value(rows,cols)
b=Read_Excel(file,'Sheet1')
value=b.get_value(1,2)
print(value)





