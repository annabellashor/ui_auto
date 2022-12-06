# coding=utf-8

from public.pages.basepages import Basepages
from public.pages.page_element import p
from time import sleep
from selenium import webdriver
from conf.config import data_path,report_path,pages_path
from public.utils.read_ini import read
import unittest

url=read.get_value("test_data","url")
username=read.get_value("test_data","username")
password=read.get_value("test_data","password")

class Test_Login(Basepages):

    @classmethod
    def setUpClass(cls) -> None:
        Basepages.set_driver(webdriver.Chrome())

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(2)

    def test_01login(self):
        Basepages.driver.get(url)
        Basepages.driver.maximize_window()
        Basepages.send_keys(Basepages.find_element(p.username),username)
        Basepages.send_keys(Basepages.find_element(p.password),password)
        Basepages.click(Basepages.find_element(p.loginbtn))
    # def test_02user_center(self):
    #     sleep(1)
    #     Basepages.click(Basepages.find_element(p.user_center))
    # def test_03add_user(self):
    #     Basepages.wait(20)
    #     elem=Basepages.find_element(p.user_manage)
    #     Basepages.click(elem)
    #     iframe=Basepages.find_element(p.iframe_box)
    #     Basepages.get_driver().switch_to.frame(iframe)
    #     Basepages.click(Basepages.find_element(p.adduser))
if __name__ == '__main__':
    unittest.main()

