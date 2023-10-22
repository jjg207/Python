employee = 1
year = 1

for employee in range (1,7):
    totalsalary = 0
    highest = 0
    smallest = 500000
    for year in range (1,6):
        salary = int(input("Please enter employee " + str(employee) + " salary for year " + str(year) + ": "))
        totalsalary = totalsalary + salary
        if(salary > highest):
            highest = salary
        elif(salary < smallest):
            smallest = salary
        average = float(totalsalary)/5
        if(year == 5):
            print("Employee " + str(employee) + " smallest salary is: $"+str(smallest))
            print("Employee " + str(employee) + " highest salary is: $"+str(highest))
            print("Employee " + str(employee) + " average salary is: $"+str(average))
            print("**********")