# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="EditSvetlana3", middlename="Editkhsdks", lastname="", nickname="1234567gxs",
                      Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobilephone="+75656567600",
                      homephone="+71065656767", workphone="+70065656767", mail="editeditgdesveta@noya.ru", bday="15", bmonth="August", byear="1990", address2="addr", notes="hkda", secondaryphone="556565665")
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
