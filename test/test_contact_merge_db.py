import re
from model.contact import Contact


def test_phones_address_email_on_home_page_and_db(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for i in range(len(contacts_from_home_page)):
        contact_from_home_page = contacts_from_home_page[i]
        contact_from_db = contacts_from_db[i]
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname
        assert contact_from_home_page.address == contact_from_db.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phone_like_on_home_page(contact_from_db)
        assert contact_from_home_page.mails == merge_mail_like_on_home_page(contact_from_db)


def merge_phone_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_mail_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))


def clear(s):
    return re.sub("[() -]", "", s)
