### LISTS ###


class_marks=[77, 95, 89, 65]

manupa = ["Manupa", 25, "Kadawatha"]
dinil = ["Dinil", 23, "Colombo"]

# print(prime_nums)
# print( len(prime_nums) )

# print(prime_nums[3])

# num = prime_nums[3]
# print(num)

# print(prime_nums)
# prime_nums[2]=11
# print(prime_nums)

# a = 3
# def change_val(val):
#     return 4
#
#
# print(a)
# a = change_val(a)
# print(a)

# prime_nums=[2,3,5,7]
# def change_val(val):
#     print("val", val)
#     val[0]=13
#
#
# print(prime_nums)
# change_val(prime_nums)
# print(prime_nums)

# for i in prime_nums:
#     print(i)

# print(prime_nums)
# prime_nums.insert(1, 13)
# print(prime_nums)

# prime_nums=[2,3,5,7]
# val=prime_nums[:]
#
# print(prime_nums)
# val[2]=13
# print("val", val)
# print(prime_nums)

# sequences=[[2,4,6], [2,3,5], [1,4,9]]
# for i in sequences:
#     for k in i:
#         print(k)



def display_menu():
    print("Enter 1 to add a person")
    print("Enter 2 to remove a person")

seats = [] # Model the list of seats
MAX_SEAT_COUNT=5

while True:
    display_menu()
    cmd = int(input("Enter a command: "))
    if cmd == 1:
        if len(seats) == 5:
            print("Seats are full, cannot add more people")
        name = input("Enter person name: ")
        seats.append(name)
    elif cmd == 2:
        if len(seats) == 0:
            print("All seats are empty")
        location=int(input("Enter seat location: "))
        seats.pop(location)
    else:
        print("Invalid Command")





























