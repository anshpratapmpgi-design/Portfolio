num = int(input("Enter number : "))
if num <= 1:
    print("Not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime number")

       
#         # using function
        
# # def prime(num):
# #  if num <= 1:
# #     print("Not prime")
# #  else:
# #     for i in range(2, num):
# #         if num % i == 0:
# #             print("Not prime")
# #             break
# #     else:
# #         print("Prime number")


#   # print all prime numbers in an interval of 1-10


# lower=1
# upper=10
# print("prime numbers",lower,"and",upper,"are")
# for  i in range (lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if(num%i)==0:
#         break
#         else:
#          print(num)
