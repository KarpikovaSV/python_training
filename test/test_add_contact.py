# -*- coding: utf-8 -*-
from model.contact import Contact
import time


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(firstname="Svetlana3", middlename="khsdks", lastname="KKKKKK", nickname="Nick", Company="Compa", titlen="Title", address="Add", mobile="+75656567676",
                            homephone="+76565656767", mail="gdesveta@noya.ru", bday="26", bmouth="August", byear="1990", address2="addr", notes="hkda", phone2="khad"))
    app.session.logout()
    time.sleep(3)
