def main():
    student = get_student()
    if student['name'] == "Padma":
        student['house'] = "Ravenclaw"
    print(f"{student['name']} is from {student['house']}")

def get_student():
    student = {} #making it a dict
    student["name"]  = input("Name: ")
    student["house"] = input("House: ")
    return student

if __name__ == "__main__":
    main()