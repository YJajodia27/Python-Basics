#Calculator
a=eval(input("Enter a choice(1 for addition and 2 for subtraction)"))
b=eval(input("Enter a number"))
c=eval(input("Enter another number"))
if a==1:
    print(b+c)
elif a==2:
    print(b-c)
elif a<2:
    print("Wrong choice")
