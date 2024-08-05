class P1:
    def display(self):
        print("P1 class")
class C1(P1):
    def show(self):
        print("C1 class")
        
        P1.display(self)
obj=C1()
obj.display()
obj.show()