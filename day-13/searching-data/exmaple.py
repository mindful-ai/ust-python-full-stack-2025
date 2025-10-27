patients = [
    {"name": "Anita Sharma", "age": 30, "disease": "Fever"},
    {"name": "Ravi Kumar", "age": 42, "disease": "Diabetes"},
    {"name": "John Doe", "age": 45, "disease": "Hypertension"}
]


disease = input("Disease ?")
for patient in patients:
    if patient["disease"].lower() == disease.lower():
        print("Patient found: ", patient["name"])


