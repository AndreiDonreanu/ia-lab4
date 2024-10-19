
class Customer:

    member=None
    member_type=None

    def __init__(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def is_member(self):
        return self.member


    def set_member(self,member):
        self.member = member

    def set_member_type(self,member_type):
        self.member_type=member_type

    def get_member_type(self):
        return self.member_type

    def  __str__(self):
        return "Nume:"+self.name+" membru:%s"%self.member+" tip:"+self.member_type