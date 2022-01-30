from model.contact import Contact
from random import randrange


def test_modify_contact_name(app, db, check_ui):
    if app.contact.count_contact() == 0:
        #contact = json_contacts
        #app.contact.add(contact)
        app.contact.add(Contact(firstname="Svetlana", middlename="Editkh", lastname="ghhjhjygy", nickname="1234567gxs",
                                Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobilephone="+75656567600",
                                homephone="+71265656767", email="editeditgdesveta@noya.ru", bday="15", bmonth="August",
                                byear="1990", address2="addr", notes="hkda", secondaryphone="khad"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    #index = 1
    old_contact = old_contacts[index]
    contact = Contact(firstname="New 57558658Svettt")
    contact.id = old_contact.id
    app.contact.modify_contact_by_id(old_contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    contact.lastname = old_contact.lastname
    #old_contacts[index].firstname = contact.firstname
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)