#ASSIGNMENT 1


#PROGRAM 1

a=input('Enter Your Number Here: ')
print(a)
b=input('Enter Your Number Here: ')
print(b)
c=input('Enter Your Number Here: ')
print(c)
a=int(a)
b=int(b)
c=int(c)
print('Your Average Is' , (a+b+c)/3)

#PROGRAM 2

a=float(input('Enter Your Gross Income: '))
print(a)
b=float(input('How Many Dependants Do You Have: '))
print(b)
c=float(b*3000)
print('Deduction For Dpendants', c)
d=float(a-10000-c)
print('Taxable Income: ', d)
e=float((a*1)/5)
print('Tax You Would Have To Pay: ', e)

#PROGRAM 3

a=int(input('State Your SID: \n'))
b=str(input('State Your NAME: \n'))
print('NOTE : gender should be one of the following \n \tM//F//U')
c=str(input('State Your Gender: \n'))
d=str(input('State Your Course Name: \n'))
e=float(input('State Your CGPA: \n'))

f=[a,b,c,d,e]
print(f)

#PROGRAM 4

m1=int(input('First Student Marks: \n'))
m2=int(input('Second Student Marks: \n'))
m3=int(input('Third Student Marks: \n'))
m4=int(input('Fourth Student Marks: \n'))
m5=int(input('Fifth Student Marks: \n'))
a=[m1,m2,m3,m4,m5]
a.sort()
print(a)

#PROGRAM 5(A)

a=['Red','Green','White','Black','Pink','Yellow']
a.remove('Black')
print(a)

#PROGRAM 5(B)

a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a[3:5]=[ 'Purple']
print(a)
