# List
# list is nothing but items or list of arrays

my_list = [1,2,3,]
my_list1 = [1, True, "kokila",28.7]
print("inital list:",my_list)

#Indexing
print("Element at index 0:",my_list[0])

# Changing an element
my_list[1] = 20
print("list after changing element at index 1:",my_list)

# append basically means adding in the end
my_list.append(4)
print("list after appending:",my_list)

#extend its also adding with list
my_list.extend([5,6])
print("list after extending:",my_list)

#insert()
my_list.insert(1,'a')
print("list after inserting 'a' at index 1:",my_list)

#remove() it removes the value not the index
my_list.remove('a')
print("list after removing 'a':",my_list)

#copy()
my_copy_list=my_list.copy()
print(my_copy_list)

#clear()
my_list.clear()
print("Intial list:",my_list)

#sort()
my_copy_list.sort()
print(my_copy_list)

#reverse
my_copy_list.reverse()
print(my_copy_list)

