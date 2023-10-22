namelist = []
idlist = []
score1list = []
score2list =[]
score3list = []

def populatelist():
    position = 0
    while (position < 4):
        name = input("Please enter a student's name : ")
        namelist.append(name)
        identity = int(input("Please enter the student's ID: "))
        idlist.append(identity)
        score1 = int(input("Please enter first score: "))
        score1list.append(score1)
        score2 = int(input("Please enter scond score: "))
        score2list.append(score2)
        score3 = int(input("Please enter third score: "))
        score3list.append(score3)
        position = position + 1
    return

def findupdate():
    foundupdate = -1
    position = 0
    while(position < 4):
        if(updateid == idlist[position]):
            foundupdate = position
            break
        position = position + 1
    return foundupdate
    
def displayupdate(du):
    print("The student name is: " + namelist[du])
    print("ID is: " + str(idlist[du]))
    print("First score  is: " + str(score1list[du]))
    print("Second score  is: " + str(score2list[du]))
    print("Third score  is: " + str(score3list[du]))
    score1update = int(input("Please enter first score: "))
    score1list[du] = score1update
    score2update = int(input("Please enter scond score: "))
    score2list[du] = score2update
    score3update = int(input("Please enter third score: "))
    score3list[du] = score3update
    return
    
def findstudent():
    foundstudent = -1
    position = 0
    while(position < 4):
        if(studentid == idlist[position]):
            foundstudent = position
            break
        position = position + 1
    return foundstudent

def displaystudent(ds):
    print("The student name is: " + namelist[ds])
    print("ID is: " + str(idlist[ds]))
    print("First score  is: " + str(score1list[ds]))
    print("Second score  is: " + str(score2list[ds]))
    print("Third score  is: " + str(score3list[ds]))
    return

def findgrade():
    foundgrade = -1
    position = 0
    while(position < 4):
        if(calculatetid == idlist[position]):
            foundgrade = position
            break
        position = position + 1
    return foundgrade

def displaygrade(dg):
    gradeaverage = (score1list[dg] + score2list[dg] + score3list[dg])/3
    print("The average is: " + str(gradeaverage))
    if(gradeaverage >= 90):
        print("The grade is: A")
    elif(gradeaverage <= 89) and (gradeaverage >= 80):
        print("The grade is: B")
    elif(gradeaverage <= 79) and (gradeaverage >= 70):
        print("The grade is: C")
    elif(gradeaverage <= 69) and (gradeaverage >= 60):
        print("The grade is: D")
    else:
        (gradeaverage < 60)
        print("The grade is: F")
    return

def displaymenu():
    print("**** MENU OPTIONS ****")
    print("Type P to populate the student information.")
    print("Type U to update student Information")
    print("Type D to display the student information.")
    print("Type C to calculate the Grade.")
    print("Type E to exit")
    choice = input("Please enter your choice: ")
    return choice
    
response = ""
while response!= "E" and response!= "e":
    response = displaymenu()
    if(response == "P") or (response == "p"):
        populatelist()
    elif(response == "U") or (response == "u"):
        updateid = int(input("Please enter the ID of the student: "))
        updateentry = findupdate()
        if(updateentry == -1):
            print("The ID is not found!")
        else:
            displayupdate(updateentry)
    elif(response == "D") or (response == "d"):
        studentid = int(input("Please enter the ID of the student: "))
        studententry = findstudent()
        if(studententry == -1):
            print("The ID is not found!")
        else:
            displaystudent(studententry)
    elif(response == "C") or (response == "c"):
        calculatetid = int(input("Please enter the ID of the student: "))
        calculateentry = findgrade()
        if(calculateentry == -1):
            print("The ID is not found!")
        else:
            displaygrade(calculateentry)
    elif(response == "E") or (response == "e"):
        print("Thank you for using the program.")
        print("Bye")
    else:
        print("Invalid choice. Please try again!")