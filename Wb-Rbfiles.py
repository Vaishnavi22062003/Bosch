f1=open("Stackroute01.jpg","rb")

f2=open("stackroute02.jpg","wb")
data=f1.read()
f2.write(data)
print("Newimage is :stackroute.jpg")