class Person:
    def __init__(self,fname,lname):
        self.firstnam=fname
        self.lastname=lname
    def printname(self):
        print(self.firstnam,self.lastname)

x=Person("John","Doe")
x.printname()   