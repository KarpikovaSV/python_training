from model.group import Group


def test_eddit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.eddit_first_group(Group(header="edt", name="edt", footer="edt"))
    app.session.logout()
