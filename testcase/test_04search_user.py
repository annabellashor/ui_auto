# coding=utf-8

from public.pages.basepages import Basepages
from public.pages.page_element import p
from time import sleep
class Search_User(Basepages):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    def test_04search_user(self):
        sleep(1)
        Basepages.get_driver().switch_to.default_content()
        iframe=Basepages.find_element(p.iframe_box)
        Basepages.get_driver().switch_to.frame(iframe)
        Basepages.send_keys(Basepages.find_element(p.searchValue),'admin')
        Basepages.click(Basepages.find_element(p.searchBtn))

