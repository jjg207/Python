Salary = 0

input("Please enter your name :")
Salary = int(input("Please enter your salary :"))

if(Salary > 100000):
    federaltax=(Salary*20)/100
else:
     federaltax=(Salary*15)/100

statetax=(Salary*5)/100

sum = federaltax + statetax

netsalary = Salary - sum

print("Your Federal Tax is :" + str(federaltax))
print("Your State Tax is :" + str(statetax))
print("Your net salary is :" + str(netsalary))