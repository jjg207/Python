def calculatepassengers(fb, sb, tb):
    total = fb + sb + tb
    return total;

def calculatefare(tp):
    totalf = tp * 2.50
    return totalf;

def calculateprofit(tf):
    totaln = tf/2
    return totaln;
    
b1 = int(input("Please enter the number of passengers for bus1 :"))
b2 = int(input("Please enter the number of passengers for bus2 :"))
b3 = int(input("Please enter the number of passengers for bus3 :" ))
print("***********")
totalpassengers = calculatepassengers(b1, b2, b3)
print("There are total " + str(totalpassengers) + " passengers from three buses.")
totalfare = calculatefare(totalpassengers)
print("The total fare earned is: $" +str(totalfare))
totalnet = calculateprofit(totalfare)
print("The net profit is: $" + str(totalnet))
print("***********")