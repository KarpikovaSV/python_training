from model.contact import Contact
import time
from random import randrange


def test_del_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add(Contact(firstname="Svetlana", middlename="Editkh", lastname="", nickname="1234567gxs",
                                Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobilephone="+75656567600",
                                homephone="+70065656767", mail="editeditgdesveta@noya.ru", bday="15", bmonth="August",
                                byear="1990", address2="addr", notes="hkda", secondaryphone="khad"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    time.sleep(1)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
