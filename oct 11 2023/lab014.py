#task 6
score=int(input("enter the score:"))
if(score<35):
    print("Poor student")
if(score>35 & score<70):
    print("Average student")
if(score>70):
    print("Good student")

      #or
score=int(input("enter the score:"))
if(score<35):
    print("Poor student")
elif(score>35 & score<70):
    print("Average student")
elif(score>70 & score< 100):
    print("Good student")
else:
    print("invalid input")



