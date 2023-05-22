class Grandfather:
    grandfathername=""
    def grandfather(self):
        print(self.grandfathername)


class Father(Grandfather):
    fathername=""
    def father(self):
        print(self.father)


class Son(Father):
    def parent(self):
        print("Grandfather:",self.grandfathername)
        print("Father:",self.fathername)

s1=Son()
s1.grandfathername="srinivas"
s1.fathername="ankush"
s1.parent()