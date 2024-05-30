import csv

FILENAME = "teachers.csv"

def readFile():
    teachers = []
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                teachers.append(row)
    except FileNotFoundError:
        print("File Not Found. Creating a New File")
        with open(FILENAME, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=attributes)
            writer.writeheader()
    return teachers

def writeFile(teachers):
    with open(FILENAME, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=attributes)
        writer.writeheader()
        for teacher in teachers:
            writer.writerow(teacher)

def showAll():
    teachers = readFile()
    if (len(teachers) == 0):
        print("No records to show. Enter some new records to view one")
        return
    for record in teachers:
        print(record)
    
def filterOnCriteria(records):
    print("a) Filter by Age")
    print("b) Filter by number of classes")
    criterion = input("Enter filter option: ")
    if (criterion.lower() == 'a'):
        [start, end] = list(map(int, input("Enter space separated range of age[start, end](both included and start <= end): ").split())) #Example 10 20 or 24 24
        print("Result of the Query:")
        for record in records:
            if (int(record['age']) >= start and int(record['age']) <= end):
                print(record)
    elif (criterion.lower() == 'b'):
        [start, end] = list(map(int, input("Enter space separated range of classes[start, end](both included and start <= end): ").split())) #Example 10 20 or 24 24
        print("Result of the Query:")
        for record in records:
            if (int(record['Num_Classes']) >= start and int(record['Num_Classes']) <= end):
                print(record)
    else:
        print("Invalid input!!")

def searchRecords(records):
    name = input("Enter the name of the teacher: ")
    searchList = []
    for record in records:
        if (record['full_name'].lower() == name.lower()):
            searchList.append(record)
    if (len(searchList) > 1):
        print("Multiple records exists by the name " + name)
        ageSearch = input("Do you want to filter further by DOB(Y/N): ")
        if (ageSearch.upper() == 'Y'):
            dob = input("Enter the DOB of the teacher(DD-MM-YYYY): ")
            for subrec in searchList:
                if (subrec['DOB'] == dob):
                    print(subrec)
        else:
            print("\n".join([str(entry) for entry in searchList]))
    elif (len(searchList) == 1):
        print(str(searchList[0]))
    else:
        print("Unable to find any record corresponding to this name")

def updateRecord(records):
    name = input("Enter name of the teacher whose details are to be updated: ")
    dob = input("Enter DOB(DD-MM-YYYY) of the teacher: ")
    update = False
    for record in records:
        if (record['full_name'].lower() == name.lower() and record['DOB'] == dob):
            print("1. Update Name\n2.Update number of classes\n")
            updateOption = int(input("Enter update option: "))
            if (updateOption == 1):
                record['full_name'] = input("Enter Updated Name: ")
            elif (updateOption == 2):
                record['Num_Classes'] = input("Enter updated number of classes: ")
            else:
                print("Invalid option selected")
            update = True
            break
    if (update):
        writeFile(records)
        print("Teacher Record Updated Successfully")
    else:
        print("No Record found to be updated.")
    return records

def deleteRecord(records):
    name = input("Enter name of the teacher: ")
    dob = input("Enter DOB(DD-MM-YYYY) of the teacher: ")
    index = -1
    for i in range(len(records)):
        if (records[i]['full_name'].lower() == name.lower() and records[i]['DOB'] == dob):
            index = i
            break
    if (index != -1):
        del records[index]
        writeFile(records)
        print("Teacher data deleted successfully")
    else:
        print("No record found to be deleted.")
    return records

def addTeacher():
    full_name = input("Enter full name: ")
    age = input("Enter age: ")
    dob = input("Enter date of birth(DD-MM-YYYY): ")
    num_classes = input("Enter number of classes: ")
    new_record = {'full_name':full_name, 'age':age, 'DOB':dob, 'Num_Classes':num_classes}
    try:
        with open(FILENAME, mode='a') as file:
            writer = csv.DictWriter(file, fieldnames=attributes)
            file_empty = file.tell() == 0
            if file_empty:
                writer.writeheader()
            writer.writerow(new_record)
    except FileNotFoundError:
        opt = input("File Not Found! Do You want to create a new file(Y/N): ")
        if (opt.upper() == 'Y'):
            with open(FILENAME, mode='w') as file:
                writer = csv.DictWriter(file, fieldnames=attributes)
                writer.writeheader()
                writer.writerow(new_record)
        else:
            return
    print("New record added to the current dataset.")

#Bonus Part Implementation
def bonusPart():
    records = readFile()
    total = 0
    for record in records:
        total = total + int(record['Num_Classes'])
    avg_classes = total / len(records) if (len(records)) else 0
    print("Average number of classes = ", avg_classes)

def printOptions():
    print("\n--------------------Teacher Management Application--------------------")
    print("1) Show All Teachers")
    print("2) Add a Teacher")
    print("3) Filter teachers based on a criteria")
    print("4) Search for a teacher")
    print("5) Update a teacher record")
    print("6) Delete a teacher")
    print("7) Calculate Average Number of Classes")
    print("8) Exit")

attributes = ['full_name', 'age', 'DOB', 'Num_Classes']
records = readFile()
while (True):
    printOptions()
    try:
        option = int(input("Enter option: "))
    except:
        print("Only numbers are allowed as options")
        continue
    if (option == 1):
        showAll()
    elif (option == 2):
        addTeacher()
        records = readFile()
    elif (option == 3):
        filterOnCriteria(records)
    elif (option == 4):
        searchRecords(records)
    elif (option == 5):
        records = updateRecord(records)
    elif (option == 6):
        records = deleteRecord(records)
    elif (option == 7):
        bonusPart()
    elif (option == 8):
        break
    else:
        print("Invalid Option. Try Again")