while True:
    n = input("Input any number: ")
    try:
        n = int(n)
        break;
    except ValueError:
        print("Please enter valid number...")


print(n, "'s divisors are: ")
for i in range(1, n):
    if n % i == 0:
        print(i, end = '\n')
        