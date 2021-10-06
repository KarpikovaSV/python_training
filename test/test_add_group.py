# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(header="jnjhn", name="bjbjjhh", footer="nm"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(header="", name="", footer=""))
    app.session.logout()


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(firstname="Svetlana3", middlename="khsdks", lastname="KKKKKK", nickname="Nick", Company="Compa", titlen="Title", address="Add", mobile="+75656567676",
                            homephone="+76565656767", mail="gdesveta@noya.ru", bday="26", bmouth="August", byear="1990", address2="addr", notes="hkda", phone2="khad"))
    app.session.logout()
