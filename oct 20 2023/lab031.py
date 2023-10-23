# Match
# similar to switch in java
# condition based is not possible in match statment
name = input("Enter a name\n")
match name:
    case "kokila":
        print("hello kokila")
    case "nagesh":
        print("hello nagesh")
    case _:
        print("who are you")
