my_dic={"arun",12,12,44,"Ritu"}
# print(type(my_dic))
# print(type(set(my_dic)))
my_dic={11,22,333,44,}
# print(my_dic)
print(type(frozenset(my_dic)))
print(type(set(my_dic)))

mydata={12,4,5,44,0}
mydata1=[]
print(bool(mydata))
print(bool(mydata1))


bit=[22,33,44]
x=bytes(bit)
print(x)
print(type(x))

#------------------------------------------------------------------------
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mylist.index(4))
print(mylist.index(10))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 7
print(list.index(6, 4, 6))
