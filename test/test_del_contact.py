from model.contact import Contact
import time


def test_del_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add(Contact(firstname="Svetlana", middlename="Editkh", lastname="", nickname="1234567gxs",
                                 Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobile="+75656567600",
                                 homephone="+70065656767", mail="editeditgdesveta@noya.ru", bday="15", bmonth="August",
                                 byear="1990", address2="addr", notes="hkda", phone2="khad"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    time.sleep(1)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
