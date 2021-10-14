from model.contact import Contact


def test_eddit_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.add(Contact(firstname="EditSvetlana", middlename="Editkhsdks", lastname="", nickname="1234567gxs",
                Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobile="+75656567600",
                homephone="+70065656767", mail="editeditgdesveta@noya.ru", bday="15", bmonth="August", byear="1990", address2="addr", notes="hkda", phone2="khad"))
    app.contact.eddit_contact(Contact(firstname="EditSvetlana3", middlename="Editkhsdks", lastname="", nickname="1234567gxs", Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobile="+75656567600",
                            homephone="+70065656767", mail="editeditgdesveta@noya.ru", bday="15", bmonth="August", byear="1990", address2="addr", notes="hkda", phone2="khad"))