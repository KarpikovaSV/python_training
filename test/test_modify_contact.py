from model.contact import Contact
from random import randrange


def test_modify_contact_name(app):
    if app.contact.count_contact() == 0:
        app.contact.add(Contact(firstname="Svetlana", middlename="Editkh", lastname="ghhjhjygy", nickname="1234567gxs",
                                Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobilephone="+75656567600",
                                homephone="+70065656767", email="editeditgdesveta@noya.ru", bday="15", bmonth="August",
                                byear="1990", address2="addr", notes="hkda", secondaryphone="khad"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New 57558658Svettt")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
#   contact.lastname = old_contacts[0].lastname
    old_contacts[index].firstname = contact.firstname
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_title(app):
#    if app.contact.count_contact() == 0:
#        app.contact.add(Contact(firstname="Svetlana", middlename="Editkh", lastname="hbjbjb", nickname="1234567gxs",
#                                  Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobile="+75656567600",
#                                  homephone="+70065656767", mail="editeditgdesveta@noya.ru", bday="15", bmonth="August",
#                                  byear="1990", address2="addr", notes="hkda", phone2="khad"))
#    app.contact.modify_first_contact(Contact(title="New title"))


#def test_eddit_contact(app):
#    if app.contact.count_contact() == 0:
#        app.contact.add(Contact(firstname="EditSvetlana", middlename="Editkhsdks", lastname="", nickname="1234567gxs",
#                Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobile="+75656567600",
#                homephone="+70065656767", mail="editeditgdesveta@noya.ru", bday="15", bmonth="August", byear="1990", address2="addr", notes="hkda", phone2="khad"))
#    app.contact.modify_first_contact(Contact(firstname="EditSvetlana3", middlename="Editkhsdks", lastname="", nickname="1234567gxs", Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobile="+75656567600",
#                            homephone="+70065656767", mail="editeditgdesveta@noya.ru", bday="15", bmonth="August", byear="1990", address2="addr", notes="hkda", phone2="khad"))
