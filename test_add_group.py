# -*- coding: utf-8 -*-
import unittest
from group import Group
from application import Application


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()
    
    def test_add_group(self):
        #wd = self.wd
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(header="jnjhn", name="bjbjjhh", footer="nm"))
        #self.return_group_page(wd)
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(header="", name="", footer=""))
        self.app.logout()
    
    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
