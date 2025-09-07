import pandas as pd 
import json
import os
from person import Person 

os.chdir(os.path.dirname(__file__))  


    
# print current list of person 
def printEntry():
    if not Person.idByIndex:
        print("No current ID selected.")
        return

    person = Person.persons.get(Person.idByIndex)
    if not person:
        print(f"Error: ID {Person.idByIndex} not found.")
        return

    print(f"ID: {Person.idByIndex}, Name: {person['name']}, Age: {person['age']}")

# Add a new person entry to the registry (update dict, list, counters)
def saveNewEntry():
    personObj.id = input("Enter ID: ").strip()
    if not personObj.id.isdigit():
        print("Invalid ID - must contain digits only")
        return

    if personObj.id in Person.persons:
        print("ID already exists!")
        return

    personObj.name = input("Enter Name: ").strip()
    personObj.age = input("Enter Age: ").strip()
    if not age.isdigit():
        print("Invalid age")
        return
    
    Person.persons_id_list.append(personObj.id)

    age = int(personObj.age)
    Person.persons[Person.id] = {"name": personObj.name, "age": age}
    Person.total_age += age
    Person.person_count += 1
    print(f"ID {personObj.id} saved successfully")

# Search for a person entry by ID and print it  
def searchById():
    if not Person.persons_id_list or Person.person_count == 0:
        print("No entries yet")
        return
    Person.search = input("Enter ID to search: ").strip()
    if Person.search in Person.persons:
        Person.idByIndex = Person.search
        Person.person = Person.persons[Person.search]
        printEntry()
    else:
        print("ID not found")

# Print the average age of all persons
def printAgesAverage():
    if Person.person_count == 0:
        print("No entries yet")
    else:
        average = Person.total_age / Person.person_count
        print(f"The average age is: {average:.2f}")

# Print all person names
def printAllNames():
    if not Person.persons_id_list:
        print("No entries yet")
        return
    # The ID is used indirectly in the data retrieval process. 
    # Removing it may cause errors, so it should be kept even if it seems unused.
    for i, (printId, data) in enumerate(Person.persons.items()):
        print(f"{i}. {data['name']}")

# Print all person IDs
def printAllIds():
    if not Person.persons_id_list:
        print("No entries yet")
        return
    for i, printId in enumerate(Person.persons):
        print(f"{i}. {printId}")

# Print all person entries with IDs, names, and ages
def printAllEntries():
    if not Person.persons_id_list:
        print("No entries yet")
        return
    for i, (printId, data) in enumerate(Person.persons.items()):
        print(f"{i}. ID: {printId}, Name: {data['name']}, Age: {data['age']}")

# Print a person entry by index (order of insertion)
def printEntryByIndex():
    if not Person.persons_id_list:
        print("No entries yet")
        return
    # this Print a person entry by index from persons_id_list
    index = input("Enter index: ").strip()
    if not index.isdigit():
        print("Invalid index")
        return
    index = int(index)
    if 0 <= index < len(Person.persons_id_list):
        Person.idByIndex = Person.persons_id_list[index]
        Person.person = Person.persons.get(Person.idByIndex)
        if not Person.person:
            print(f"Error ID {Person.idByIndex} not found.")
            return
        printEntry()
    else:
        print("Index out of range")

#create csv file from the python code
def createCSVFile(choice1):
    
    if not Person.persons_id_list:
        print("No entries yet - nothing to export")
        return
    # Export all person records to a CSV file (column names from config.json)
    print("this app was only meant to create csv files")
    if not choice1.lower().endswith(".csv"):
        print("you have try to enter file that isn't csv," 
        " so try again enter csv file")
        return
    
    config_path = "D:/Users/razva/Desktop/Nadav Assinment/summery project 3/config.json"

    data = []

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            raw = f.read()
            print(f" File content:\n{raw}")
            columns_config = json.loads(raw)
            print(" JSON parsed successfully:", columns_config)

    except Exception as e:
            print(f"Error reading config file: {e}")
            return
    
    for person_id, person in Person.persons.items():
        row = {
            columns_config["id"]: person_id,
            columns_config["name"]: person["name"],
            columns_config["age"]: person["age"]
        }
        data.append(row)
    df = pd.DataFrame(data)
    df.to_csv(choice1,index = False)

#Delete the registry by re-calling the constructor
def resetAllData():
    Person.__init__()
    print("All data has been reset.")

# Main loop: display the menu and handle user choices
def run():

    while True:
        printMenu()
        choice = input("Please enter your choice: ")

        if choice == "0":
            resetAllData()
        elif choice == "1":
            saveNewEntry()
        elif choice == "2":
            searchById()
        elif choice == "3":
            printAgesAverage()
        elif choice == "4":
            printAllNames()
        elif choice == "5":
            printAllIds()
        elif choice == "6":
            printAllEntries()
        elif choice == "7":
            printEntryByIndex()
        elif choice == "8":
            
            choice1 = input("What is your output file name?")
            createCSVFile(choice1)
            
        elif choice == "9" or choice.lower() == "exit":
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == "y":
                print("Goodbye!")
                break
        else:
            print("Invalid choice")

        input("Press Enter to continue...")

#printing the menu 
def printMenu():
    menu_items = [
        "0. Reset all data",
        "1. Save a new entry",
        "2. Search by ID",
        "3. Print ages average",
        "4. Print all names",
        "5. Print all IDs",
        "6. Print all entries",
        "7. Print entry by index",
        "8. Save all data",
        "9. Exit"
    ]

    print("Menu:\n" + "\n".join(menu_items))

# running the app
if __name__ == "__main__":
    personObj = Person()

run()