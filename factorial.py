n = int(input("Enter any number: "))
factorial = 1

for i in range(1, n+1):
    factorial *= i  
print("Factorial of", n, "is:", factorial)

# using function
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# n=int(input("enter any number :"))
# print("factorial number=",fact(n)) 