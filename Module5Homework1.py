def calculatewages(wh, hp):
    total = wh * hp
    return total;
    
def calculatestatetax(residence):
    if(residence == "CA") or (residence == "NV") or (residence == "SD") or (residence == "WA") or (residence == "AZ"):
        statetax = totalwage * .08
    elif(residence == "TX") or (residence == "IL") or (residence == "MO") or (residence == "OH") or (residence == "VA"):
        statetax = totalwage * .07
    elif(residence == "NM") or (residence == "OR") or (residence == "IN"):
        statetax = totalwage * .06
    else:
        statetax = totalwage * .05
    return statetax

def calculatefederaltax(status):
    if(status == "Married"):
        federaltax = totalwage * .20
    elif(status == "Single"):
        federaltax = totalwage * .25
    else:
        federaltax = totalwage * .22
    return federaltax
def calculatenet(tw, ft, st):
    totalnet = tw - ft - st
    return totalnet

workhours = int(input("Please enter your work hours: "))
hourlypay = int(input("Please enter your hourly rate: "))
stateresidence = input("Please enter your state of resident: ")
maritalstatus = input("Please enter your marital status: ")
print("**********")
totalwage = calculatewages(workhours, hourlypay)
print("Your wage is: $" + str(totalwage))
federal = calculatefederaltax(maritalstatus)
print("Your federal tax is: $" + str(federal))
state = calculatestatetax(stateresidence)
print("Your state tax is: $" + str(state))
totalnetwage = calculatenet(totalwage, federal, state)
print("Your net wage is: $" + str(totalnetwage))
print("**********")