list = [1,3,5,8]
print(dir(list))
#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# Map and filter in the list

sq = lambda x: x*x
result = sq(5)
print(result)

# Map function( where we will go from one item and apply a functions)
numbers=[1,2,3,4,5]
sq_numbers = []
for i in numbers:
    sq_numbers.append(sq(i))
print(sq_numbers)

#new
def triple(a):
    return a * 3

# Map function
sq_number1 = list(map(lambda x: x * 3,numbers))
sq_number1 = list(map(triple,numbers))
print(sq_number1)
print(sq_number2)


