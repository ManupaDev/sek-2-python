# age = int(input("Enter your age: "))

# nums = [2,3,5,7]
#
# print(nums[6])

# try:
#     age = int(input("Enter your age: "))
#     nums = [2,3,5,7]
#     print(nums[1])
#     print(5/0)
# except ValueError as e:
#     print("Invalid input: ", e)
# except IndexError as e:
#     print("Invalid index used in a list: ", e)
# except Exception as e:
#     print("Some error happend: ", e)

# seats = {"A1": None, "A2":None, "A3":None }
#
# def display_menu():
#     print("Enter 1 to add a person")
#     print("Enter 2 to remove a person")
#     print("Enter 3 to view all seats")
#     print("Enter 0 to exit")
#
# def get_user_data():
#     try:
#         name = input("Enter your name: ").strip()
#         age = int(input("Enter your age: ").strip())
#         phone = input("Enter your phone: ").strip()
#         if not (phone.isdigit() and len(phone) <= 10):
#             raise ValueError("Invalid phone number")
#         return {
#             "name": name,
#             "age": age,
#             "phone": phone
#         }
#     except ValueError as e:
#         print("Invalid input: ", e)
#
# while True:
#     try:
#         display_menu()
#         cmd = int(input("Enter a command: "))
#
#         if cmd == 1:
#             user = get_user_data()
#             seat_found = False
#             for k, v in seats.items():
#                 if v is None:
#                     seats[k] = user
#                     print(f"{user['name']} assigned to seat {k}")
#                     seat_found = True
#                     break
#             if not seat_found:
#                 print("All seats are full.")
#
#         elif cmd == 2:
#             seat = input("Enter the seat you want to remove a user from (e.g., A1): ").strip().upper()
#             if seat in seats:
#                 if seats[seat] is not None:
#                     seats[seat] = None
#                 else:
#                     print(f"Seat {seat} is already empty.")
#             else:
#                 print("Invalid seat number.")
#
#         elif cmd == 3:
#             for seat, person in seats.items():
#                 if seats.get(seat):
#                     print(f"Seat {seat}: Name:{person['name']}, Age:{person['age']} Phone:{person['phone']} ")
#         elif cmd == 0:
#             print("Thank you for using our system")
#             break
#
#         else:
#             print("Invalid command")
#
#     except ValueError:
#         print("Please enter a valid number for the command.")
#
#     except Exception as e:
#         print(f"An unexpected error occured {e}")

# class Person():
#     def __init__(self, name, age, phone):
#         self.name = name
#         self.age = age
#         self.phone = phone
#
#     def greet(self):
#         print(f"My name is {self.name}")
#
# manupa = Person("manupa", 24, "0702703440")

class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Phone: {self.phone}"

class SeatManager():
    def __init__(self):
        self.seats = {"A1": None, "A2": None, "A3": None}

    def display_menu(self):
        print("\nEnter 1 to add a person")
        print("Enter 2 to remove a person")
        print("Enter 3 to view all seats")
        print("Enter 0 to exit")

    def get_user_data(self):
        while True:
            name = input("Enter your name: ").strip()
            try:
                age = int(input("Enter your age: "))
            except ValueError:
                print("Invalid input. Age must be a number.")
                continue
            phone = input("Enter your phone: ").strip()
            if not phone.isdigit() or len(phone) < 7:
                print("Invalid phone number. Please enter digits only (min 7 digits).")
                continue
            return Person(name, age, phone)

    def add_person(self):
        user = self.get_user_data()
        for seat, person in self.seats.items():
            if person is None:
                self.seats[seat] = user
                print(f"{user.name} assigned to seat {seat}")
                return
        print("All seats are full.")

    def remove_person(self):
        seat = input("Enter the seat you want to remove a user from (e.g., A1): ").strip().upper()
        if seat in self.seats:
            if self.seats[seat] is not None:
                removed_name = self.seats[seat].name
                self.seats[seat] = None
                print(f"Removed {removed_name} from seat {seat}.")
            else:
                print(f"Seat {seat} is already empty.")
        else:
            print("Invalid seat number.")

    def view_seats(self):
        print("\n--- Seat Status ---")
        for seat, person in self.seats.items():
            if person:
                print(f"Seat {seat}: {person}")
            else:
                print(f"Seat {seat}: Empty")


manager = SeatManager()
while True:
    try:
        manager.display_menu()
        cmd = int(input("Enter a command: "))
        if cmd == 1:
            manager.add_person()
        elif cmd == 2:
            manager.remove_person()
        elif cmd == 3:
            manager.view_seats()
        elif cmd == 0:
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please enter 0, 1, 2, or 3.")
    except ValueError:
        print("Please enter a valid number for the command.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")





















