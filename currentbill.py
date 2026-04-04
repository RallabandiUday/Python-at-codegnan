units=int(input("enter the units"))
if units>=0 and units<=100:
    print("Current bill :",units*5)
elif units>100 and units<=200:
    print("Current bill:", units*7)
else:
    print("Current bill:",units*10)
