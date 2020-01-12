x=(10,20,30)

print(x)
print(x[0])

for i in x:
    print(i)

#'tuple' object does not support item assignment(Modify)
'''x[0]=20
for i in x:
    print(i)
'''

print("Max=%d Min= %d" %(max(x),min(x)))

x=10
y=20
z=x+y

print("Add Value of %d and %d= %d" %(x,y,z))

y="kumar"

print("Name= %s" %(y))

#list

x=[10,20]

print(x)

x[0]=30


print(x)


'''WAP to show the list of students in institute and prefix techvision'''
student_name = ["Abhishek", "Satyam", "Vimlesh", "Mamta", "Raman", "Monika"]
print (student_name)

for i in student_name:
    print(i)

student_name[0]="Abhi"
print (student_name)


'''WAP to show the list of students in institute and prefix techvision'''
student_name = ("Abhishek", "Satyam", "Vimlesh", "Mamta", "Raman", "Monika")
print (student_name)

for i in student_name:
    print(i)

student_name[0]="Abhi"
print (student_name)
