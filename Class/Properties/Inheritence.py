# class P1:
#     def display(self):
#         print("P1 class")
# class C1(P1):
#     def show(self):
#         print("C1 class")
        
#         P1.display(self)
# obj=C1()
# obj.display()
# obj.show() 
#------------------single lavel------------------------
# class P:
#     city="Bhopal"
#     def display(self):
#         print("This is from Display")
# class C(P):
#     def show(self):
#         print("This is from Show")
#         print("City :",P.city)
# obj=C()
# obj.show()
# print(obj.city,obj.display())

#------------------multi lavel------------------------
class P:
    city="Bhopal"
    def display(self):
        print("This is from Display")
class C(P):
    def show(self):
        print("This is from Show")
        print("City :",P.city)
class C1(C):
    city1=P.city
    def show1(self):
        (self.display())
        (self.show())
obj=C1()
print(obj.city1)
obj.show1()
obj.show()
obj.display()
