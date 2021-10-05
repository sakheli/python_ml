while True:
    n = input("Input any number: ")
    try:
        n = int(n)
        break;
    except ValueError:
        print("Please enter valid number...")

print("This number is", "palindrome" if str(n) == str(n)[::-1] else "not palindrome")