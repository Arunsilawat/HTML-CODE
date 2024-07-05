# n=input("Enter Value :")
# m=n[ : :-1]
# if n==m:
#     print("Palindrom")
# else:
#     print("Not Palindrom")

# -----------------------------------------------------------------
# n=int(input("Enter Value :"))
# digit,x=0,n
# while n>0:
#     rev=n%10
#     digit=digit*10+rev
#     n=n//10
# print(digit)
# print(n)
# print(x)
# if x==digit:
#     print("Palindrom")
# else:
#     print("Not a Palindrom")
#--------------------------------------------------------------------
#-----------partten
n=int(input("How many row requird"))
i=1
while i<=n:
    print(i*'*'+(n-i)*(' '))
    i=i+1
#-----------------reverse ----------------------
n=int(input("How many row requird"))
i=1
while i<=n:
    print((n-i)*(' ')+i*'*')
    i=i+1

#------------------piramid --------------------
n=int(input("How many row requird"))
i=1
while i<=n:
    print((n-i)*(' ')+i*' *')
    i=i+1
#--------------odd even piramid --------------
n=int(input("How many row requird"))
i=1
while i<=n:
    print((n-i)*(' ')+(2*i-1)*'*')
    i=i+1