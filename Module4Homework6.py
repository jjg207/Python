balance = 0

while True:
    print("Type D to deposit money")
    print("Type W to withdraw money")
    print("Type B to display Balance")
    print("Type E to exit")
    response = input("Enter your choice now: ")
    if(response == "D"):
        deposit = int(input("Please enter your amount to deposit: "))
        balance = balance + deposit
    elif(response == "W"):
        withdraw = int(input("Please enter the amount you want to withdraw: "))
        if(balance > withdraw):
            balance = balance - withdraw
        else:
            (balance < withdraw)
            print("Not enough balance")
    elif(response == "B"):
        print("Your balance is: " + str(balance))
    elif(response == "E"):
        break
    else:
        print("Invalid Choice. Try again")
    print("*****")
    continue