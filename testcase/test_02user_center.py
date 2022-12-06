# coding=utf-8

from public.pages.basepages import Basepages
from public.pages.page_element import p
from time import sleep
from selenium import webdriver
from conf.config import data_path,report_path,pages_path
from public.utils.read_ini import read
import unittest

class User_Center(Basepages):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test_user_center(self):
        Basepages.click(Basepages.find_element(p.user_center))
if __name__ == '__main__':
    unittest.main()



