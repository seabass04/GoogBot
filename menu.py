from addevent import addEvent
from color import colorchange
from color import getcolorId
from color import getcolor
from datetime import time
from datetime import date

def menu():
    while True:
        print ("Hello! Please select an option or 'exit' to exit")
        print ("1. Add Event\n2. Display Events\n3. Change event color\n4. Display event color")
        userIN = input()

        if userIN == "1":
            addevent()

        elif userIN == "2":
            print ("Option 2 selected\n")

        elif userIN == "3":
            #print ("Option 3 selected\n")
            colorchange()

        elif userIN == "4":
            #print ("Option 4 selected\n")
            print ("\nCurrent color: %s(%s)\n" %(getcolor(),getcolorId()))

        elif userIN == "exit" or userIN == "Exit":
            break

        else:
            print ("Invalid input\n")

def addevent():
    eventTitle = input ("\nEnter event title: \n")

    eventDate = input ("Enter date (m d): \n")
    eventDate = parseDate(eventDate)

    dateCreated = date.today()

    eventDescription = input("Enter event description: \n")

    if not eventDescription:
        eventDescription += 'Created by GoogBot: %s' %dateCreated
    else:
        eventDescription += '\nCreated by GoogBot: %s' %dateCreated
        print

    #print('Title:[%s]'%eventTitle)
    #print('Date:[%s]'%eventDate)
    #print('Description:[%s]\n'%eventDescription)

    addEvent (eventTitle, eventDate, eventDescription)


def parseDate(dateIn):
    month = int(dateIn.split()[0])
    day = int(dateIn.split()[1])

    return date(2020, month , day).isoformat()


menu()
