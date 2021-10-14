from selenium.webdriver.support.ui import Select


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

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def eddit_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[22]").click()

    # def fill_contact(self, contact):
    #     wd = self.app.wd
    #     wd.find_element_by_name("firstname").click()
    #     wd.find_element_by_name("firstname").clear()
    #     wd.find_element_by_name("firstname").send_keys(contact.firstname)
    #     wd.find_element_by_name("middlename").click()
    #     wd.find_element_by_name("middlename").clear()
    #     wd.find_element_by_name("middlename").send_keys(contact.middlename)
    #     wd.find_element_by_name("lastname").click()
    #     wd.find_element_by_name("lastname").clear()
    #     wd.find_element_by_name("lastname").send_keys(contact.lastname)
    #     wd.find_element_by_name("nickname").click()
    #     wd.find_element_by_name("nickname").send_keys(contact.nickname)
    #     wd.find_element_by_name("company").click()
    #     wd.find_element_by_name("company").clear()
    #     wd.find_element_by_name("company").send_keys(contact.Company)
    #     wd.find_element_by_name("title").click()
    #     wd.find_element_by_name("title").clear()
    #     wd.find_element_by_name("title").send_keys(contact.titlen)
    #     wd.find_element_by_name("address").click()
    #     wd.find_element_by_name("address").clear()
    #     wd.find_element_by_name("address").send_keys(contact.address)
    #     wd.find_element_by_name("mobile").click()
    #     wd.find_element_by_name("mobile").clear()
    #     wd.find_element_by_name("mobile").send_keys(contact.mobile)
    #     wd.find_element_by_name("home").click()
    #     wd.find_element_by_name("home").clear()
    #     wd.find_element_by_name("home").send_keys(contact.homephone)
    #     wd.find_element_by_name("email").click()
    #     wd.find_element_by_name("email").clear()
    #     wd.find_element_by_name("email").send_keys(contact.mail)
    #     wd.find_element_by_name("bday").click()
    #     Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
    #     wd.find_element_by_name("bmonth").click()
    #     Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmouth)
    #     wd.find_element_by_name("byear").click()
    #     wd.find_element_by_name("byear").clear()
    #     wd.find_element_by_name("byear").send_keys(contact.byear)
    #     wd.find_element_by_name("address2").click()
    #     wd.find_element_by_name("address2").clear()
    #     wd.find_element_by_name("address2").send_keys(contact.address2)
    #     wd.find_element_by_name("notes").click()
    #     wd.find_element_by_name("notes").clear()
    #     wd.find_element_by_name("notes").send_keys(contact.notes)
    #     wd.find_element_by_name("phone2").click()
    #     wd.find_element_by_name("phone2").clear()
    #     wd.find_element_by_name("phone2").send_keys(contact.phone2)

    def count_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # fill form
        self.fill_contact(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()

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
        self.change_field_contact("mobile", contact.mobile)
        self.change_field_contact("home", contact.homephone)
        self.change_field_contact("email", contact.mail)
        self.select_xpa("bday", contact.bday)
        self.select_xpa("bmonth", contact.bmonth)
        self.change_field_contact("byear", contact.byear)
        self.change_field_contact("address2", contact.address2)
        self.change_field_contact("notes", contact.notes)
        self.change_field_contact("phone2", contact.phone2)

    def change_field_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

        # def fill_contact(self, contact):
        #     wd = self.app.wd
        #     wd.find_element_by_name("firstname").click()
        #     wd.find_element_by_name("firstname").clear()
        #     wd.find_element_by_name("firstname").send_keys(contact.firstname)
        #     wd.find_element_by_name("middlename").click()
        #     wd.find_element_by_name("middlename").clear()
        #     wd.find_element_by_name("middlename").send_keys(contact.middlename)
        #     wd.find_element_by_name("lastname").click()
        #     wd.find_element_by_name("lastname").clear()
        #     wd.find_element_by_name("lastname").send_keys(contact.lastname)
        #     wd.find_element_by_name("nickname").click()
        #     wd.find_element_by_name("nickname").send_keys(contact.nickname)
        #     wd.find_element_by_name("company").click()
        #     wd.find_element_by_name("company").clear()
        #     wd.find_element_by_name("company").send_keys(contact.Company)
        #     wd.find_element_by_name("title").click()
        #     wd.find_element_by_name("title").clear()
        #     wd.find_element_by_name("title").send_keys(contact.title)
        #     wd.find_element_by_name("address").click()
        #     wd.find_element_by_name("address").clear()
        #     wd.find_element_by_name("address").send_keys(contact.address)
        #     wd.find_element_by_name("mobile").click()
        #     wd.find_element_by_name("mobile").clear()
        #     wd.find_element_by_name("mobile").send_keys(contact.mobile)
        #     wd.find_element_by_name("home").click()
        #     wd.find_element_by_name("home").clear()
        #     wd.find_element_by_name("home").send_keys(contact.homephone)
        #     wd.find_element_by_name("email").click()
        #     wd.find_element_by_name("email").clear()
        #     wd.find_element_by_name("email").send_keys(contact.mail)
        # self.select_xpa()
        #     wd.find_element_by_name("bmonth").click()
        #     Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmouth)
        #     wd.find_element_by_name("byear").click()
        #     wd.find_element_by_name("byear").clear()
        #     wd.find_element_by_name("byear").send_keys(contact.byear)

    def select_xpa(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)







