import csv

file = open("phonebook.csv", "a")

with open("phonebook.csv", "r") as file:

    name = input("Enter name: ")
    number = input("Enter number: ")

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})


# name = input("Enter name: ")
# number = input("Enter number: ")
#
# writer = csv.writer(file)
# writer.writerow([name, number])

file.close()

