#-----1->position arguments----------
# add(2,3)
def add(x,y):
    return x-y
x=add(20,10)
print(x)

# default aruments--------------
def add(x=0,y=0,z=0):
    return x-y-z
x=add()
x=add(10)
x=add(50,10)
print(x)
# keyword aruments--------------
def add(x=0,y=0,z=0):
    return x+y+z
x=add()
x=add(10)
x=add(z=10,x=30,y=20)
print(x)
# variable lenth aruments  (* **key word)--------------
# * aruments--------------
def add(*n):
    print(n)
    sum=0
    for i in n:
        sum=sum+i
    return sum
x=add(5)
print(x)
y=add(5,6,7,8)
print(y)
# ** kw aruments--------------
