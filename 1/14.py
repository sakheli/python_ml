def NInput():
    while True:
        n = input("Input any number: ")
        try:
            n = int(n)
            break;
        except ValueError:
            print("Please enter valid number...")
    return n

numbers = [NInput() for i in range(10)]
sum = 0

for elem in numbers:
    sum += elem

print(sum/10)