#string
#bunch of char
name = "kokila gopal"
 #string functions
 #python immutable in nature - they can't changed. once created
# Once the content is created it cannot be changed in strings, its reference can be changed but content cannot be changed.

#capitalize()
#returns a copy of string with its first character capitalized.
result = name.capitalize()
print(result)
print(name)

print(id(name))
print(id(result))# identity is kind of ref to address


#uppercase
result1=name.upper()
print(result1)
print(name)

#lowercase
result2=name.lower()
print(result2)
print(name)

#swapcase()
# Returns a copy of the string with uppercase characters to lowercase and vice versa

name = "kOkIlA gOpAl"
print(name.swapcase())

# Title
# Returns a titlecased version of the string,
# Where words start with uppercase character and the remaining characters are lowercase

text= "Hello world"
print(text.title())

# Replace
#text="hello world"
#result_rep = text.replace(__old:"world",__new:"python")
#print(result_rep)

#Index and length
name="kokila"
#len-->starts from 1 in length no of spaces is also counted
print(len(name))
#Index-->starts from 0 to len -1
# here k-0,o-1,k-2,i-3,l-4,a-5.

# Find
# Find basically returns the lowest index of substring form
# Returns -1 if the substring is not found.

text="hello world"
index=text.find("world")
print(index)

#Count is counting the character
count=text.count("l")
print(count)

name = "K N"
print (len(name))


name="kokila"
print(name)
del name
print(name)







