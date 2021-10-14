from model.group import Group


def test_eddit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.eddit_first_group(Group(header="edt4", name="edt6", footer="edt8"))
