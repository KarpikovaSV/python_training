from model.contact import Contact
from model.group import Group
from random import randrange


def test_add_contact_in_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(header="jnjhn", name="bjbjjhh", footer="nm"))
    groups = db.get_group_list()
    index_g = randrange(len(groups))
    group = groups[index_g]
    contacts_not_in_group = db.get_contacts_not_in_group(group)
    if len(contacts_not_in_group) == 0:
        contact = Contact(firstname="Svetlana", middlename="Editkh", lastname="ghhjhjygy", nickname="1234567gxs",
                    Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobilephone="+75656567600",
                    homephone="+71265656767", email="editeditgdesveta@noya.ru", bday="15", bmonth="August",
                    byear="1990", address2="addr", notes="hkda", secondaryphone="khad")
        app.contact.add(contact)
        contacts_not_in_group = db.get_contacts_not_in_group(group)
    index_c = randrange(len(contacts_not_in_group))
    contact = contacts_not_in_group[index_c]
    old_contacts = db.get_contacts_in_group(group)
    old_contacts.append(contact)
    app.contact.add_contact_by_id_to_group(contact.id, group.id)
    new_contacts = db.get_contacts_in_group(group)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)