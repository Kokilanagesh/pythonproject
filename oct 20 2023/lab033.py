#palindrome checker
string1=input("Enter string name:")
string2=(string1[::-1]) # [::-1] this is slicing method to reverse the string
print(string1)
print("reversed string:",string2)
if(string1 == string2):
    print("The string is palindrome.")
else:
     print("The string is not a palindrome.")

                # or
def palindrome():
    if name==rev:
        print("This is palindrome")
    else:
        print("This is not a palindrome")
name=input("please enter the string name:")
rev=name[::-1] #reverse the string
print(rev)
palindrome() #function calling



