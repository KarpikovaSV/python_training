from model.contact import Contact
from random import randrange


def test_add_contact_in_group(app, db, json_contacts, json_groups, check_ui):
    if app.group.count() == 0:
        group = json_groups
        db.create(group)
    groups = db.get_group_list()
    index_g = randrange(len(groups))
    group = groups[index_g]
    contacts_not_in_group = db.get_contacts_not_in_group(group)
    if len(contacts_not_in_group) == 0:
        contact = json_contacts
        app.contact.add(contact)
        contacts_not_in_group.append(contact)
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