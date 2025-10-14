import primes
print("new-project.py __name__ = ", __name__)

# inputs

print("Enter your data: ")
n = []
while True:
    
    x = input("-> ")
    if x == "!":
        break
    else:
        if x.isdigit():
            n.append(int(x))

print("Numbers entered: ", n)

# process

primeNumbers = []
for item in n:
    if primes.checkprime(item):
        primeNumbers.append(item)

# output

print("-"*80)
print("Prime numbers -> ", primeNumbers)