loopcount = 0
married = 0
divorced = 0
single = 0
separated = 0
m20 = 0
m30 = 0
m40 = 0
m50 = 0
d20 = 0
d30 = 0
d40 = 0
d50 = 0
s20 = 0
s30 = 0
s40 = 0
s50 = 0
sep20 = 0
sep30 = 0
sep40 = 0
sep50 = 0

while(loopcount < 6):
    maritalstatus = input("Please enter persons marital status: ")
    age = int(input("Please enter perons age: "))
    if(maritalstatus == "MARRIED") or (maritalstatus == "married"):
        married = married + 1
        if(age >= 20) and (age < 30):
            m20 = m20 + 1
        elif(age >= 30) and (age < 40):
            m30 = m30 + 1
        elif(age >= 40) and (age < 50):
            m40 = m40 + 1
        elif(age >= 50):
            m50 = m50 + 1
        else:
            print("Sorry ! The person does not belong to any group")
    elif(maritalstatus == "DIVORCED") or (maritalstatus == "divorced"):
        divorced = divorced + 1
        if(age >= 20) and (age < 30):
            d20 = d20 + 1
        elif(age >= 30) and (age < 40):
            d30 = d30 + 1
        elif(age >= 40) and (age < 50):
            d40 = d40 + 1
        elif(age >= 50):
            d50 = d50 + 1
        else:
            print("Sorry ! The person does not belong to any group")
    elif(maritalstatus == "SINGLE") or (maritalstatus == "single"):
        single = single + 1
        if(age >= 20) and (age < 30):
            s20 = s20 + 1
        elif(age >= 30) and (age < 40):
            s30 = s30 + 1
        elif(age >= 40) and (age < 50):
            s40 = s40 + 1
        elif(age >= 50):
            s50 = s50 + 1
        else:
            print("Sorry ! The person does not belong to any group")
    elif(maritalstatus == "SEPARATED") or (maritalstatus == "separated"):
        separated = separated + 1
        if(age >= 20) and (age < 30):
            sep20 = sep20 + 1
        elif(age >= 30) and (age < 40):
            sep30 = sep30 + 1
        elif(age >= 40) and (age < 50):
            sep40 = sep40 + 1
        elif(age >= 50):
            sep50 = sep50 + 1
        else:
            print("Sorry ! The person does not belong to any group")
    else:
        print("Sorry ! The marital status does not belong to one of the known statuses")
    loopcount = loopcount + 1
print("*****")

print("The number of pepole who are married is: " + str(married))
print("The number of pepole who are married and over the 50 is: " + str(m50))
print("The number of pepole who are married and in the age group of 40's is: " + str(m40))
print("The number of pepole who are married and in the age group of 30's is: " + str(m30))
print("The number of pepole who are married and in the age group of 20's is: " + str(m20))
print("*****")
print("The number of pepole who are single is: " + str(single))
print("The number of pepole who are single and over the 50 is: " + str(s50))
print("The number of pepole who are single and in the age group of 40's is: " + str(s40))
print("The number of pepole who are single and in the age group of 30's is: " + str(s30))
print("The number of pepole who are single and in the age group of 20's is: " + str(s20))
print("*****")
print("The number of pepole who are divorced is: " + str(divorced))
print("The number of pepole who are divorced and over the 50 is: " + str(d50))
print("The number of pepole who are divorced and in the age group of 40's is: " + str(d40))
print("The number of pepole who are divorced and in the age group of 30's is: " + str(d30))
print("The number of pepole who are divorced and in the age group of 20's is: " + str(d20))
print("*****")
print("The number of pepole who are separated is: " + str(separated))
print("The number of pepole who are separated and over the 50 is: " + str(sep50))
print("The number of pepole who are separated and in the age group of 40's is: " + str(sep40))
print("The number of pepole who are separated and in the age group of 30's is: " + str(sep30))
print("The number of pepole who are separated and in the age group of 20's is: " + str(sep20))
print("*****")
    