#leap year checker

year=int(input("enter the year:"))
if( year % 4 == 0 and year % 100 !=0):
    print("Its leap year")
elif(year %400 ==0):
    print("Its leap year")
else:
    print("Its not leap year")
