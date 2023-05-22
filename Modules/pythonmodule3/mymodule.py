def greeting(name):
    print("Hello,"+name)

person1={
    "name":"John",
    "Age":36,
    "Country":"Norway"
}

from mymodule import person1

print(person1["name"])
