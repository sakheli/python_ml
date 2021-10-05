while True:
    n = input("Input any number: ")
    try:
        n = int(n)
        break;
    except ValueError:
        print("Please enter valid number...")

print("The amount of digits in this number is", len(str(n)))