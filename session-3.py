# name = input("Enter your name: ")
# print("Hi " + name)
# age = int(input("Enter your age: "))
#
# if age >= 18:
#     birth_year = 2025 - int(age)
#     print("You were born in " + str(birth_year))
# else:
#     print("You are to young to use the system.")

# name = input("Enter your name: ")
# print("Hi " + name)
# marks = int(input("Enter your marks: "))
#
# if marks >= 75:
#     print("Grade: A")
# elif marks >= 65:
#     print("Grade: B")
# elif marks >= 55:
#     print("Grade: C")
# elif marks >= 35:
#     print("Grade: S")
# else:
#     print("Grade: F")

# num = int(input("Enter a number: "))
# if num >= 0 and num <= 100:
#     print("Number is in range 0 to 100")
# else:
#     print("Number is not in range 0 to 100")

# balance = 5000
#
# print("Welcome to Python Banking!")
# print("Enter 1 if you want to Withdraw.")
# print("Enter 2 if you want to Deposit.")
#
# cmd = int(input("Choose a option: "))
# if cmd == 1:
#     amount = int(input("Enter withdrawal amount: "))
#     if balance >= amount:
#         balance -= amount
#         print("You have withdrawed LKR " + str(amount))
#     else:
#         print("Insufficient funds")
# elif cmd == 2:
#     amount = int(input("Enter deposit amount: "))
#     balance += amount
#     print("You have deposited LKR " + str(amount))
# else:
#     print("Invalid command")
#
# print("Account balance: LKR " + str(balance))


### LOOPS ###

# for i in range(10):
#     print("Kevin", i)

# print( list(range(10)) )

num = int(input("Enter a number: "))
while num <= 10:
    print("Number is " + str(num))
    num = int(input("Enter a number: "))












