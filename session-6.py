### DICTIONARIES ###

def display_menu():
    print("\n===== Seat Manager =====")
    print("1. Add a person")
    print("2. Remove a person")
    print("3. Show all seats")
    print("4. Quit")

MAX_SEAT_COUNT = 5
seats = []

while True:
    display_menu()
    try:
        cmd = int(input("Enter a command (1-4): ").strip())
    except ValueError:
        print("Please enter a valid number.")
        continue

    if cmd == 1:
        if len(seats) >= MAX_SEAT_COUNT:
            print("Seats are full, cannot add more people.")
            continue

        name = input("Enter person name: ").strip()
        age_input = input("Enter age: ").strip()
        phone = input("Enter phone number: ").strip()

        if not age_input.isdigit():
            print("Age must be a number.")
            continue

        person = {
            "name": name,
            "age": int(age_input),
            "phone": phone
        }
        seats.append(person)
        print(f"{name} added to seat #{len(seats) - 1}")

    elif cmd == 2:
        if len(seats) == 0:
            print("All seats are empty.")
            continue

        try:
            location = int(input("Enter seat index to remove (0 to {}): ".format(len(seats) - 1)).strip())
            removed = seats.pop(location)
            print(f"Removed {removed['name']} from seat #{location}")
        except (ValueError, IndexError):
            print("Invalid seat index.")

    elif cmd == 3:
        if not seats:
            print("No passengers currently.")
        else:
            print("\nCurrent seat list:")
            for i, person in enumerate(seats):
                print(f" Seat {i}: {person['name']}, Age: {person['age']}, Phone: {person['phone']}")

    elif cmd == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid command. Please choose 1-4.")






























