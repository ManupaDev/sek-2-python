### Functions ###
# A description of a program(set of instructions).
import math

def greet():
    print("Hey! Good Evening")
    name = input("Please enter your name ?: ")
    print("Welcome, " + name)

greet()

# def raise_power(a, b):
#     print(a ** b)
#
#
# raise_power(2, 3)


# def raise_power(a, b):
#     c = a ** b
#     return c
#
#
# value = raise_power(2, 3)
# print(value)

# def greet():
#     print("Hey! Good Evening")
#     name = input("Please enter your name ?: ")
#     return "Welcome, " + name
#
#
# greeting_message = greet()
# print(greeting_message)


# def f1():
#     s = "I like to eat ice cream"
#
#     def f2():
#         print(s)
#
#     f2()
#
#
# f1()


def use_atm():
    balance = 5000
    print("Welcome to Python Banking!")
    name = input("Enter your name: ")
    print("Hello, "+ name)

    print("Enter 1 if you want to Withdraw.")
    print("Enter 2 if you want to Deposit.")

    def withdraw(balance, amount):
        if balance >= amount:
            # balance -= amount
            balance = balance - amount
            return balance
            print("You have withdrawed LKR " + str(amount))
        else:
            print("Insufficient funds")

    def deposit(balance, amount):
        balance = balance + amount
        return balance
        # balance += amount
        print("You have deposited LKR " + str(amount))

    cmd = int(input("Choose a option: "))
    if cmd == 1:
        amount = int(input("Enter withdrawal amount: "))
        balance = withdraw(balance, amount)
        # withdraw(balance, amount)
    elif cmd == 2:
        amount = int(input("Enter deposit amount: "))
        balance = deposit(balance, amount)
        # deposit(balance, amount)
    else:
        print("Invalid command")

    print("Account balance: LKR " + str(balance))


use_atm()

# def print_num():
#     x = 5
#     print(x)
#
# print_num()

# x = 2

# def calculate():
#     x = 5
#     def print_num():
#         x = 7
#         print(x)
#
#     print_num()
#
# calculate()


