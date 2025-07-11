### DICTIONARIES ###

seats = {"A1": None, "A2":None, "A3":None }

def display_menu():
    print("Enter 1 to add a person")
    print("Enter 2 to remove a person")
    print("Enter 3 to view all seats")

def get_user_data():
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))
    phone = input("Enter your phone: ").strip()
    return {
        "name":name,
        "age":age,
        "phone":phone
    }

while True:
    display_menu()
    cmd = int(input("Enter a command: "))
    if cmd == 1:
        user = get_user_data()
        seat_found = False
        for k, v in seats.items():
            if v is None:
                seats[k] = user
                seat_found = True
                break
        if not seat_found:
            print("All seats are full")
    elif cmd == 2:
        seat = input("Enter the seat you want to remove a user from (e.g., A1): ").strip().upper()
        if seat in seats:
            if seats[seat] is not None:
                seats[seat] = None
            else:
                print(f"Seat {seat} is already empty.")
        else:
            print("Invalid seat number.")
    elif cmd == 3:
        for seat,person in seats.items():
            if seats.get(seat):
                print(f"Seat {seat}: Name:{person['name']}, Age:{person['age']} Phone:{person['phone']} ")



























# manupa_name = "Manupa"
# manupa_age = 25
# manupa_phone = "0702703440"
#
# manupa = {
#     "age": 25,
#     "name": "Manupa",
#     "phone": "0702703440"
# }

# print(manupa)
# del manupa["phone"]
# print(manupa)
#
# for k, v in manupa.items():
#     print(k)
#     print(v)

# print("age" in manupa)

# manupa.update("age")

# name = "Manupa"
# print(name[:3])

# stored_name = "Manupa"
# name = input("Enter your name: ")
#
# if name.strip().lower() == stored_name.lower():
#     print("Yes")

# name = "Manupa"
# print(name.strip(), end=",")
# print(name, end=",")

# print("K" in name)

# print("My name is "+ manupa["name"], " and my age is " + str(manupa["age"]))

# phrase = f"My name is {manupa['name']} and my age is {manupa['age']}"
# print(phrase)
