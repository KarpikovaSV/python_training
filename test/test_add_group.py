# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(header="jnjhn", name="bjbjjhh", footer="nm"))
    app.session.logout()
    time.sleep(3)


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(header="", name="", footer=""))
    app.session.logout()
    time.sleep(3)
