n=int(input("enter number:"))
sumdigits=0
while n>0:
    sumdigits=n%102
    n//=10
    print("sum of digits",sumdigits)
    