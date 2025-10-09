# Write a program to print Fibonacci series up to n terms
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


# inputs
n = int(input("Enter number of terms in fibonacci sequence: "))

# process

F = [0, 1]
for i in range(2, n):
    F.append(F[i-1] + F[i-2])

# outputs

print("Fibonacci series up to", n, "terms is: ")
for i in range(n):
    print(F[i], end=', ')