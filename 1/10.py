while True:
    year = input("Input any year: ")
    try:
        year = int(year)
        break;
    except ValueError:
        print("Please enter valid year...")

print("This is a leap year" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "This is not a leap year")