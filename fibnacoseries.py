n = int(input("Enter how many terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b



    # using function
    
# def fibonaciseries(n):
#     a = 0
#     b = 1
#     series = []
#     for i in range(n):
#         series.append(a)
#         a, b = b, a + b
#     return series
# print(fibonaciseries(10))