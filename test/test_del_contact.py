from model.contact import Contact
import time
from random import randrange


def test_del_contact(app, json_contacts):
    if app.contact.count_contact() == 0:
        contact = json_contacts
        app.contact.add(contact)
        # app.contact.add(Contact(firstname="Svetlana", middlename="Editkh", lastname="", nickname="1234567gxs",
        #                         Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobilephone="+75656567600",
        #                         homephone="+71165656767", workphone="+71165656767", email="editeditgdesveta@noya.ru", bday="15", bmonth="August",
        #                         byear="1990", address2="addr", notes="hkda", secondaryphone="644646466"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    time.sleep(1)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
