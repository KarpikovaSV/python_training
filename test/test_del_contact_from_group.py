from model.contact import Contact
from random import randrange


def test_del_contact_from_group(app, db, json_contacts, json_groups, check_ui):
    if app.group.count() == 0:
        group = json_groups
        db.create(group)
    groups = db.get_group_list()
    index_g = randrange(len(groups))
    group = groups[index_g]
    contacts_in_group = db.get_contacts_in_group(group)
    if len(contacts_in_group) == 0:
        if app.contact.count() == 0:
            contact = json_contacts
            app.contact.add(contact)
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