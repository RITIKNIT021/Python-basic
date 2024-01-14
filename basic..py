from math import *
print("hellow")
a=int(input())
b=int(input())
s=a+b
print("sum is:"+str(s))
name="Ritik pal"
print(name.find('p'))
print(name.replace("pal","kumar"))
print('R' in name)
print(2>6 or 0!=0)
print(not 8>5)
if s>=10:
    print("yes")
elif s>6 and s<10:
    print("no")
else:
    print("thanks")

i=1
while i<=a:
    print(i*"*")
    i+=1

marks=[8,5,6,4,10]
print(marks[-4])
print(marks[0:4])
marks.append(11)
print(marks)
marks.insert(2,12)
print(marks)
print(len(marks))
print(marks.pop(3))
marks.clear()
print(marks)
marks=(3,4,5,6,6,6,6)
print(marks.count(6))
print(marks.index(5))
marks={5,7,8,8}
print(marks)
marks={"a":5,"b":3,"c":5}
print(marks["b"])
print(sqrt(9))

def sum(x,y):
    print(x+y)

sum(4,7)
x=lambda a:a+12
print(x(9))
l=[1,6,8,32.55,"strin","ritki","data"]
l1=[]
l2=[]
for i in l:
    if type(i)==int or type(i)==float:
        l1.append(i)
    else:
        l2.append(i)

print(l1)
print(l2)