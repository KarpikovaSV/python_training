import pymysql.connections
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            #cursor.execute("select id, firstname, lastname, middlename, nickname, Company, title, address, homephone, email, bday, bmonth, byear, address2, notes, mobilephone, workphone, secondaryphone, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            cursor.execute("select id, firstname, lastname, middlename, nickname, company, title, address, home, mobile, work, email, bday, bmonth, byear, notes, email2, email3, address2 from addressbook where deprecated='0000-00-00 00:00:00'")

            for row in cursor:
                (id, firstname, lastname, middlename, nickname, Company, title, address, home, mobile, work, email, bday, bmonth, byear, notes, email2, email3, address2) = row
                #( secondaryphone,) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename, nickname=nickname, Company=Company, title=title, address=address, homephone=home, mobilephone=mobile, workphone=work, email=email, bday=bday, bmonth=bmonth, byear=byear, notes=notes, email2=email2, email3=email3, address2=address2))
        finally:
            cursor.close()
        return list
