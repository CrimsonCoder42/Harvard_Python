people = {
    "John": "+1-617-495-1000",
    "Ellen": "+1-212-555-1234",
    "Marie": "+1-202-555-1234",
    "Bob": "+1-617-495-1000",
}

name = input("Name: ")

if name in people:
    print(f"Number: {people[name]}")

