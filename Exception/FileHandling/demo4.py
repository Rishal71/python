f=open("demofile3.txt","w")
f.write("Woops! i have deleted the content")
f.close()

f=open("demofile3.txt","r")

print(f.read()) 