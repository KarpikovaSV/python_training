from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, Company=None, title=None, address=None, mobile=None, homephone=None,
                    mail=None, bday=None, bmonth=None, byear=None, address2=None, notes=None, phone2=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.Company = Company
        self.title = title
        self.address = address
        self.mobile = mobile
        self.homephone = homephone
        self.mail = mail
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.address2 = address2
        self.notes = notes
        self.phone2 = phone2
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or self.firstname is None or self.id == other.id or self.lastname is None) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
