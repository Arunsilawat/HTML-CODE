

my_dict={"name":"Arun","city":"Bhopal"}  #key--->uniqe 
print(my_dict['city'])
print(id(my_dict))
my_dict1=dict()
print(my_dict1)
print(type(my_dict1))

my_dict["name"]="Rohan"
print(my_dict)

my_dict['quali']='M-tech'
print(my_dict)
print(id(my_dict))

del my_dict['city']    #----->delete
print(my_dict)
# print(my_dict['city'])
# print(my_dict.clear())


print(len(my_dict))
print(max(my_dict))
print(min(my_dict))
my_dict[1]="Indore"
print(my_dict)
# print(max(my_dict))
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get('4','Arun'))  #get------>defoult value set karte hai
print(my_dict)
my_dict.pop('name')
print(my_dict)