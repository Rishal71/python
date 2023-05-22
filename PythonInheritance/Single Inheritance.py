class Parent:
    def func1(self):
        print("This function is in Parent class.")


class Child(Parent):
    def func2(self):
        print("This function is in child class>")


object=Child()
object.func1()
object.func2()