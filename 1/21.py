def NInput():
    while True:
        n = input("Input any number: ")
        try:
            n = int(n)
            if(n < 0):
                raise ValueError("")
            break;
        except ValueError:
            print("Please enter valid number...")
    return n


print("Enter 2 numbers to calculate their greatest common divisor")

a = NInput()
b = NInput()

while b:
    a, b = b, a%b

print("Greatest common divisor is", a)