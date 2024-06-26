
my_list=[10,50,30,"abc123","abc","abc",10]

print(my_list)
print(my_list[3])
my_list[0]="Arun"
print(my_list)
print(my_list[0:6:2])
print(my_list.index(30))
#----------------------Inbuild function------------------------
#len(),max(),min(),some(),list()-->typecasting ke 
print(len(my_list))
#----------------------Inbuild Method------------------------
my_list.append('50')  #append()---->last me object ko add karna
print(my_list)

my_list1=[3,43,23]    #extend()--->do list ko ek karne ke liye
my_list.extend(my_list1)
print(my_list)

my_list.pop()         #pop()---->last bala object ko hatane ke liye
print(my_list)

my_list.remove('abc') #remove()---->jo object doge bo hatega 
print(my_list)

my_list.insert(5,900) #insert(index_no,object)-->object ko index par add karna
print(my_list)

a=[22,33,433,443,45,4343]
a.sort()          #soet--------->asenting order me karega
print(a)
a.sort(reverse=True)  #-------->reverse bhi sath me karega
print(a)
# ---------------------------------------------------------------------------------------------------
c=[12,2,3,4,5]
d=[6,5,4,33,2]
c.append(d)
print(c)

c.extend(d)
print(c)