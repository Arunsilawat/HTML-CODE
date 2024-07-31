#value change nhi hogi
class Student:
    school='HSS Tulsipar'
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        Student.centercode=101
    def display(self):
        Student.great='10th'
        print("Name : ",self.name)
        print("Roll No :",self.roll)
        print("School Name :",Student.school)
        print("Center Code",Student.centercode)
        print("Great :",Student.great)
 

obj=Student("Arun",1001)
obj.display()
print("Class Name se :",Student.school)
print("Object Se :",obj.school)
obj1=Student("Ritu",1009)
obj1.display()
  
print("--------------------------------------------------------------------------------------------------------")
class Employee:
    Company="SS Creation"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Employee.Company_Code=101
    def display(self):
        Employee.Company_Project="E-Commarce"
        print("Company Name : ",Employee.Company)
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Company Code : ",Employee.Company_Code)
        print("Company Project : ",Employee.Company_Project)
        print("City : ",Employee.city)
obj=Employee("Arun",24)

Employee.city="Bhopal"
obj.display()
print("--------------------------------------------------------------------------------------------------------")