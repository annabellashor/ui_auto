# coding=utf-8

import unittest
from selenium import webdriver
import pymysql
import random
# driver=webdriver.Chrome()
# driver.implicitly_wait()
class Basepages(unittest.TestCase):
    @classmethod
    def set_driver(cls,driver):
        cls.driver=driver
    @classmethod
    def get_driver(cls):
        return cls.driver
    @classmethod
    def find_element(cls,list):
        type=list[0]
        value=list[1]
        if type=="id":
            elem=cls.driver.find_element_by_id(value)
        elif type=="class":
            elem=cls.driver.find_element_by_class_name(value)
        elif type=="xpath":
            elem=cls.driver.find_element_by_xpath(value)
        elif type=="css":
            elem=cls.driver.find_element_by_css_selector(value)
        elif type=="name":
            elem=cls.driver.find_element_by_name(value)
        elif type=="link_text":
            elem=cls.driver.find_element_by_link_text(value)
        else:
            raise ValueError("please input correct type!")
        return elem
    @classmethod
    def send_keys(cls,elem,text):
        return elem.send_keys(text)
    @classmethod
    def click(cls,elem):
        return elem.click()
    @classmethod
    def  wait(cls,scend):
        return cls.driver.implicitly_wait(scend)
def get_name():
    # db=pymysql.connect(host="192.168.153.128",
    #                    user="root",
    #                    password="123456",
    #                    database="chengdu11",
    #                    port=3306)
    # cursor=db.cursor()

    str1="qwertyuiopasdfghjklzxcvbnmm"
    str2=""
    for i in range(6):
        str2=str2+random.choice(str1)
    # cursor.execute("insert into cms_user_name values(%s)"%str2)
    return str2
if __name__ == '__main__':
    from conf.config import data_path
    import os
    from public.utils.read_ini import Read_data_ini
    file=os.path.join(data_path,"data.ini")
    r=Read_data_ini()
    r.read_ini(file)
    value=r.get_value("test_data","url")
    value1=r.get_value("test_data","username")
    value2=r.get_value("test_data","password")
    Basepages.set_driver(webdriver.Chrome())
    # Basepages.get_driver()
    # Basepages.maximize_window()
    Basepages.get_driver().maximize_window()
    # Basepages.get(value)
    Basepages.get_driver().get(value)
    list1=["id","userAccount"]
    list2=["name","loginPwd"]
    list3=["xpath",'//*[@id="loginBtn"]']
    Basepages.send_keys(Basepages.find_element(list1),value1)
    Basepages.send_keys(Basepages.find_element(list2),value2)
    Basepages.click(Basepages.find_element(list3))
