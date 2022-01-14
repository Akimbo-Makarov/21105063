print('ASSIGNMENT 1 \n')


print('PROGRAM 1 \n')

a=input('Enter Your Number Here: ')
print(a)
b=input('Enter Your Number Here: ')
print(b)
c=input('Enter Your Number Here: ')
print(c)
a=int(a)
b=int(b)
c=int(c)
print('Your Average Is \n' , (a+b+c)/3)


print('PROGRAM 2 \n')

a=float(input('Enter Your Gross Income: '))
print(a)
b=float(input('How Many Dependants Do You Have: '))
print(b)
c=float(b*3000)
print('Deduction For Dpendants', c)
d=float(a-10000-c)
print('Taxable Income: ', d)
e=float((a*1)/5)
print('Tax You Would Have To Pay: \n', e)

print('PROGRAM 3 \n')

a=int(input('State Your SID: \n'))
b=str(input('State Your NAME: \n'))
print('NOTE : gender should be one of the following \n \tM//F//U')
c=str(input('State Your Gender: \n'))
d=str(input('State Your Course Name: \n'))
e=float(input('State Your CGPA: \n'))

f=[a,b,c,d,e]
print(f)
print('. \n')

print('PROGRAM 4 \n')

m1=int(input('First Student Marks: \n'))
m2=int(input('Second Student Marks: \n'))
m3=int(input('Third Student Marks: \n'))
m4=int(input('Fourth Student Marks: \n'))
m5=int(input('Fifth Student Marks: \n'))
a=[m1,m2,m3,m4,m5]
a.sort()
print(a)
print('. \n')

print('PROGRAM 5(A) \n')

a=['Red','Green','White','Black','Pink','Yellow']
a.remove('Black')
print(a)
print('. \n')
print('PROGRAM 5(B) \n')

a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a[3:5]=[ 'Purple']
print(a)
