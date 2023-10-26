#list of squares
#squares = [1,4,9,16,25]
#my_list = [True,"kokila",12,34,90]
#my_list.sort() # TypeError: '<' not supported between instances of 'str' and 'bool'
#print(my_list)

squares = [1,4,9,16,25]
l= squares
l1 = squares.copy()
print(squares)
print(l)
print(l1)

squares[0]=33
print(squares)
print(l)
print(l1)

