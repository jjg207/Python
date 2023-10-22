elitedeposit = 0
highdeposit = 0
mediumdeposit = 0
lowdeposit = 0
totaldeposit = 0

for count in range(7):
    deposit = int(input("Please enter your deposit amount: "))
    if(deposit >= 1000):
        elitedeposit = elitedeposit + 1
        totaldeposit = totaldeposit + deposit
    elif(deposit <= 999) and (deposit >= 500):
        highdeposit = highdeposit + 1
        totaldeposit = totaldeposit + deposit
    elif(deposit <= 499) and (deposit >= 100):
        mediumdeposit = mediumdeposit + 1
        totaldeposit = totaldeposit + deposit
    elif(deposit < 100) and (deposit >= 0):
        lowdeposit = lowdeposit + 1
        totaldeposit = totaldeposit + deposit
    else:
        (deposit < 0)
        print("You entered a wrong amount!")
    
print("You have " + str(elitedeposit) + " deposit over or equal to 1000 dollars.")
print("You have " + str(highdeposit) + " deposit between 500 and 999 dollars.")
print("You have " + str(mediumdeposit) + " deposit between 100 and 499 dollars. ")
print("You have " + str(lowdeposit) + " deposit below 100 dollars.")
print("Your balance is : " + str(totaldeposit))