dict={
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964  
}
for x,y in dict.items():
    print(x,y)

print("")

dict={
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964  
}
dict["color"]="red"
print(dict)

print("")

dict={
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964  
}
dict.pop("model")
print(dict)

print("")

dict={
    "brand" : "ford",
    "model" : "mustang",
    "year"  : 1964  
}
dict.clear()
print(dict)