print("Welcome to the rollercoaster!")
height = int(input("What is your height in inches?\n"))
bill = 0

if height >= 48:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    elif 45 <= age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.")

    want_photos = input("Would you like your photo taken for an additional $3? Y or N\n").upper()
    if want_photos == "Y":
        bill += 3

    print(f"Your final bill is ${bill}. Thank you!")

else:
    print("Sorry, you're not yet tall enough to ride.")
