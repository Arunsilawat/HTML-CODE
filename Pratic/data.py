# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def div(x,y):
#     return x/y
# def multi(x,y):
#     return x*y
# while True:
#     print('Select You Choice')
#     n=int(input("add-1,sub-2,div-3,multi-4,exit-5 : "))
#     p=int(input("Enter First num : "))
#     q=int(input("Enter Second num : "))
#     if n==1:
#         print(p,"+",q,"= ",add(p,q))
#     elif n==2:
#         print(p,"-",q,"= ",sub(p,q))
#     elif n==3:
#         print(p,"/",q,"= ",div(p,q))
#     elif n==4:
#         print(p,"*",q,"= ",multi(p,q))
#     elif n==5:
#         break
#     else:
#         print("Invalid Number")
# -------------------------------------------------------------------------------------------------------------
 # def sum(*n):
#     total=0
#     for i in n:
#         total=total+i 
#     print(total)
# sum()
# sum(10)
# sum(20,10,20)
#
 ------------------------------------------------
# def fact(num):
#     result=1
#     while num>1:
#         result=result*num
#         num=num-1
#     return result
# i=int(input("Enter Number : "))
# print("Fact of num ",i,"= ",fact(i))
# 
---------------------------------------------
# def even_odd(num):
#     if num%2==0:
#         print("Even Num")
#     else:
#         print("Odd num")
# x=int(input("Enter Num :"))
# even_odd(x)
# ---------------------------------------------
# 
n=int(input("Enter Number : "))
# m=n 
# rev=0
# while m>0:
#     r=m%10
#     rev=(rev*10)+r
#     m=m//10
# if rev==n:
#     print("Palindrom") 
# else:
#     print("Not a Palindrom")
# ---------------------------------------------------