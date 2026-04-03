n=int(input("Enter the number"))
if n>0 and n%2==0:
    print("Postive Even number",n)
elif n>0 and n%2!=0:
    print("Postive odd number",n)
elif n<0 and n%2==0:
    print("negative Even number",n)
else:
    print("negative odd number",n)
