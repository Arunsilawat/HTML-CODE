def outer_fun(fun):
    def inner_fun(x,y):
        x=x+10
        y=y+10
        return fun(x,y)
    return inner_fun
@outer_fun
def main_fun(x,y):
    return x+y
#decorater ke bina code......
# var1=outer_fun(main_fun)
# var2=var1(5,5)
# print(var2)
x=main_fun(5,5)
print(x)