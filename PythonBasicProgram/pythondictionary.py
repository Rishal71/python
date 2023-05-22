dict={
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964  
}
print(dict)

print("")

dict={
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964  
}
x=dict["model"]
print(x)

print("")

thisdict={
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 2002
}
thisdict["year"]=2018
print(thisdict)

print("")

thisdict={
    "brand" : "ford",
    "model" : "mustang",
    "year" : 2004
}
for x in thisdict:
    print(x)

print("")

dict={
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964  
}
for x in dict:
    print(dict[x])

print("")

for x in dict.values():
    print(x)