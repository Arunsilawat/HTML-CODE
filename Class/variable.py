# Instance Variable declare throough constractor
class Student:
    def __init__(self,name,age):  #constractor ke variables ko instance variable bolenge
        self.n1=name
        self.n2=age
    def display(self):
        print("Name : ",self.n1)
        print("Age :",self.n2)
obj=Student("Arun",24)
obj.display()
obj1=Student("Rohan",22)
obj1.display()
print(obj.n1)
print(obj.n2)

# Instance Variable declare throough object
class Student1:         
    def display(self):
        print("Name : ",self.n1)
        print("Age :",self.n2)
obj=Student1()
# obj.display()  #function ko bad me call karna he value dene ke bad
obj.n1="Arun"
obj.n2=24
obj.display()

# Instance Variable declare throough method
class Student2:
    def display(self,name,age):
        self.n1=name
        self.n2=age
    def show(self):
        print("Name : ",self.n1)
        print("Age :",self.n2)
obj=Student2()
obj.display("Arun Silawat",20)
obj.show()
print(obj.n1,obj.n2)

#Access instance variable
#1) Within the class --> through self
#2) Outside the class --> through object