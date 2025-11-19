# try:
#     number = int(input("Enter a number:"))
#     result = 10 / number
#     print("Result: ", result)

# except ZeroDivisionError:
#     print("You cannot divide by zero!")

# except ValueError:
#     print("Please enter a valid number.")


users = {"covenant": "1234"}
try:
    username = input("Enter Username: ")
    password = input("Enter password: ")

    if users[username] == password:
        print("Login Succeefull")
    else:
        print("Wrong Password")

except KeyError:
    print("Username not found")
    
