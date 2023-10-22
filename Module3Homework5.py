westernregion = 0
westernmarried = 0
westernsingle = 0
westerndivorced = 0
westernseperated = 0

easternregion = 0
easternmarried = 0
easternsingle = 0
easterndivorced = 0
easternseperated = 0

southernregion = 0
southernmarried = 0
southernsingle = 0
southerndivorced = 0
southernseperated = 0


firpstate=input("please enter the state where the first person resides :")
firpstatus=input("Please enter marital status of first person :")
if(firpstate ==  'CA') or (firpstate == 'ca') or (firpstate == 'NV') or (firpstate == 'nv') or (firpstate == 'AZ') or (firpstate == 'az') or (firpstate == 'WA') or (firpstate == 'wa'):
    westernregion = westernregion + 1
    if(firpstatus == 'Married') or (firpstatus == 'married'):
        westernmarried = westernmarried + 1
    elif(firpstatus == 'Single') or (firpstatus == 'single'):
            westernsingle = westernsingle + 1
    elif(firpstatus == 'Divorced') or (firpstatus == 'divorced'):
            westerndivorced = westerndivorced + 1
    else:
        (firpstatus == 'Seperated') or (firpstate == 'seperated')
        westernseperated = westernseperated + 1
elif(firpstate == 'NY') or (firpstate == 'ny') or (firpstate == 'MA') or (firpstate == 'ma') or (firpstate == 'FL') or (firpstate == 'fl'):
    easternregion = easternregion + 1
    if(firpstatus == 'Married') or (firpstatus == 'married'):
        easternmarried = easternmarried + 1
    elif(firpstatus == 'Single') or (firpstatus == 'single'):
        easternsingle = easternsingle + 1
    elif(firpstatus == 'Divorced') or (firpstatus == 'divorced'):
        easterndivorced = easterndivorced + 1
    else:
        (firpstatus == 'Seperated') or (firpstate == 'seperated')
        easternseperated = easternseperated + 1
elif(firpstate == 'TX') or (firpstate == 'tx') or (firpstate == 'AL') or (firpstate == 'al') or (firpstate == 'GA') or (firpstate == 'ga'):
    southernregion= southernregion + 1
    if(firpstatus == 'Married') or (firpstatus == 'married'):
        southernmarried = southernmarried + 1
    elif (firpstatus == 'Single') or (firpstatus == 'single'):
        southernsingle = southernsingle + 1
    elif(firpstatus == 'Divorced') or (firpstatus == 'divorced'):
        southerndivorced = southerndivorced + 1
    else:
        (firpstatus == 'Seperated') or (firpstate == 'seperated')
        southernseperated = southernseperated + 1

spstate=input("please enter the state where the second person resides :")
spstatus=input("Please enter marital status of second person :")
if(spstate ==  'CA') or (firpstate == 'ca') or (firpstate == 'NV') or (firpstate == 'nv') or (firpstate == 'AZ') or (firpstate == 'az') or (firpstate == 'WA') or (firpstate == 'wa'):
    westernregion = westernregion + 1
    if(spstatus == 'Married') or (spstatus == 'married'):
        westernmarried = westernmarried + 1
    elif(spstatus == 'Single') or (spstatus == 'single'):
        westernsingle = westernsingle + 1
    elif(spstatus == 'Divorced') or (spstatus == 'divorced'):
        westerndivorced = westerndivorced + 1
    else:
        (spstatus == 'Seperated') or (spstate == 'seperated')
        westernseperated = westernseperated + 1
elif(spstate == 'NY') or (firpstate == 'ny') or (firpstate == 'MA') or (firpstate == 'ma') or (firpstate == 'FL') or (firpstate == 'fl'):
    easternregion = easternregion + 1
    if(spstatus == 'Married') or (spstatus == 'married'):
        easternmarried = easternmarried + 1
    elif(spstatus == 'Single') or (spstatus == 'single'):
        easternsingle = easternsingle + 1
    elif(spstatus == 'Divorced') or (spstatus == 'divorced'):
        easterndivorced = easterndivorced + 1
    else:
        (spstatus == 'Seperated') or (spstate == 'seperated')
        easternseperated = easternseperated + 1
elif(spstate == 'TX') or (firpstate == 'tx') or (firpstate == 'AL') or (firpstate == 'al') or (firpstate == 'GA') or (firpstate == 'ga'):
    southernregion= southernregion + 1
    if(spstatus == 'Married') or (spstatus == 'married'):
        southernmarried = southernmarried + 1
    elif (spstatus == 'Single') or (spstatus == 'single'):
        southernsingle = southernsingle + 1
    elif(spstatus == 'Divorced') or (spstatus == 'divorced'):
        southerndivorced = southerndivorced + 1
    else:
        (spstatus == 'Seperated') or (spstate == 'seperated')
        southernseperated = southernseperated + 1

tpstate=input("please enter the state where the third person resides :")
tpstatus=input("Please enter marital status of third person :")
if(tpstate == 'CA') or (firpstate == 'ca') or (firpstate == 'NV') or (firpstate == 'nv') or (firpstate == 'AZ') or (firpstate == 'az') or (firpstate == 'WA') or (firpstate == 'wa'):
    westernregion = westernregion + 1
    if(tpstatus == 'Married') or (tpstatus == 'married'):
        westernmarried = westernmarried + 1
    elif(tpstatus == 'Single') or (tpstatus == 'single'):
        westernsingle = westernsingle + 1
    elif(tpstatus == 'Divorced') or (tpstatus == 'divorced'):
        westerndivorced = westerndivorced + 1
    else:
        (tpstatus == 'Seperated') or (tpstate == 'seperated')
        westernseperated = westernseperated + 1
elif(tpstate == 'NY') or (firpstate == 'ny') or (firpstate == 'MA') or (firpstate == 'ma') or (firpstate == 'FL') or (firpstate == 'fl'):
    easternregion = easternregion + 1
    if(tpstatus == 'Married') or (tpstatus == 'married'):
        easternmarried = easternmarried + 1
    elif(tpstatus == 'Single') or (tpstatus == 'single'):
        easternsingle = easternsingle + 1
    elif(tpstatus == 'Divorced') or (tpstatus == 'divorced'):
        easterndivorced = easterndivorced + 1
    else:
        (tpstatus == 'Seperated') or (tpstate == 'seperated')
        easternseperated = easternseperated + 1
elif(tpstate == 'TX') or (firpstate == 'tx') or (firpstate == 'AL') or (firpstate == 'al') or (firpstate == 'GA') or (firpstate == 'ga'):
    southernregion= southernregion + 1
    if(tpstatus == 'Married') or (tpstatus == 'married'):
        southernmarried = southernmarried + 1
    elif (tpstatus == 'Single') or (tpstatus == 'single'):
        southernsingle = southernsingle + 1
    elif(tpstatus == 'Divorced') or (tpstatus == 'divorced'):
        southerndivorced = southerndivorced + 1
    else:
        (tpstatus == 'Seperated') or (tpstate == 'seperated')
        southernseperated = southernseperated + 1

fopstate=input("please enter the state where the fourth person resides :")
fopstatus=input("Please enter marital status of fourth person :")
if(fopstate == 'CA') or (firpstate == 'ca') or (firpstate == 'NV') or (firpstate == 'nv') or (firpstate == 'AZ') or (firpstate == 'az') or (firpstate == 'WA') or (firpstate == 'wa'):
    westernregion = westernregion + 1
    if(fopstatus == 'Married') or (fopstatus == 'married'):
        westernmarried = westernmarried + 1
    elif(fopstatus == 'Single') or (fopstatus == 'single'):
        westernsingle = westernsingle + 1
    elif(fopstatus == 'Divorced') or (fopstatus == 'divorced'):
        westerndivorced = westerndivorced + 1
    else:
        (fopstatus == 'Seperated') or (fopstate == 'seperated')
        westernseperated = westernseperated + 1
elif(fopstate == 'NY') or (firpstate == 'ny') or (firpstate == 'MA') or (firpstate == 'ma') or (firpstate == 'FL') or (firpstate == 'fl'):
    easternregion = easternregion + 1
    if(fopstatus == 'Married') or (fopstatus == 'married'):
        easternmarried = easternmarried + 1
    elif(fopstatus == 'Single') or (fopstatus == 'single'):
        easternsingle = easternsingle + 1
    elif(fopstatus == 'Divorced') or (fopstatus == 'divorced'):
        easterndivorced = easterndivorced + 1
    else:
        (fopstatus == 'Seperated') or (fopstate == 'seperated')
        easternseperated = easternseperated + 1
elif(fopstate == 'TX') or (firpstate == 'tx') or (firpstate == 'AL') or (firpstate == 'al') or (firpstate == 'GA') or (firpstate == 'ga'):
    southernregion= southernregion + 1
    if(fopstatus == 'Married') or (fopstatus == 'married'):
        southernmarried = southernmarried + 1
    elif (fopstatus == 'Single') or (fopstatus == 'single'):
        southernsingle = southernsingle + 1
    elif(fopstatus == 'Divorced') or (fopstatus == 'divorced'):
        southerndivorced = southerndivorced + 1
    else:
        (fopstatus == 'Seperated') or (fopstate == 'seperated')
        southernseperated = southernseperated + 1

fifpstate=input("please enter the state where the fifth person resides :")
fifpstatus=input("Please enter marital status of fifth person :")
if(fifpstate == 'CA') or (firpstate == 'ca') or (firpstate == 'NV') or (firpstate == 'nv') or (firpstate == 'AZ') or (firpstate == 'az') or (firpstate == 'WA') or (firpstate == 'wa'):
    westernregion = westernregion + 1
    if(fifpstatus == 'Married') or (fifpstatus == 'married'):
        westernmarried = westernmarried + 1
    elif(fifpstatus == 'Single') or (fifpstatus == 'single'):
        westernsingle = westernsingle + 1
    elif(fifpstatus == 'Divorced') or (fifpstatus == 'divorced'):
        westerndivorced = westerndivorced + 1
    else:
        (fifpstatus == 'Seperated') or (fifpstate == 'seperated')
        westernseperated = westernseperated + 1
elif(fifpstate == 'NY') or (firpstate == 'ny') or (firpstate == 'MA') or (firpstate == 'ma') or (firpstate == 'FL') or (firpstate == 'fl'):
    easternregion = easternregion + 1
    if(fifpstatus == 'Married') or (fifpstatus == 'married'):
        easternmarried = easternmarried + 1
    elif(fifpstatus == 'Single') or (fifpstatus == 'single'):
        easternsingle = easternsingle + 1
    elif(fifpstatus == 'Divorced') or (fifpstatus == 'divorced'):
        easterndivorced = easterndivorced + 1
    else:
        (fifpstatus == 'Seperated') or (fifpstate == 'seperated')
        easternseperated = easternseperated + 1
elif(fifpstate == 'TX') or (firpstate == 'tx') or (firpstate == 'AL') or (firpstate == 'al') or (firpstate == 'GA') or (firpstate == 'ga'):
    southernregion= southernregion + 1
    if(fifpstatus == 'Married') or (fifpstatus == 'married'):
        southernmarried = southernmarried + 1
    elif (fifpstatus == 'Single') or (fifpstatus == 'single'):
        southernsingle = southernsingle + 1
    elif(fifpstatus == 'Divorced') or (fifpstatus == 'divorced'):
        southerndivorced = southerndivorced + 1
    else:
        (fifpstatus == 'Seperated') or (fifpstatus == 'seperated')
        southernseperated = southernseperated + 1

print("The number of people who belong to Western region is :" + str(westernregion))
print("The number of people who are married in Western region is :" + str(westernmarried))
print("The number of people who are single in Western region is :" + str(westernsingle))
print("The number of people who are divorced in Western region is :" + str(westerndivorced))
print("The number of people who are separated in Western region is :" + str(westernseperated))

print("The number of people who belong to Eastern region is :" + str(easternregion))
print("The number of people who are married in Eastern region is :" + str(easternmarried))
print("The number of people who are single in Eastern region is :" + str(easternsingle))
print("The number of people who are divorced in Eastern region is :" + str(easterndivorced))
print("The number of people who are separated in Eastern region is :" + str(easternseperated))

print("The number of people who belong to Soutern region is :" + str(southernregion))
print("The number of people who are married in Soutern region is :" + str(southernmarried))
print("The number of people who are single in Soutern region is :" + str(southernsingle))
print("The number of people who are divorced in Soutern region is :" + str(southerndivorced))
print("The number of people who are separated in Soutern region is :" + str(southernseperated))

