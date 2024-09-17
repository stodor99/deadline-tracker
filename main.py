#!/usr/bin/env python3
from datetime import datetime, timedelta

today = datetime.now().date()

tasks_dict = {
        "App": "19-11-2023",
        "Algo&Spiele Game": "22-11-2023",
        "Algo Game": "12-12-2023"
    }

exams_dict = {
        "CON": "28-11-2023",
        "EAA": "20-11-2023",
        "Algo&Spiele Exam": "21-11-2023",
        "Theo. Inf.": "11-12-2023"  
    }

# add to specific dict
def addAction(item, date, dict_name):
    dict_name[item] = date
    print("\n")

# remove from specific dict
def removeAction(item, dict_name):
    if item in dict_name:
        deadline_date = datetime.strptime(dict_name[item], '%d-%m-%Y').date()
        days_remaining = (deadline_date - today).days
        del dict_name[item]
        print(f"{item} removed! But you have {days_remaining} day(s) till {item}\n")

    else:
        print(f"{item} Not found. \n")

# view of specific dict
def viewAction(dict_name):
    for item, date in dict_name.items():
        print(f"{item} : {date}")
    print("\n")

# check the nearest deadlines (next two weeks)
def nextDeadlines(dict_name):
    print("\n")
    global today, next_deadlines
    two_weeks_from_now = today + timedelta(days=14)

    print("Deadlines/exams within the next two weeks: ")
    for item, deadline in dict_name.items():
        # str to date format
        deadline_date = datetime.strptime(deadline, '%d-%m-%Y').date()
        if today <= deadline_date <= two_weeks_from_now:
            days_remaining = (deadline_date - today).days
            print(f"{item}: Due in {days_remaining} day(s)")
    print("\n")

# input date until we get valid date
def getValidDate(input_function=input):
    while True:
        input_date = input("Enter the date in DD-MM-YYYY format and date should not be in the past: ")
        try:
            date = datetime.strptime(input_date, '%d-%m-%Y').date()
            if date >= datetime.now().date():
                return date.strftime('%d-%m-%Y')
            else:
                print("Date should not be in the past. Please try again.\n")
        except ValueError:
            print("Invalid date format or date. Please try again.\n")

def main():
    
    while True:
        action = input("Choose an action: [A] Add, [R] Remove, [V] View, [E] Exit: ").upper()

        if action in ['A', 'R', 'V']:
            category = input("Choose an category:  [Task] or [Exam]: ").lower()
            print("\n")

            if category == 'task' or category == 'exam': 
                dict_name = tasks_dict if category == 'task' else exams_dict
                
                if action == 'A':
                    item = input("Enter the name: ")
                    date = getValidDate()
                    addAction(item, date, dict_name)
                
                elif action == 'R':
                    item = input(f"Write name of {category} to be removed: ")
                    removeAction(item, dict_name)

                elif action == 'V':
                    viewAction(dict_name)

                    # print nearest deadlines
                    showDeadlines = input(f"Do you want to know nearest deadlines for {category}s?: [Yes] or [No]: ").upper()
                    if showDeadlines == 'YES':
                        nextDeadlines(dict_name)
                    elif showDeadlines == 'NO':
                        pass
                    else:
                        print("Invalid action. Please choose again.\n")
            else:
                print("Invalid category. Please choose again.\n")
        # stopps when entering E
        elif action == 'E':
            break

        else:
             print("Invalid action. Please choose again.\n")

if __name__ == '__main__':
    main()

