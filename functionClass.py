#no arguments no return function in python

#create/define a function
def msg():
    print("Hello")

'''
here def: is pre define keyword
     msg: User define keyword
     print: pre define function/command which is used for print any thisngs

'''


#use/call a function

msg()

msg()

msg()


#With arguments no return function in python

#create/define a function

def add(a,b):

    c=a+b # addition and store on c 
    print("Add Value of a and b = ",c)



add(10,20)

add(14,30)
#get value from user and use function

x=int(input("Please enter the first value"))
y=int(input("Please enter the second value"))

add(x,y)



#With arguments with return function in python

#create/define a function

def multiply(a,b):
    c=a*b
    return c

z=multiply(10,2)
print(z+2)
    

#NO arguments with return function in python

def greeting():
    return 'Good Moring'


print("Hello Abhi",greeting())


















