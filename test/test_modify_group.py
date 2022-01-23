from model.group import Group
from random import randrange
import random


def test_modify_group_name(app, db, json_groups, check_ui):
    if app.group.count() == 0:
        group = json_groups
        db.create(group)
        #app.group.create(header="jnjhn", name="bjbjjhh", footer="nm")
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    old_group = old_groups[index]
    group = Group(name="New group")
    group.id = old_group.id
    app.group.modify_group_by_id(old_group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(header="jnjhn", name="bjbjjhh", footer="nm")
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_headerr(app):
#    if app.group.count() == 0:
#        app.group.create(header="jnjhn", name="bjbjjhh", footer="nm")
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="jnjhn", name="bjbjjhh", footer="nm"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)