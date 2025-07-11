### Error Handling ###

seats = {"A1": None, "A2": None, "A3": None}


def display_menu():
    print("\nEnter 1 to add a person")
    print("Enter 2 to remove a person")
    print("Enter 3 to view all seats")
    print("Enter 0 to exit")


def get_user_data():
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
        return {
            "name": name,
            "age": age,
            "phone": phone
        }


while True:
    try:
        display_menu()
        cmd = int(input("Enter a command: "))

        if cmd == 1:
            user = get_user_data()
            seat_found = False
            for k, v in seats.items():
                if v is None:
                    seats[k] = user
                    print(f"{user['name']} assigned to seat {k}")
                    seat_found = True
                    break
            if not seat_found:
                print("All seats are full.")

        elif cmd == 2:
            seat = input("Enter the seat you want to remove a user from (e.g., A1): ").strip().upper()
            if seat in seats:
                if seats[seat] is not None:
                    removed_name = seats[seat]['name']
                    seats[seat] = None
                    print(f"Removed {removed_name} from seat {seat}.")
                else:
                    print(f"Seat {seat} is already empty.")
            else:
                print("Invalid seat number.")

        elif cmd == 3:
            print("\n--- Seat Status ---")
            for seat, person in seats.items():
                if person:
                    print(f"Seat {seat}: Name: {person['name']}, Age: {person['age']}, Phone: {person['phone']}")
                else:
                    print(f"Seat {seat}: Empty")

        elif cmd == 0:
            print("Exiting program.")
            break

        else:
            print("Invalid command. Please enter 0, 1, 2, or 3.")

    except ValueError:
        print("Please enter a valid number for the command.")
    except:
        print(f"An unexpected error occurred")












