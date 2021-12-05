from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="Svetlana", middlename="Editkh", lastname="gvjgvjg", nickname="1234567gxs",
                                Company="Compa56", title="Titlehsjah", address="EditAddshgdsb", mobilephone="+75656567600",
                                homephone="+71165656767", workphone="+71165656767", email="editeditgdesveta@noya.ru",
                                email2="editeditgdesveta@noya.ru", email3="editeditgdesveta@noya.ru",
                                bday="15", bmonth="August",
                                byear="1990", address2="addr", notes="hkda", secondaryphone="644646466")
]

# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def random_tel(maxlen):
#     symbols = string.digits
#     return "+" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# def random_email(maxlen):
#     symbols = string.ascii_letters + string.digits
#     symbols1 = string.ascii_letters
#     return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + "".join([random.choice(symbols1) for i in range(5)]) + ".com"
#
#
# def random_bday():
#     return str(random.randrange(1, 28))
#
#
# testdata = [
#     Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
#             lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
#             Company=random_string("Company", 20), title=random_string("title", 20),
#             address=random_string("address", 20), mobilephone=random_tel(11),
#             homephone=random_tel(11), workphone=random_tel(11),
#             email=random_email(10),
#             email2=random_email(10),
#             email3=random_email(10),
#             bday=random_bday(), bmonth="August", byear="1990",
#             address2=random_string("address2", 20), notes=random_string("notes", 20),
#             secondaryphone=random_tel(11))
# ]
#
# #for i in range(2)