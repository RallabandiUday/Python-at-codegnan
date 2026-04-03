marks=int(input("Enter the marks"))
if marks>=90 and marks<=100:
    print("Grade A",marks)
elif marks>=80 and marks<=89:
    print("Grade B",marks)
elif marks>=60 and marks<=79:
    print("Grade C",marks)
elif marks>=40 and marks<=59:
    print("Grade D",marks)
elif marks>100 or marks<0:
    print("INVALID INPUT",marks)
else:
    print("Fail",marks)

