# Data about 10 different people
people = [
    {"name": "John Doe", "age": 30, "blood_group": "A+"},
    {"name": "Jane Smith", "age": 25, "blood_group": "B-"},
    {"name": "Emily Davis", "age": 40, "blood_group": "O+"},
    {"name": "Michael Brown", "age": 35, "blood_group": "AB-"},
    {"name": "William Johnson", "age": 28, "blood_group": "A-"},
    {"name": "Emma Wilson", "age": 22, "blood_group": "B+"},
    {"name": "Oliver Martinez", "age": 33, "blood_group": "O-"},
    {"name": "Sophia Anderson", "age": 27, "blood_group": "AB+"},
    {"name": "James Thomas", "age": 45, "blood_group": "A+"},
    {"name": "Isabella Lee", "age": 38, "blood_group": "B-"}
]

# Function to print the information in a formatted manner
def print_person_info(person):
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"Blood Group: {person['blood_group']}")
    print("-" * 40)

# Main function
def main():
    for person in people:
        print_person_info(person)

# Run the main function
if __name__ == "__main__":
    main()
