#create a program
#take 5 numbers from the users
#add 1-2 duplicates
#print the non duplicate numbers
print("Enter 5 NUmbers, Please Enter atleast two duplicates")
num1=int(input("Enter the 1st Number:"))
num2=int(input("Enter the 2nd Number:"))
num3=int(input("Enter the 3rd Number:"))
num4=int(input("Enter the 4th Number:"))
num5=int(input("Enter the 5th Number:"))
list= [num1,num2,num3,num4,num5]
print("Data entered by users in List: ",list)
NonDuplist = set(list)
print("Non Duplicate list created after removing duplicate elements: ",NonDuplist)
