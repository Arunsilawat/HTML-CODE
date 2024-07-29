class Student:
    x=10
    y=20
    def __init__(self):
        print("this is from Constructor")
        print(id(self))
    @staticmethod                             #
    def display():
        print("This is from Display")
obj=Student()
print(id(obj))
print(obj.x)
obj.display()
obj1=Student()
print(id(obj1))