n=int(input("Enter value of n"))
if n>=0:
    if n%2==0:
        print("Positive even number",n)
    else:
        print("Positive odd number",n)
else:
    if n%2==0:
        print("negative even number",n)
    else:
        print("negative odd number",n)
