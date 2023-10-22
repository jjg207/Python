namelist = []
accountnumbers = []
balancelist = []

def populatelist():
    position = 0
    while (position < 5):
        name = input("Please enter a name: ")
        namelist.append(name)
        account = int(input("Please enter an account number: "))
        accountnumbers.append(account)
        balance = int(input("Please enter a balance: "))
        balancelist.append(balance)
        position = position + 1
    return

def findaccount():
    foundaccount = -1
    position = 0
    while(position < 5):
        if(accountnumber == accountnumbers[position]):
            foundaccount = position
            break
        position = position + 1
    return foundaccount

def displayaccount(pos1):
    print("Name is: " + namelist[pos1])
    print(namelist[pos1], "account has the balance of : $" + str(balancelist[pos1]))
    return
    
def displaymenu():
    print("**** MENU OPTIONS ****")
    print("Type P to populate accounts")
    print("Type S to search for account")
    print("Type E to exit")
    choice = input("Please enter your choice: ")
    return choice

response = ""
while response!= "E" and response!= "e":
    response = displaymenu()
    if(response == "P") or (response == "p"):
        populatelist()
    elif(response == "S") or (response == "s"):
        accountnumber = int(input("Please enter the account number to search: "))
        accountentered = findaccount()
        if(accountentered == -1):
            print("The account number not found!")
        else:
            displayaccount(accountentered)
    elif(response == "E") or (response == "e"):
        print("Thank you for using the program.")
        print("Bye")
    else:
        print("Invalid choice. Please try again!")
        
    



