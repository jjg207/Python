federaltax = 0
statetax = 0
netsalary = 0
eliteincome = 0
highincome = 0
mediumincome = 0
lowincome = 0
totalfederaltax = 0
totalstatetax = 0
response = "yes"
while (response == "YES") or (response == "yes"):
    salary = int(input("Please one persons salary: "))
    if(salary > 100000):
        federaltax = salary * 0.20
    else:
        (salary < 100000)
        federaltax = salary * 0.15
    if(salary > 100000):
        eliteincome = eliteincome + 1
    elif(salary >= 50000) and (salary < 100000):
        highincome = highincome + 1
    elif(salary >= 25000) and (salary < 50000):
        mediumincome = mediumincome + 1
    else:
        (salary < 25000)
        lowincome = lowincome + 1
    statetax = salary * 0.05
    netsalary = salary - federaltax - statetax
    print("Your federal tax is :" + str (federaltax))
    print("Your state tax is :" + str(statetax))
    print("Your net salaryis: " + str(netsalary))
    totalfederaltax = totalfederaltax + federaltax
    totalstatetax = totalstatetax + statetax
    response = input("Would you like to continue?(yes/no): ")
print("*****")
print("The number of pepole who earned more than 100000 is:  " + str(eliteincome))
print("The number of pepole who earned More than or equal to 50000 and less than 100000 is:  " + str(highincome))
print("The number of pepole who earned More than or equal to 25000 and less than 50000 is:  " + str(mediumincome))
print("The number of pepole who earned Below 25000 is:  " + str(lowincome))
print("The total state tax is: " + str(totalstatetax))
print("The total federa tax is: " + str(totalfederaltax))