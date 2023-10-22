lowincome =0
mediumincome = 0
highincome = 0
eliteincome = 0

firstincome = int(input("Please enter yearly income of first person :"))
if(firstincome <= 30000):
    lowincome = lowincome + 1
elif (firstincome > 30000) and (firstincome <= 50000):
    mediumincome = mediumincome + 1
elif (firstincome > 50000) and (firstincome <= 75000):
    highincome = highincome + 1
else:
    (firstincome > 75000)
    eliteincome = eliteincome + 1

secondincome = int(input("Please enter yearly income of second person :"))
if(secondincome <= 30000):
    lowincome = lowincome + 1
elif (secondincome > 30000) and (secondincome <= 50000):
    mediumincome = mediumincome + 1
elif (secondincome > 50000) and (secondincome <= 75000):
    highincome = highincome + 1
else:
    (secondincome > 75000)
    eliteincome = eliteincome + 1

thirdincome = int(input("Please enter yearly income of third person :"))
if(thirdincome <= 30000):
    lowincome = lowincome + 1
elif (thirdincome > 30000) and (thirdincome <= 50000):
    mediumincome = mediumincome + 1
elif (thirdincome > 50000) and (thirdincome <= 75000):
    highincome = highincome + 1
else:
    (thirdincome > 75000)
    eliteincome = eliteincome + 1

fourthincome = int(input("Please enter yearly income of fourth person :"))
if(fourthincome <= 30000):
    lowincome = lowincome + 1
elif (fourthincome > 30000) and (fourthincome <= 50000):
    mediumincome = mediumincome + 1
elif (fourthincome > 50000) and (fourthincome <= 75000):
    highincome = highincome + 1
else:
    (fourthincome > 75000)
    eliteincome = eliteincome + 1

fifthincome = int(input("Please enter yearly income of fifth person :"))
if(fifthincome <= 30000):
    lowincome = lowincome + 1
elif (fifthincome > 30000) and (fifthincome <= 50000):
    mediumincome = mediumincome + 1
elif (fifthincome > 50000) and (fifthincome <= 75000):
    highincome = highincome + 1
else:
    (fifthincome > 75000)
    eliteincome = eliteincome + 1

sixthincome = int(input("Please enter yearly income of sixth person :"))
if(sixthincome <= 30000):
    lowincome = lowincome + 1
elif (sixthincome > 30000) and (sixthincome <= 50000):
    mediumincome = mediumincome + 1
elif (sixthincome > 50000) and (sixthincome <= 75000):
    highincome = highincome + 1
else:
    (sixthincome > 75000)
    eliteincome = eliteincome + 1

seventhincome = int(input("Please enter yearly income of seventh person :"))
if(seventhincome <= 30000):
    lowincome = lowincome + 1
elif (seventhincome > 30000) and (seventhincome <= 50000):
    mediumincome = mediumincome + 1
elif (seventhincome > 50000) and (seventhincome <= 75000):
    highincome = highincome + 1
else:
    (seventhincome > 75000)
    eliteincome = eliteincome + 1

print("Number of people who made less than  or equal to 30000 is :" + str(lowincome))

print("Number of people who made above 30000 and  less than or equal to 50000 is :" + str(mediumincome))

print("Number of people who made  above 50000 and less than or equal to 75000 is :" + str(highincome))

print("Number of people who made  above 75000 is :" + str(eliteincome))

totalincome = firstincome + secondincome + thirdincome + fourthincome + fifthincome + sixthincome + seventhincome

print("The total(Combined) earning made by all people is :" + str(totalincome))