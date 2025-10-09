# Get numeric values from the user until they enter !
# Then extract the following stats:
# - count of numbers entered
# - sum of numbers entered
# - average of numbers entered  
# - max of numbers entered
# - min of numbers entered  
# - median of numbers entered
# - standard deviation of numbers entered
# Print as a dictionary

import statistics

# inputs

numbers = []
while True:
    val = input("Enter a number (! to stop): ")
    if val == '!':
        break
    elif val.isdigit():
        numbers.append(float(val))

print("Numbers entered:", numbers)

# calculations

D = {}
D['count'] = len(numbers)
D['sum'] = sum(numbers) 
D['average'] = D['sum'] / D['count'] if D['count'] > 0 else 0
D['max'] = max(numbers) if D['count'] > 0 else None
D['min'] = min(numbers) if D['count'] > 0 else None
D['median'] = statistics.median(numbers) if D['count'] > 0 else None
D['stddev'] = statistics.stdev(numbers) if D['count'] > 1 else None

# output
print(D)
