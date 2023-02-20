import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file) #allows it to be less fragile, such that evenif got changes, as long as header stays inline with values, wont break
    for row in reader:
        students.append(row)

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['region']}")