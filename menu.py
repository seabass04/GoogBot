from datetime import time
from datetime import date

def menu():
    while True:
        print ("Hello! Please enter an option or 'exit' to exit")
        print ("1. Add Event\n2. Display Events\n3. Change event color")
        userIN = raw_input()

        if userIN == "1":
            print ("Option 1 selected\n")
            addevent()

        elif userIN == "2":
            print ("Option 2 selected\n")

        elif userIN == "3":
            print ("Option 3 selected\n")
            colorchange()

        elif userIN == "exit" or userIN == "Exit":
            break

        else:
            print ("Invalid input\n")

def colorchange():
    print ("This would give options to change color and what not\n")

def addevent():
    print ("This begins the add event function\n")

    eventTitle = raw_input ("Enter event title: \n")

    eventDate = raw_input ("Enter date (x x): \n")
    eventDate = date(2020, 12, 4).isoformat()

    dateCreated = date.today()
    eventDescription = raw_input("Enter event description: \n")
    eventDescription += 'Created by GoogBot: %s' %DATE,

def parseDate

menu()
