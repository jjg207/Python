sum = 0
loopcount = 0
smallest = 0

response = int(input("How many numbers do you want to enter?: "))
smallest = response

while (loopcount < response):
    number = int(input("Please enter your number: "))
    sum = sum + number
    if(number < smallest):
        smallest = number
    avg = float(sum)/response
    loopcount = loopcount + 1
print("*****")
print("The smallest number is:", smallest)
print("The average is: " + str(avg))    
    
