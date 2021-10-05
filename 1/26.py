def BruteForcePrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(2,1001):
    if BruteForcePrime(i):
        print(i)