import os
os.system('color A')
a=dict()
limit=int(input("how many value you want enter"))
for i in range(0,limit):
    key=input("enter you input \n")
    value=input("Enter you value \n")
    a[key]=value

#print(a)
access=input()
print(a.get(access))
print("\n Updat value")
updat, v=input().split()
a[updat]=v
print(a)
b=dict()
l=int(input("how many value you want enter"))
for i in range(0,l):
    
    
    k=input("enter you input \n")
    va=input("Enter you value \n")
    b[k]=va
    b.update(a)
print(b)
#delet()
#item=input()
d= b.pop(input())
print(b)
name=input() in a 
print(name)
#keys()
ke=b.keys()
print(ke)
vl=b.values()
print(vl)




