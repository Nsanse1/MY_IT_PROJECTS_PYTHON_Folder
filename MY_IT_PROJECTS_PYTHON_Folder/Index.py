# Name = "Nsanse"
# print(Name)

# decimal = 3.142
# print(decimal)

# boolean = True
# print(boolean)


# integer = 42
# print(integer)


# Num1 = 100
# Num2 = 60

# sum = Num1 == Num2

# print(sum)

# Lists

# students_name = ["Nsanse", "Osim", "Enyieko"]
# print(students_name[2])


# courses = ("Math", "Biology", "English")
# print(courses)

# Sets

# students_lastname = {"Nsanse", "Osim","Enyieko"}
# print(len(students_lastname))

# Dictionary

# car = {
#     "color": "Red",
#     "Model": "Toyota",
#     "Year": 2020
# }

# # print(car["model"])
# print(car)


# DAY 3
# Using if statement

# age = 18

# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")



# score = 40

# if score >= 70:
#     print("Grade: A")
# elif score >= 60:
#     print("Grade: B")
# elif score >= 50:
#     print("Grade: C")
# elif score >= 45:
#     print("Grade: D")
# elif score >= 40:
#     print("Grade: E")
# elif score <= 40:
#     print("Grade: F")



#   Loops

# list = ["Apple", "Banana", "Mango", "Orange", "Watermelon", "Cashew"]
# for list in["Apple", "Banana", "Mango", "Orange", "Watermelon", "Cashew"]:
#     print(list)


# students = ["Paschal", "Agema", "Amake", "Esin", "Tilda", "Cherry"]
# for students in["Paschal", "Agema", "Amake", "Esin", "Tilda", "Cherry"]:
#     print(students)


# count = 0 
# while count < 5:
#     print("count is", count)
#     count += 1


# corrtect_password = "123456789"
# attempt = 0

# while attempt < 5:
#     password = input("Enter Password: ")
#     print("Login Successful")
#     break
# else:
#     print("Wrong Password")
#     attempt += 1

# if attempt == 5:
#     print("Account Blocked: Too many attempts")



# DAY 4 - Function
# def send_email():
#     print("Hello Nsanse, We are having a class tommorrow")

# send_email()


def send_welcome_email(user):
    print("Hello,", user + " Welcome To your Dashboard")

send_welcome_email("Nsanse")
send_welcome_email("Kisha")
send_welcome_email("Amake")
send_welcome_email("Agema")
