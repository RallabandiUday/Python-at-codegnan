n=int(input("Enter year"))
if n%4==0 and n%100!=0 or  n%400==0 :
    print("Leap year",n)
else:
    print("Not a leap year",n)
