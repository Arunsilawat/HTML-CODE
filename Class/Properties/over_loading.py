class A:
    def add(x=0,y=0):
        return x+y
    def add(x=0,y=0,z=0):  #last bali method hi chalegi
        return x+y+z
obj=A 
x=obj.add(4,3)
print(x)