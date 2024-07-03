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

# my_list1=input("Enter Name")
# v,c=0,0
# for i in my_list1:
#     if i=='a' or i=='i' or i=='o' or i=='u' or i=='e':
#         v=v+1
#     else:
#         c=c+1
# print(v)
# print(c)
#----------------------------------------------------------------------
# n=int(input("Enter NUmber :"))
# i=1
# sum=0
# while i<=n:
#     sum=sum+i
#       if i<=n-1:
#         print(i,end=",")
#       else:
#         print(i)
#       i=i+1
#---------------------------------------------
#-------sum --------------
# n=int(input("Enter NUmber :"))
# i=1
# sum=0
# while i<=n:
#       sum=sum+i
#       if i<=n-1:
#         print(i,end="+")
#       else:
#         print(i,end="=")
#       i=i+1
# print(sum)

#-------------------------------------------------------------------
n=int (input("Enter no."))
i=1
sum=0
while i<=n:
     if i==n:
         print(i,end="=")
     else:
         print(i,end="+")
         sum=sum+i
     i=i+1
print(sum)
# ==============Even No================

n=int (input("Enter no."))
i=1
sum=0
while i<=n:
     if i%2==0:
         print(i,end=",") 
     i=i+1
# ============ Factorial =================
n=int (input("Enter no."))
i=1
multi=1
while i<=n:
     multi=multi*i
     if i<n:
         print(i,end="=") 
     else:
         print(i,end="x")
         
     i=i+1
print(multi)

n=int (input("Enter no."))
i=1
multi=1
while i<=n:
     multi=multi*n
     if i<n:
         print(n,end="=") 
     else:
         print(n,end="x")
         
     n=n-1
print(multi)