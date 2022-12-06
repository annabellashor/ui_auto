# coding=utf-8


import os
from conf.config import data_path
from configparser import ConfigParser

# file=os.path.join(data_path,"data.ini")

# class Read_Ini(ConfigParser):
#     def __init__(self,file):
#         super(Read_Ini, self).__init__()
#         self.read(file)
#     def get_value(self,section,option):
#         return self.get(section,option)
#
# if __name__ == '__main__':
#     file=os.path.join(data_path,"data.ini")
#     read=Read_Ini(file)
#     url=read.get_value("test_data","url")
#     print(url)


class Read_data_ini(ConfigParser):
    def read_ini(self,file):
        return self.read(file)
    def get_value(self,section,option):
        return self.get(section,option)
file=os.path.join(data_path,"data.ini")
read=Read_data_ini()
read.read_ini(file)

if __name__ == '__main__':
    # file=os.path.join(data_path,"data.ini")
    # r=Read_data_ini()
    # read.read_ini(file)
    value=read.get_value("test_data","url")
    print(value)










