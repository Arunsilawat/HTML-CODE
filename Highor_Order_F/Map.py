#map() -->number or input == no of output-->colection return aayega

my_list=[1,2,3,4,5]
def squer(n):
    return n**2
new_list=list(map(squer,my_list))
print(new_list)