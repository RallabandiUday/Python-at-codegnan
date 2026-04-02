#One egg price is 5  and what is the cost of n eggs
EC=int(input("enter the  cost of each egg"))
N=int(input("Enter no of eggs"))
Tp=EC*N
print("Totoal cost of eggs are",Tp)

#If box contains N pencils and total price is M ,then what is the price of each pencil
N=int(input("total no. of pencils in a box"))
Tp=int(input("total cost of pencils are"))
Ep=Tp//N
print("cost of each pencil is", Ep)

# red ball price is 25 and green ball price is 30
#if i buy n red ball and m green balls then what is the total cost
Rb=25
gb=30
n=int(input("how many red balls u want to buy"))
m=int(input("how many green balls u want to buy"))
Tp=((n*Rb)+(m*gb))
print("total cost",Tp)
