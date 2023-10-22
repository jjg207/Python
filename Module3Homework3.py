firstexam = 0
secondexam = 0
thirdexam = 0

firstexam = int(input("Please enter your first exams score :"))
secondexam = int(input("Please enter your second exams score :"))
thirdexam = int(input("Please enter your third exams score :"))

Average = (firstexam + secondexam + thirdexam)/3

print("Your average score is :" + str(Average))

if(Average >= 90):
    print("Your grade is :A")
elif(Average >= 80) and (Average < 90):
    print("Your grade is :B")
elif(Average >= 70) and (Average < 80):
    print("Your grade is :C")
else: 
    (Average > 70)
    print("Your grade is :F")