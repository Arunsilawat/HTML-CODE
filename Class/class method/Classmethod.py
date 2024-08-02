class Book:
    price=1000
    self detail(self,author_name,author_city):
        print("Name : ",author_name)
        print("City : ",author_city)
        print("Price : ",Book.price)
    @classmethod
    def update_price(cls,update_price):
        cls.price=update_price
obj=Book()
obj.detail("Arun","Bhopal")
obj.update_price(1500)
obj.detail("Arun","Bhopal")