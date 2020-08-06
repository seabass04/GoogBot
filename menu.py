from addevent import addEvent
from datetime import time
from datetime import date

def menu():
    while True:
        print ("Hello! Please enter an option or 'exit' to exit")
        print ("1. Add Event\n2. Display Events\n3. Change event color")
        userIN = raw_input()

        if userIN == "1":
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
    eventTitle = raw_input ("\nEnter event title: \n")

    eventDate = raw_input ("Enter date (m d): \n")
    eventDate = parseDate(eventDate)

    dateCreated = date.today()

    eventDescription = raw_input("Enter event description: \n")
    if not eventDescription:
        eventDescription += 'asdasdCreated by GoogBot: %s' %dateCreated
    else:
        eventDescription += '\nCreated by GoogBot: %s' %dateCreated
        print

    #print('Title:[%s]'%eventTitle)
    #print('Date:[%s]'%eventDate)
    #print('Description:[%s]\n'%eventDescription)

    addEvent (eventTitle, eventDate, eventDescription)


def parseDate(dateIn):
    month = dateIn.split()[0]
    day = dateIn.split()[1]

    month = int(month)
    day = int(day)

    return date(2020, month , day).isoformat()


menu()
