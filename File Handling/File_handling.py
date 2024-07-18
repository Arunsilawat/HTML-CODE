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

# f=open('n1.txt','x')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed


#---------------x mode-------------------
f=open('n1.txt','x')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)
#---------------x+ mode -----------------

f=open('n2.txt','x+')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)

#==========================w mode ===========================
f=open('n3.txt','w')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)
#------------------ w+ mode ----------------------
f=open('n4.txt','w+')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)
#======================== r mode ======================
f=open('n4.txt','r')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)
#--------------------- r+ mode -----------------

f=open('n4.txt','r+')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)
#========================== a mode ===================
f=open('n7.txt','a')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)
#----------------------a+ mode --------------------
f=open('n8.txt','a+')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)
