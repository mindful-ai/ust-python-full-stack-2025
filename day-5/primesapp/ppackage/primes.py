def checkprime(n):
    """Checks wether a number is prime or not"""
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

def getHighestPrime(m, n):
    """Gives you the highest prime number in a given range m, n"""
    for i in range(n , m - 1, -1):
        if(checkprime(i)):
            return i
    return None

def getAllPrimes(m, n):
    """Gives all the prime numbers in between a range m, n"""
    count = 0
    primeNumbers = []
    for x in range(m , n + 1):
        if(checkprime(x)):
            count += 1
            primeNumbers.append(x)
    return count, primeNumbers

'''
    NOTES: importing modules will cause the module to be executed where it is imported
           When running directly primes.py __name__ ->  __main__
           When imported primes.py __name__ ->  primes

'''

# # Test checkprime()
# print("10 -> ", checkprime(10))
# print("11 -> ", checkprime(11))

# # Test getHighestPrime()
# print("100, 200 -> ", getHighestPrime(100, 200))

# # Test getAllPrimes()
# print("100, 200 -> ", getAllPrimes(100, 200))

print("primes.py __name__ = ", __name__)
if __name__ == "__main__":

    # Test checkprime()
    print("10 -> ", checkprime(10))
    print("11 -> ", checkprime(11))

    # Test getHighestPrime()
    print("100, 200 -> ", getHighestPrime(100, 200))

    # Test getAllPrimes()
    print("100, 200 -> ", getAllPrimes(100, 200))
