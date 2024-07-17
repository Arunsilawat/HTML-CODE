# create 
# open
# read write
# close   ,data strore karne ke liye  crud opreation ke liye
# CRUD-->1. create 2.delete 3.update 4.read
#mode 4 categitre hote he a,w,x,r,=>file 3 cetegire ki hoti he .txt, .binary, .csv
# f=open('newpy2.txt','a')   #new file create hogi #dobara run karne par ->FileExistsError:File exists
# f=open('newpy1.txt','w')   #new file create hogi
# f=open('newpy1.txt','x')   #new file create hogi
# f=open('newpy2.txt','r')   #new file create nhi hogi
# print(f.read())

f=open('n1.txt','x')
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)
print(f.writable())