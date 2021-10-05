def NInput():
    while True:
        n = input("Input any number: ")
        try:
            n = float(n)
            break;
        except ValueError:
            print("Please enter valid number...")
    return n


print("Input 3 numbers to calculate the mean")

print("The mean is",  (NInput() + NInput() +  NInput())/3)