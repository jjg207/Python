Fooddays = 0
Gasdays = 0

Mondayfood = int(input("Please enter the amount spent on food on Monday :"))
if (Mondayfood > 20): 
    Fooddays = Fooddays + 1

Mondaygas = int(input("Please enter the amount spent on gas on Monday :"))
if (Mondaygas > 10):
    Gasdays = Gasdays + 1

Tuesdayfood = int(input("Please enter the amount spent on food on Tuesday :"))
if (Tuesdayfood > 20): 
    Fooddays = Fooddays + 1

Tuesdaygas = int(input("Please enter the amount spent on gas on Tuesday :"))
if (Tuesdaygas > 10):
    Gasdays = Gasdays + 1

Wednesdayfood = int(input("Please enter the amount spent on food on Wednesday :"))
if (Wednesdayfood > 20): 
    Fooddays = Fooddays + 1

Wednesdaygas = int(input("Please enter the amount spent on gas on Wednesday :"))
if (Wednesdaygas > 10):
    Gasdays = Gasdays + 1 

Thursdayfood = int(input("Please enter the amount spent on food on Thursday :"))
if (Thursdayfood > 20):
    Fooddays = Fooddays + 1

Thursdaygas = int(input("Please enter the amount spent on gas on Thursday :"))
if (Thursdaygas > 10):
    Gasdays = Gasdays + 1

Fridayfood = int(input("Please enter the amount spent on food on Friday :"))
if (Fridayfood > 20): 
    Fooddays = Fooddays + 1

Fridaygas = int(input("Please enter the amount spent on gas on Friday :"))
if (Fridaygas > 10):
    Gasdays = Gasdays + 1

Saturdayfood = int(input("Please enter the amount spent on food on Saturday :"))
if (Saturdayfood > 20): 
    Fooddays = Fooddays + 1

Saturdaygas = int(input("Please enter the amount spent on gas on Saturday :"))
if (Saturdaygas > 10):
    Gasdays = Gasdays + 1

Sundayfood = int(input("Please enter the amount spent on food on Sunday :"))
if (Sundayfood > 20): 
    Fooddays = Fooddays + 1

Sundaygas = int(input("Please enter the amount spent on gas on Sunday :"))
if (Sundaygas > 10):
    Gasdays = Gasdays + 1

print ("You spent more than 20 dollars per day on food in " + str(Fooddays) + " days of the week.")

print ("You spent more than 10 dollars per day on gas in " + str(Gasdays) + " days of the week.")
