federaltax = 0
statetax = 0
tax = 0
netsalary = 0
salary = 0

West = ["California", "Nevada", "Arizona", "Washington"]
South = ["Texas", "NewMexico", "Alabama"]
East = ["Newyork", "Illinois", "Wisconsin", "Delaware"]

for count in range (5):
    employee = input("Please enter employee Name: ")
    salary = int(input("Please enter employee salary: "))
    if(salary > 100000):
        federaltax = salary * 0.20
    else:
        federaltax = salary * 0.15
    state = input("Please enter employee state: ")
    if state in West:
        statetax = salary * 0.10
    elif state in South:
        statetax = salary * 0.09
    elif state in East:
        statetax = salary * 0.08
    else:
        statetax = salary * 0.12
    print(employee + " federal tax is: " + str(federaltax))
    print(employee + " state tax is: " + str(statetax))
    tax = federaltax + statetax
    netsalary = salary - tax
    print(employee + " net salary is: " + str(netsalary))
    print("*****")