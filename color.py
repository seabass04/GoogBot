from itertools import islice

def colorchange():
    #print ("This would give options to change color and what not\n")
    colorfile = open("color.txt","w")#clears file
    colors = ["Blue", "Green", "Purple", "Red", "Yellow", "Orange", "Turquoise", "Gray", "Bold Blue", "Bold Green", "Bold Red"]

    print
    for i in range(len(colors)):
        print("%i. %s" %(i+1, colors[i]))

    userIN = int(input ("\nEnter color choice: \n"))
    colorfile.write("%i %s\n" %(userIN,colors[userIN - 1]))
    print

def getcolorId():#returns string, may change to int
    colorfile = open("color.txt","r")
    colorId = colorfile.readline()
    if colorId[2].isspace():
        colorId = colorId[:2]
    else:
        colorId = colorId[:1]

    colorfile.close()
    return colorId

def getcolor():#returns string
    colorfile = open("color.txt","r")
    color = colorfile.readline()
    if color[2].isspace():
        color = color[3:-1]
    else:
        color = color[2:-1]

    colorfile.close()
    return color

#print(getcolorId())
#print(getcolor())
#colorchange()
