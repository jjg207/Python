monthlist = []
mileslist = []

def populatelist():
    position = 0
    while (position < 12):
        month = input("Please enter a month name: ")
        monthlist.append(month)
        miles = int(input("Please enter miles driven for the month: "))
        mileslist.append(miles)
        position = position + 1
    return

def findmonth():
    foundmonth = -1
    position = 0
    while(position < 12):
        if(monthname == monthlist[position]):
            foundmonth = position
            break
        position = position + 1
    return foundmonth
    
def displaymonthname(pos1):
    print("The month name is:", monthlist[pos1], "and the miles driven for the month is:", mileslist[pos1])
    return

def findmostmiles():
    mostmiles = 0
    position = 1
    while (position < 12):
        if(mileslist[position] > mileslist[mostmiles]):
            mostmiles = position
        position = position + 1
    return mostmiles
    
def findleastmiles():
    leastmiles = 0
    position = 1
    while (position < 12):
        if(mileslist[position] < mileslist[leastmiles]):
            leastmiles = position
        position = position + 1
    return leastmiles

def displaymenu():
    print("**** MENU OPTIONS ****")
    print("Type P to populate miles and month name.")
    print("Type S to search for Month")
    print("Type M to search for Month name with smallest Miles")
    print("Type L to search for Month Name with Largest Miles")
    print("Type E to exit")
    choice = input("Please enter your choice: ")
    return choice

response = ""
while response!= "E" and response!= "e":
    response = displaymenu()
    if(response == "P") or (response == "p"):
        populatelist()
    elif(response == "S") or (response == "s"):
        monthname = input("Please enter the month name to search: ")
        monthentered = findmonth()
        if(monthentered == -1):
            print("The month name not found!")
        else:
            displaymonthname(monthentered)
    elif(response == "M") or (response == "m"):
        smallestmiles = findleastmiles()
        print("The result for searching the smallest miles:")
        print("The month name is:", monthlist[smallestmiles], "and the miles driven for the month is:", mileslist[smallestmiles])
    elif(response == "L") or (response == "l"):
        largestmiles = findmostmiles()
        print("The result for searching the largest miles:")
        print("The month name is:", monthlist[largestmiles], "and the miles driven for the month is:", mileslist[largestmiles])
    elif(response == "E") or (response == "e"):
        print("Thank you for using the program.")
        print("Bye")
    else:
        print("Invalid choice. Please try again!")