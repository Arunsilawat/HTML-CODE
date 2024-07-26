def gen():
    i=1
    my_list=[]
    while i<=10:
        my_list.append(i)
        i=i+1
    return my_list
var1=gen()
print(var1)
#--------------------generator---------------------
def gen():
    i=1
    my_list=[]
    while i<=10:
        my_list.append(i)
        i=i+1
    yield my_list
var1=gen()
# print(var1)
print(next(var1))


#--
def gen():
    i=1
    my_list=[]
    while i<=10:
        my_list.append(i)
        i=i+1
    yield my_list
var1=gen()
# print(var1)
# print(next(var1))
for i in var1:
    print(i)

#------------------single object nikalna -------------
def gen_no(x,y):
    while x<=y:
        yield x
        x=x+1
var1=gen_no(1,10)
print(next(var1))
print("Welcome 1")
print(next(var1))
print("Welcome 2")
print(next(var1))
print("Welcome 3")
print(next(var1))
print("Welcome 4")
print(next(var1))
print("Welcome 5")