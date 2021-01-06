def Organizer():
    name_first = (input("\nWhat is your first name?: ")).lower()
    name_last = (input("What is your last name?: ")).lower()
    name_full = name_first.title() + " " + name_last.title()
    return name_full

print(Organizer())