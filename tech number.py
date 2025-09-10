n=int(input("enter 2 digit number="))
temp=n
digit_sum=0
while n>0:
    r=n%10
    digit_sum=digit_sum+r
    n=n//10
if digit_sum**2==temp:
    print("tech number")
else:
    print("not a tech number")