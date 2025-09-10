a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=int(input("enter third number :"))
if(a>b and b<c):
    print("second smallest number is :",a)
elif(b>a and b<c):
    print("second smallest number is :",b)
else:
            print("second smallest number is :",c)