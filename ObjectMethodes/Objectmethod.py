class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hello my name is "+self.name)
        print("Hello my age is "+str(self.age))
p1 = Person("john",36)
p1.myfunc()      