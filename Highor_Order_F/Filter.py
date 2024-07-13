
#-----------------------find vovel ---------------------
my_str=input("Enter Name")
def vovel(n):
    my_vovel=['a','e','i','o','u','e','A','I','O','U','E']
    if n in my_vovel:
        return True
print(list(filter(vovel,my_str)))

# ---------------------- consonenet ------------------------object in ,not in // object==object same find karne ke liye is ,is not
my_str=input("Enter Name")
def vovel(n):
    my_vovel=['a','e','i','o','u','e','A','I','O','U','E']
    if n not in my_vovel:
        return True
print(list(filter(vovel,my_str)))