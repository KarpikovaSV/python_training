from model.contact import Contact


def test_eddit_contact(app):
    app.contact.eddit_contact(Contact(firstname="EditSvetlana3", middlename="Editkhsdks", lastname="", nickname="1234567gxs", Company="Compa56", titlen="Titlehsjah", address="EditAddshgdsb", mobile="+75656567600",
                            homephone="+70065656767", mail="editeditgdesveta@noya.ru", bday="15", bmouth="August", byear="1990", address2="addr", notes="hkda", phone2="khad"))
    app.open_home_page()