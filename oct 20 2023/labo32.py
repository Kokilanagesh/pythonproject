# Functions
# functions are reusable set of operations
#functions are the backbone of python

output = max(1,3) # built in function
print(output)

#block of code
# 1. Built in - which are created by python guys
# for u so that u can use them without creating your own
# 2. custom function - u cna create a fun which is a block of code,anyone can use

a=int(input("enter a\n"))
b=int(input("enter b\n"))
print(a+b)

# written some code
#reuseable code
#def is a keyword
def sum(a,b):
    return a+b
a=int(input("enter a\n"))
b=int(input("enter b\n"))
print(sum(a,b))

print(sum(34,45))

# new
def sayhello()
    print("Hi")

sayhello()
