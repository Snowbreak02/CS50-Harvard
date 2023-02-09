"""
students = {
    "Jeremy" : "east" ,
    "James" : "west",
    "Hatim" : "north",
    "Angus" : "south",
}

for student in students:
    print(student, students[student], sep="| ")
"""
# [] means its going to be a list
# {} means its going to be a 'dictionary' bcos u can link values tgt inside

students = [
    {"name": "Jeremy", "house": "Landed", "race": "chink"},
    {"name": "James", "house": "HDB", "race": "chink"},
    {"name": "Hatim", "house": "condo", "race": "indian"},
    {"name": "Faeez", "house": "hdb", "race": None}

]

for student in students:
    print(student["name"], student["house"], student["race"], sep="| ")