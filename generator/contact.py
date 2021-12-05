from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numbers of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_tel(maxlen):
    symbols = string.digits
    return "+" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    symbols1 = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + "".join([random.choice(symbols1) for i in range(5)]) + ".com"


def random_bday():
    return str(random.randrange(1, 28))


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            Company=random_string("Company", 20), title=random_string("title", 20),
            address=random_string("address", 20), mobilephone=random_tel(11),
            homephone=random_tel(11), workphone=random_tel(11),
            email=random_email(10),
            email2=random_email(10),
            email3=random_email(10),
            bday=random_bday(), bmonth="August", byear="1990",
            address2=random_string("address2", 20), notes=random_string("notes", 20),
            secondaryphone=random_tel(11))
            # for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))