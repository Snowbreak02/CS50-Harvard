import csv

name= input("What's your name? ")
region = input("Where do you live? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","region"])
    writer.writerow({"name": name,"region": region})