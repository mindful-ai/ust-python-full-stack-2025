# Step 1
# Read the content



print("INFO -> step 1", content)

# Step 2
# Process the content and store in a data structure
# What data structure will be good here? Sanjeev -> Dictionary
# student_dict -> class_dict


print("\n" + "-"*100)
print("INFO -> step 2 \n", class_dict)

# Step 3
# Calculate the average


print("\n" + "-"*100)
print("INFO -> step 3 -> Class dictionary after averages updated\n", class_dict)

# Step 4
# Calculate the rank


print("\n" + "-"*100)
print("INFO -> step 4 -> Class dictionary after ranks updated\n", class_dict)

# Step 5
# Display the report

template = "{0:8} | {1:15} | {2:5} | {3:5} | {4:5} | {5:5} | {6:5} | {7:5} | {8:5}"
line = '-'*90

print("\nCLASS REPORT")
print(line)
print(template.format('REGID', 'NAME', 'AGE', 'PHY', 'CHEM', 'MATH', 'BIO', 'AVG', 'RANK'))
print(line)
for regid in class_dict.keys():
    name = class_dict[regid]['name']
    id = class_dict[regid]['regid']
    age = class_dict[regid]['age']
    phy = class_dict[regid]['phy']
    chem = class_dict[regid]['chem']
    math = class_dict[regid]['math']
    bio = class_dict[regid]['bio']
    avg = class_dict[regid]['avg']
    rank = class_dict[regid]['rank']
    print(template.format(id, name, age, phy, chem, math, bio, avg, rank))
  
print(line)