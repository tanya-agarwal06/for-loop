#1
'''for i in range(1,10):
    print(input("enter any number"))
    print(i)'''

#2
'''x="true"
while(x=="true"):
    print("loop is infinite")'''

#3
'''l=[]
a=int(input("enter the input value"))
b=int(input("enter the input value"))
l.append(a)
l.append(b)
for i in l:
    print(i**2)'''

#4
'''l=[]
j=[]
k=[]
for a in range(10):
    a=input("enter integer and strings")
if isinstance(a,int):
    l.append(a)
    print(l)
elif isinstance(a,str):
    j.append(a)
    print(j)
elif isinstance(a,float):
    k.append(a)
    print(k)'''


#5
'''even=[]
odd=[]
for i in range(0,101):
    if i %2==0:
        even.append(i)
    else:
        odd.append(i)
print("number is even",even)
print("number is odd",odd)'''

#6
'''for i in range(0,4):
    for i in range(0,i+1):
        print("*",end=" ")
    print()'''

#7
'''dictionary = {"name":"tanya","age":"19"}
for i in dictionary:
    dictionary.get(i)
    print(i)'''

#8
l=[]
for i in range(0,5):
    num=int(input("enter number"))
    l.append(num)
print(l)
l2=[]
a=int(input("enter value"))
x=l.index(2)
x=l.remmove(2)
print(l)