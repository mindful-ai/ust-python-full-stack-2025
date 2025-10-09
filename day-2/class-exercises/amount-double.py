# A person wants to double an amount every for a given rate of interest
# Calculate how much time is required to double the amount

# inputs 

amount = float(input("Enter the amount: "))
rate = float(input("Enter the rate of interest (in %): "))

# process
target = 2 * amount
years = 0
while(amount < target):
    amount += (amount * rate / 100)
    years += 1      

# outputs
print("Number of years required to double the amount is: ", years)

