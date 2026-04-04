n=int(input())
for i in range(2,n):
    if n%i==0:
        print(f" {n} Not a prime number")
        break
    else:
        print(f" {n} Prime number")
        break
