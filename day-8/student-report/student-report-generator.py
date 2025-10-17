# Step 1
# Read the content

path = r"students.csv"
f = open(path)
content = f.readlines()
f.close()

print("INFO -> step 1", content)

# Step 2
# Process the content and store in a data structure
# What data structure will be good here? Sanjeev -> Dictionary
# student_dict -> class_dict

class_dict = {}
columns = [item.strip() for item in content[0].split(',')] # Keys of the student dictionary
for dataitem in content[1:]:
    values = [item.strip() for item in dataitem.split(',')] # Values for the student dictionary
    student_dict = dict(zip(columns, values)) # Zipping keys and values to form the student dictionary
    class_dict[student_dict['regid']] = student_dict # Adding student dictionery to class dictionary


print("\n" + "-"*100)
print("INFO -> step 2 \n", class_dict)

# Step 3
# Calculate the average

for regid in class_dict.keys():
    sum_of_subjects = float(class_dict[regid]['phy']) + float(class_dict[regid]['chem']) + \
                      float(class_dict[regid]['math']) + float(class_dict[regid]['bio'])
    class_dict[regid]['avg'] = sum_of_subjects / 4


print("\n" + "-"*100)
print("INFO -> step 3 -> Class dictionary after averages updated\n", class_dict)

# Step 4
# Calculate the rank

avgs = [class_dict[regid]['avg'] for regid in class_dict.keys()]
avgs.sort(reverse=True)

for regid in class_dict.keys():
    class_dict[regid]['rank'] = avgs.index(class_dict[regid]['avg']) + 1

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