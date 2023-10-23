# Continue
# need to be more careful with spacings
for num in range(1,10):
    if num % 2 == 0:
        print(f"Found even Number {num}") # here "f" means the value of num value will be displayed
        continue
    print(f"odd number found {num}")

              #or
# we can use without "f" both are same
for num in range(1,10):
    if num % 2 == 0:
        print("Found even Number", num)
        continue
    print(f"odd number found ",num)
