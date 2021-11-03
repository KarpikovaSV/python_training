# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_tel(maxlen):
    symbols = string.digits
    return "+" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    symbols1 = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + "".join([random.choice(symbols1) for i in range(5)]) + ".com"


def random_bday():
    return str(random.randrange(1, 28))


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            Company=random_string("Company", 20), title=random_string("title", 20),
            address=random_string("address", 20), mobilephone=random_tel(11),
            homephone=random_tel(11), workphone=random_tel(11),
            email=random_email(10),
            email2=random_email(10),
            email3=random_email(10),
            bday=random_bday(), bmonth="August", byear="1990",
            address2=random_string("address2", 20), notes=random_string("notes", 20),
            secondaryphone=random_tel(11))
for i in range(2)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
