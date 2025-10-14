def checkprime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def getPrimes():
    pass


print("primes.py __name__ = ", __name__)
if __name__ == "__main__":
    for n in range(11):
        print(f"{n} is ", "Prime" if checkprime(n) else "Not Prime")

