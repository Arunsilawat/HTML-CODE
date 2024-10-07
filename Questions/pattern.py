n=int(input("row :"))
for i in range(1,n+1):
    print("* "*i)

n=int(input("row :"))
for i in range(1,n+1):
    print(" "*(n-i),"*"*i)

n=int(input("row :"))
for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i-1))

n=int(input("row :"))
for i in range(1,n+1):
    print(" "*(n-i),"* "*( i))

n=int(input("row :"))
for i in range(n,0,-1):
    print(" "*(n-i),"*"*(i))

n=int(input("row :"))
for i in range(n,0,-1):
    print(" "*(n-i)," *"*(i))

n=int(input("row :"))
for i in range(n,0,-1):
    print("*"*(i))

n=int(input("row :"))
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)

for i in range(n,0,-1):
    print(" "*(n-i),"* "*i)


n=int(input("row :"))
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)