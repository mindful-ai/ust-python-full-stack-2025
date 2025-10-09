# Write a program to print a character pyramid for a given character and number of rows.


'''
Enter a character: *
Enter number of rows: 3
          
          *
        * * *
      * * * * *          
'''

# inputs
ch = input("Enter a character: ")
n = int(input("Enter number of rows: "))

# process and outputs
buffer = 10
spaces = n
nstars = 1
for i in range(n + 1):
    print(' ' * (buffer + spaces), end='')
    print(ch * nstars)
    spaces -= 1
    nstars += 2