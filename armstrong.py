n = int(input("Enter any number: "))
sum = 0
temp = n
digits = len(str(n))

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == n:
    print(n, "is an Armstrong Number")
else:
    print(n, "is not an Armstrong Number")

# using function

# def armstrong(n):
#     arm = 0
#     d = n
#     while n > 0:
#         r = n % 10
#         arm = arm + r ** 3
#         n = n // 10
#     if d == arm:
#         print("Armstrong number")
#     else:
#         print("Not an Armstrong number")

# n = int(input("Enter the value of n: "))
# armstrong(n)
