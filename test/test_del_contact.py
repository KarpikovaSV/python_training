

def test_del_contact(app):
    app.contact.delete_first_contact()
    app.open_home_page()
