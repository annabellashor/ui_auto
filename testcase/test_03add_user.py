# coding=utf-8

from public.pages.basepages import Basepages
from public.pages.page_element import p
from time import sleep
from selenium import webdriver
from conf.config import data_path,report_path,pages_path
from public.utils.read_ini import read
import unittest
from public.pages.basepages import get_name

class Add_User(Basepages):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test_add_user(self):
        Basepages.wait(5)
        Basepages.click(Basepages.find_element(p.user_manage))
        iframe=Basepages.find_element(p.iframe_box)
        Basepages.get_driver().switch_to.frame(iframe)
        Basepages.click(Basepages.find_element(p.adduser))
        iframe1=Basepages.find_element(p.iframe1)
        Basepages.get_driver().switch_to.frame(iframe1)
        Basepages.send_keys(Basepages.find_element(p.userName),get_name())
        Basepages.click(Basepages.find_element(p.sex_nv))
        Basepages.send_keys(Basepages.find_element(p.user_email),get_name()+"@qq.com")
        Basepages.send_keys(Basepages.find_element(p.loginPwd),"123456")
        Basepages.send_keys(Basepages.find_element(p.confirmPwd),"123456")
        Basepages.send_keys(Basepages.find_element(p.user_tel),"13012345678")
        Basepages.send_keys(Basepages.find_element(p.userAccount),get_name())
        Basepages.click(Basepages.find_element(p.submitBtn))
        sleep(1)




if __name__ == '__main__':
    unittest.main()

