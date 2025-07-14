print("******  Mini Calculator  ******")
Num1=float(input("Enter the first number: "))
Num2=float(input("Enter the second number: "))
print("press 1 for Addition\n press2 for Substraction\n press3 for Multiplication\n press4 for Division")
choice=int(input("Enter your choice from 1-4: "))
if choice==1:
    print(Num1+Num2)
elif choice==2:
    print(Num2-Num2)
elif choice==3:
    print(Num1*Num2)
elif choice==4:
    print(Num1/Num2)
else:
    print("invalid choice")