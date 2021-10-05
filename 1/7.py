while True:
    n = input("Input any number: ")
    try:
        n = int(n)
        break;
    except ValueError:
        print("Please enter valid number...")

if n%10 == 0:
    print("Is divisible by 10")
else:
    print("Is not divisible by 10")