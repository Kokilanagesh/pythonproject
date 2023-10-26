# check list is empty
list =[]
if not list:
    print("Empty")
else:
    print("not empty")

####
squares = [1,4,9,16,25,1] # here 4 is in index number 1 so in output its removes the 4 value in the  list
print(squares.pop(1)) # pop will remove the index value
print(squares)
print(squares.remove(1)) #it removes the value not the index
print(squares)

