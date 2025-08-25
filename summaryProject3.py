import pandas as pd 
import json
import os
os.chdir(os.path.dirname(__file__))  

# Person registry using dictionary
# DEBUG: shows current working directory
# print("Current working directory: \n", os.getcwd())
def printMenu():
    print("\nMenu:")
    print("1. Save a new entry")
    print("2. Search by ID")
    print("3. Print ages average")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Save alll data")
    print("9. Exit")
    

def printEntry(id, data):
    print(f"ID: {id}, Name: {data['name']}, Age: {data['age']}")

def saveNewEntry(persons, total_age_ref, person_count_ref,persons_list):
    # this Add new person to persons dict and update counters

    id = input("Enter ID: ")
    if not id.isdigit():
        print("Invalid ID – must contain digits only")
        return

    if id in persons:
        print("ID already exists!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    if not age.isdigit():
        print("Invalid age")
        return
    
    persons_list.append(id)

    age = int(age)
    persons[id] = {"name": name, "age": age}
    total_age_ref[0] += age
    person_count_ref[0] += 1
    print(f"ID {id} saved successfully")

def searchById(persons):
    search = input("Enter ID to search: ")
    if search in persons:
        printEntry(search, persons[search])
    else:
        print("ID not found")

def printAgesAverage(total_age, person_count):
    if person_count == 0:
        print("No entries yet")
    else:
        average = total_age / person_count
        print(f"The average age is: {average:.2f}")

def printAllNames(persons):
    # The ID is used indirectly in the data retrieval process. 
    # Removing it may cause errors, so it should be kept even if it seems unused.
    for i, (id,data) in enumerate(persons.items()):
        print(f"{i}. {data['name']}")

def printAllIds(persons):
    for i, id in enumerate(persons):
        print(f"{i}. {id}")

def printAllEntries(persons):
    for i, (id, data) in enumerate(persons.items()):
        print(f"{i}. ", end="")
        printEntry(id, data)

def printEntryByIndex(persons,persons_list):
    # this Print a person entry by index from persons_list
    index = input("Enter index: ")
    if not index.isdigit():
        print("Invalid index")
        return
    index = int(index)
    if 0 <= index < len(persons_list):
        id = persons_list[index]
        person = persons[id]
        printEntry(id, person)
    else:
        print("Index out of range")

def createCSVFile(choice1,persons):
    # this fuction  Export persons data to a CSV file (columns mapped from config.json)
    print("this app was only meant to create csv files")
    if not choice1.lower().endswith(".csv"):
       print("you have try to enter file that isn't csv," 
       " so try again enter csv file")
       return
       
    config_path = "D:/Users/razva/Desktop/Nadav Assinment/summery project 3/config.json"
    """ DEBUG: path checks during development
    print(f" Trying to open config from: {config_path}")
    print(" File exists?", os.path.exists(config_path))
    print(" Running from:", __file__)
    print(" Current working directory:", os.getcwd())"""

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
    
    for id, person in persons.items():
        row = {
            columns_config["id"]: id,
            columns_config["name"]: person["name"],
            columns_config["age"]: person["age"]
        }
        data.append(row)
    df = pd.DataFrame(data)
    df.to_csv(choice1,index=False)

def run():
    persons = {}
    total_age = [0]  # use list for mutable integer reference
    person_count = [0]
    persons_list =[]

    while True:
        printMenu()
        choice = input("Please enter your choice: ")

        if choice == "1":
            saveNewEntry(persons, total_age, person_count,persons_list)
        elif choice == "2":
            searchById(persons)
        elif choice == "3":
            printAgesAverage(total_age[0], person_count[0])
        elif choice == "4":
            printAllNames(persons)
        elif choice == "5":
            printAllIds(persons)
        elif choice == "6":
            printAllEntries(persons)
        elif choice == "7":
            printEntryByIndex(persons,persons_list)
        elif choice == "8":
            
            choice1 = input("What is your output file name?")
            createCSVFile(choice1,persons)
            

        elif choice == "9" or choice.lower() == "exit":
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == "y":
                print("Goodbye!")
                break
        else:
            print("Invalid choice")

        input("Press Enter to continue...")
        
        """ DEBUG: path test
        print(os.path.exists("C:/Users/razva_xfg9hp/Desktop/Nadav Assinment/summery project 3/config.json" +"\n"))
        DEBUG: script path
        print(" You are running file:", __file__) - 
        DEBUG: cwd check
        print(" Current working directory:", os.getcwd())"""
# running the app
run()
