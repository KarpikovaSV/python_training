from model.contact import Contact
import time
import random
from random import randrange


def test_del_contact(app, db, check_ui):
    if app.contact.count_contact() == 0:
        app.contact.add(Contact(firstname="Svetlana", middlename="Editkh", lastname="", nickname="1234567gxs",
                                Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobilephone="+75656567600",
                                homephone="+71165656767", workphone="+71165656767", email="editeditgdesveta@noya.ru", bday="15", bmonth="August",
                                byear="1990", address2="addr", notes="hkda", secondaryphone="644646466"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    #index = randrange(len(old_contacts))
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    time.sleep(1)
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(contact)
    #old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

