mystr="I am from bhopal"
mystr1="I Am from Bhopal"
mystr2="i am from bhopal I AM ARUN SILAWAT"
# mystr[0]="Arun"
# print(mystr)
p="python"
n=3
o=p*n 
print(o)

print(mystr.upper())
print(mystr1.upper())
print(mystr2.swapcase())
print(mystr2.title())
a="ARUN"
b=a.center(20,'*')
b=a.center(20,'=')
print(b)

# aa=["Arun","From","Bhopal"]
# bb=["You","Are","My","Friend"]
aa="Arun"
bb="You1432"
print(aa)
print('='.join(aa))
cc='_'
print(cc.join(aa))
print(aa.join(bb))

x="Bhopal"
y="abc123"
print(x.join(y))

st="Python is a programing language"
print(st.split(":",0))


na=[12,44,34,65]
print(na)
na.append(90)
na.append("Arun")
na.append([23,43,55,"Ritu"])
print(na)

ca=[2,3,4,23,4,4,4,2]
print(ca.count(2))

list1=[1,2,34,4]
list2=[3,4,32,2]
list1.extend(list2)
print(list1)
set1={23,45,65,76}
tuple1=(3,77,65,5)
list1.extend(set1)
print(list1)
list2.extend(tuple1)
print(list2)
list2.reverse()
print(list2)
list2.pop()
print(list2)
list2.insert(2,111)
print(list2)

num=[7,54,33,2,1]
num.sort()
print(num)
num.sort(reverse=True)
print(num)


x={10,20,30,40,40}
y={30,40,50,60}
print(x.union(y))
