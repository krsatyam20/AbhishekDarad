x=[1,2,3,4,5]

print(x[0])


print(x[:])
print(x[:3])
print(x[2:3])
print(x[2])

#add in list

x[0]=10


print(x[0])

#delete in list
del(x[0])
print(x[0])
print("List",x[:])

#opretor


print(x*2)

y=[10,20,11.2]
#concatnation
z=(x+y)

print(z)

print(max(z))

print(min(z))

print(len(z))


#append in list
l=[]
n=int(input("Please enter the no. of element"))
for i in range(0,n):
    l.append(input("please enter the value"))

#print List

for x in l:
    print(x)

del(l[0])

print("After remove")


for x in l:
    print(x)


#add of list value 
sum=0
for x in l:
    sum=sum+x


print("Total of list",sum)    














