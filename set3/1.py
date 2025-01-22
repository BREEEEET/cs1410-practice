# Inputs

username = input("Enter your username: ")

is_alnum = username.isalnum()

length = len(username)

 

is_valid = False

# Nested If/Else

if not username:
    print("Username cannot be empty.")

elif not is_alnum:
    print("Username must be alphanumeric.")

elif not length >= 6:
    print("Username is too short.")
elif not length <= 12:

    print("Username is too long.")


else:
    print("Username is valid.")



