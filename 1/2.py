while True:
    n = input("Input any number: ")
    try:
        n = int(n)
        break;
    except ValueError:
        print("Please enter valid number...")

rem = []
while n >=1 :
    rem.append(n%2)
    n = n//2

rem.reverse()
print("Binary: ", "".join([str(elem) for elem in rem]))