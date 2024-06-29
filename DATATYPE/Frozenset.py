import sys
my_list=[2,3,4,3,2,67,9,90,"Arun",530]
my_tuple=(4,3,2,4,78,9,7,5,"Ritu",570)
my_set={5,4,3,2,8,97,6,5,4,90}
my_dict={'name':"ARUN",'age':23,'quali':"BSC"}

a=frozenset(my_list)
b=frozenset(my_tuple)
print(frozenset(my_list))   #friz ho gya
print(frozenset(my_tuple))
print(frozenset(my_set))
print(frozenset(my_dict))

print(max(my_set))
print(min(my_set))
print(sum(my_set))
print(len(my_set))

s=a.union(b)
print(s)
s1=a.intersection(b)
print(s1)
s2=a.difference(b)
print(s2)

lsize=sys.getsizeof(my_list)
tsize=sys.getsizeof(my_tuple)
ssize=sys.getsizeof(my_set)
dsize=sys.getsizeof(my_dict)

print(lsize)
print(tsize)
print(ssize)
print(dsize)