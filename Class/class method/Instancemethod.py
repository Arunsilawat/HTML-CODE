
class Student:
    city="Bhopal"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def display(self):
        print("hellow This is Display instance method")
    def show(self):
        print("name= ",self.name)
        print("roll= ",self.roll) 
        print("City= ",Student.city) 
        self.display()          #self ki help se hi call hoga function
obj=Student("Arun",101)
obj.show()
obj.display()