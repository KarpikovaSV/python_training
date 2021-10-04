# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
from aplication import Aplication
from contact import Contact

@pytest.fixture
def ap(request):
    fixture = Aplication()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(ap):
    ap.login(username="admin", password="secret")
    ap.add_contact(Contact(firstname="Svetlana3", middlename="khsdks", lastname="KKKKKK", nickname="Nick", Company="Compa", titlen="Title", address="Add", mobile="+75656567676",
                         homephone="+76565656767", mail="gdesveta@noya.ru", bday="26", bmouth="August", byear="1990", address2="addr", notes="hkda", phone2="khad"))
    ap.logout()

