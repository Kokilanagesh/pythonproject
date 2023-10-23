# using lambda in palindrome
original_str = "Gopal"
reverse_str = lambda original_str: original_str[::-1]
if reverse_str("Gopal") == original_str:
    print("palindrome")
else:
    print("not a palindrome")
