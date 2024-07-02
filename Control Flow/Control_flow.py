#1Sequantial  --> line by line
#2->Condition --> if if else,if elif,if elif elif.
#3->transfar  --> Comtinuew,pass,breack
#4->iteretive --> for,while
#-------------------if--------------------------
# n=int(input("Enter your age"))
# if n>=18:print("You are eligible")
# print("Thank you for visit")

#------------------if else -----------------------
# n=int(input("Enter your age"))
# if n>=18:
#     print("You are eligible")
# else:
#     print("You are not eligible")
# print("Thank you for visit")
#----------------- Iteretive ---------------------
# for----> list Tuple(()) dict() set() string() frozonset()
# x=range(-1,-11,-2)
# x=range(-2,-10,-2)
# x=range(10)
# print(x)
# print(list(x))
# print(tuple(x))
# print(set(x))
#-------------------------even no squer--------------------------------
# my_list=[]
# for i in range(2,11,2):
#     x=i**2
#     my_list.append(x)
# print(my_list)

my_list1=input("Enter Name")
v,c=0,0
for i in my_list1:
    if i=='a' or i=='i' or i=='o' or i=='u' or i=='e':
        v=v+1
    else:
        c=c+1
print(v)
print(c)
    