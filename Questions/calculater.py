def add(x,y):
    return x+y 
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
def multi(x,y):
    return x*y
while True:
    print("plz select options")
    print("1-add,2-sub,3-div,4-multi,5-off")
    a=int(input("Enter Choice"))
    b=int(input("finst num"))
    c=int(input("sec num"))
    if a==1:
        print(b,"+",c,"=",add(b,c))
    elif a==2:
        print(b,"-",c,"=",sub(b,c))
    elif a==3:
        print(b,"/",c,"=",div(b,c))
    elif a==4:
        print(b,"*",c,"=",multi(b,c))
    elif a==5:
        break
    else:
        print("invalid syntax")