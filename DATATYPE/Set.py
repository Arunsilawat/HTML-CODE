
my_set={10,20,30,"Arun",40,10,50}  #---duplicate not allow , bar bar value badlega,
print(my_set)                       #--- indexing not allow sliceing not alluw
                                     #-->mutable 
print(len(my_set))
# print(max(my_set))
# print(min(my_set))
my_set.add("Rahul")              #----> single object add krna 
print(my_set)

my_set1=[66,77,88,88,99,00]
my_set.update(my_set1)           #----->multi object add karega duplicate value nhi aayegi
print(my_set)

my_set.remove(77)
print(my_set)

my_set.discard(9987)            #-----> value nhi hone par bhi error nhi dega 
print(my_set)


s1={10,20,30}
s2={40,20,60}

s3=s1.intersection(s2)   #same value nhi hogi to set() dikhega   comman
print(s3)

s4=s1.union(s2)       #add krta hai
print(s4)

s5=s2.difference(s1)  #diffrence
print(s5)