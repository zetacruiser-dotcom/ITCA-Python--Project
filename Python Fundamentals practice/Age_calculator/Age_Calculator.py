from datetime import datetime

Personal_Info = [ 
    {"Name": "Ehrard", "Surname": "Jordaan", "Birthdate": "17.01.2005"},
    {"Name": "Alice", "Surname": "Smith", "Birthdate": "20.05.2006"},
    {"Name": "Bob", "Surname": "Johnson", "Birthdate": "12.09.2004"},
    {"Name": "Charlie", "Surname": "Brown", "Birthdate": "05.03.2005"},
    {"Name": "Diana", "Surname": "Miller", "Birthdate": "30.11.2006"}
]

search_date = input("Enter a date (dd.mm.yyyy): ")
search_date = datetime.strptime(search_date, "%d.%m.%Y")

print("\nPersonal Information")
for person in Personal_Info:
    birthdate = datetime.strptime(person["Birthdate"], "%d.%m.%Y")
    
    age = search_date.year - birthdate.year 
    
    if (search_date.month, search_date.day) < (birthdate.month, birthdate.day):
        age -= 1
        
    if search_date.month == birthdate.month and search_date.day == birthdate.day:
     print(f"Name: {person['Name']} {person['Surname']}, {age} years old")
     print(f"Happy Birthday, {person['Name']} {person['Surname']}! You are now {age} years old")
    else:    
        print(f"Name: {person['Name']} {person['Surname']}, {age} years old")

  
