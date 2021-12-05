from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re
import time


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        # fill form
        wd = self.app.wd
        self.app.open_page()
        self.fill_contact(contact)
        # submit contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        #wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def select_first_contacts(self):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]").click()

    def count_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # fill form
        self.fill_contact(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def fill_contact(self, contact):
        wd = self.app.wd
        self.change_field_contact("firstname", contact.firstname)
        self.change_field_contact("middlename", contact.middlename)
        self.change_field_contact("lastname", contact.lastname)
        self.change_field_contact("nickname", contact.nickname)
        self.change_field_contact("company", contact.Company)
        self.change_field_contact("title", contact.title)
        self.change_field_contact("address", contact.address)
        self.change_field_contact("mobile", contact.mobilephone)
        self.change_field_contact("work", contact.workphone)
        self.change_field_contact("home", contact.homephone)
        self.change_field_contact("email", contact.email)
        self.change_field_contact("email2", contact.email2)
        self.change_field_contact("email3", contact.email3)
        self.select_xpa("bday", contact.bday)
        self.select_xpa("bmonth", contact.bmonth)
        self.change_field_contact("byear", contact.byear)
        self.change_field_contact("address2", contact.address2)
        self.change_field_contact("notes", contact.notes)
        self.change_field_contact("phone2", contact.secondaryphone)

    def change_field_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                firstname = element.find_element_by_xpath(".//td[3]").text
                lastname = element.find_element_by_xpath(".//td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = element.find_element_by_xpath(".//td[4]").text
                all_mails = element.find_element_by_xpath(".//td[5]").text
                all_phones = element.find_element_by_xpath(".//td[6]").text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address, mails=all_mails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def select_xpa(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id = id, address=address, email=email, email2=email2, email3=email3,
                       homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone)











