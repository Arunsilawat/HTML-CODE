

class A:
    def display(self):
        print("This is from A")
class B(A):
    def display(self):
        print("This is from B")
    def show(self):
        super().display()
obj=B()
obj.display()
obj.show()