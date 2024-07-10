
# scope -->global scope
# local scope
# variable-->1- global 2->local

x=10
def show():
    x=20
    return x
y=show()
print("value of inner x",y)
print("value of outer x",x)

#-----------------------------------------------------------
#global keyword use karke variable global ho jayega
x=10
def show():
    global x
    x=20
    return x
y=show()
print("value of inner x",y)
print("value of outer x",x)

#------------------------------------------------------------
# function ke andar global variable ka access lena 
# same name ke variable he to globals("variable name")

x=10
def show():
    x=20
    print(globals()["x"])
show()