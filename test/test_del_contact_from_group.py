from model.contact import Contact
from model.group import Group
from random import randrange


def test_del_contact_from_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(header="jnjhn", name="bjbjjhh", footer="nm"))
        #app.group.create(Group(name="test"))
    groups = db.get_group_list()
    index_g = randrange(len(groups))
    group = groups[index_g]
    contacts_in_group = db.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        if app.contact.count() == 0:
            app.contact.add(
                Contact(firstname="Svetlana", middlename="Editkh", lastname="ghhjhjygy", nickname="1234567gxs",
                        Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobilephone="+75656567600",
                        homephone="+71265656767", email="editeditgdesveta@noya.ru", bday="15", bmonth="August",
                        byear="1990", address2="addr", notes="hkda", secondaryphone="khad"))
        contacts = app.contact.get_contact_list()
        index_c = randrange(len(contacts))
        contact = contacts[index_c]
        app.contact.add_contact_by_id_to_group(contact.id, group.id)
        contacts_in_group.append(contact)
    index_c = randrange(len(contacts_in_group))
    contact = contacts_in_group[index_c]
    app.contact.del_contact_by_id_in_group(contact.id, group.id)
    new_contacts = db.get_contacts_in_group(group)
    assert len(contacts_in_group) - 1 == len(new_contacts)
    contacts_in_group.remove(contact)
    assert contacts_in_group == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                           key=Contact.id_or_max)