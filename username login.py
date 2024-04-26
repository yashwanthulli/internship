user_name = "yashwanth"
user_password = 1234

name = input("Enter your name: ")

if name == user_name:
    for i in range(3):  # Loop for three attempts
        password = int(input("Enter your password: "))
        if password == user_password:
            print("Welcome!")
            break
        else:
            print("Incorrect password.")
            print("Attempts remaining:", 2 - i)
    else:
        print("All attempts used. Please try again later.")
else:
    print("User not found.")
