# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.dv = webdriver.Firefox()
        self.dv.implicitly_wait(30)
    
    def test_add_contact(self):
        dv = self.dv
        dv.get("http://localhost/addressbook/edit.php")
        dv.find_element_by_name("user").click()
        dv.find_element_by_name("user").send_keys("admin")
        dv.find_element_by_name("pass").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | name=pass | ]]
        dv.find_element_by_name("pass").clear()
        dv.find_element_by_name("pass").send_keys("secret")
        dv.find_element_by_xpath("//input[@value='Login']").click()
        dv.find_element_by_name("theform").click()
        dv.find_element_by_name("firstname").click()
        dv.find_element_by_name("firstname").clear()
        dv.find_element_by_name("firstname").send_keys("Svetlana")
        dv.find_element_by_name("theform").click()
        dv.find_element_by_name("middlename").click()
        dv.find_element_by_name("middlename").clear()
        dv.find_element_by_name("middlename").send_keys("khsdks")
        dv.find_element_by_name("lastname").click()
        dv.find_element_by_name("lastname").clear()
        dv.find_element_by_name("lastname").send_keys("KKKKKK")
        dv.find_element_by_name("nickname").click()
        dv.find_element_by_name("nickname").clear()
        dv.find_element_by_name("nickname").send_keys("Nick")
        dv.find_element_by_name("company").click()
        dv.find_element_by_name("company").clear()
        dv.find_element_by_name("company").send_keys("Compa")
        dv.find_element_by_name("theform").click()
        dv.find_element_by_name("title").click()
        dv.find_element_by_name("title").clear()
        dv.find_element_by_name("title").send_keys("Title")
        dv.find_element_by_name("address").click()
        dv.find_element_by_name("address").clear()
        dv.find_element_by_name("address").send_keys("Add")
        dv.find_element_by_name("mobile").click()
        dv.find_element_by_name("mobile").clear()
        dv.find_element_by_name("mobile").send_keys("+75656567676")
        dv.find_element_by_name("home").click()
        dv.find_element_by_name("home").clear()
        dv.find_element_by_name("home").send_keys("+76565656767")
        dv.find_element_by_xpath("//div[@id='content']/form/label[14]").click()
        dv.find_element_by_name("email").click()
        dv.find_element_by_name("email").clear()
        dv.find_element_by_name("email").send_keys("gdesveta@noya.ru")
        dv.find_element_by_name("theform").click()
        dv.find_element_by_name("bday").click()
        Select(dv.find_element_by_name("bday")).select_by_visible_text("26")
        dv.find_element_by_xpath("//option[@value='26']").click()
        dv.find_element_by_name("bmonth").click()
        Select(dv.find_element_by_name("bmonth")).select_by_visible_text("August")
        dv.find_element_by_xpath("//option[@value='August']").click()
        dv.find_element_by_name("byear").click()
        dv.find_element_by_name("byear").clear()
        dv.find_element_by_name("byear").send_keys("1990")
        dv.find_element_by_name("theform").click()
        dv.find_element_by_name("address2").click()
        dv.find_element_by_name("address2").clear()
        dv.find_element_by_name("address2").send_keys("addr")
        dv.find_element_by_name("notes").click()
        dv.find_element_by_name("notes").clear()
        dv.find_element_by_name("notes").send_keys("hkda")
        dv.find_element_by_name("phone2").click()
        dv.find_element_by_name("phone2").clear()
        dv.find_element_by_name("phone2").send_keys("khad")
        dv.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        dv.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.dv.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.dv.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.dv.quit()

if __name__ == "__main__":
    unittest.main()
