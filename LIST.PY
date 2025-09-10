l = []
n = int(input("Enter size of list: "))
for i in range(n):
    item = input("Enter element: ")
    l.append(item)
print(l, end=" ")

    using nested

l=[]
n=int(input("enter the number or inner list="))
for i in range(n):
    l1=[]
    m=int(input(f"enter the value of element in inner list{i+1}="))
    for j in range(m):
        val=input(f"enter the elenent {j+1} of inner list{i+1}=")
        l1.append(val)
    l.append(l1)
print(l)

  multiply all number in a list  

numbers = [10, 20, 30, 40, 50]
productofnumbers = 1
for i in numbers:
    productofnumbers *= i
    print("Product of elements in the list:", productofnumbers)
 
   smallest number in a list

numbers = [30, 10, -45, 5, 20] 
minimum = numbers[0] 
for i in numbers:
 if i < minimum:
   minimum = i
print("The smallest number in the list is:", minimum)

    largest number in a list

numbers = [30, 10, -45, 5, 20] 
minimum = numbers[0] 
for i in numbers:
 if i > minimum:
    minimum = i
print("The largest number in the list is:", minimum)

   Second largest number

numbers = [30, 10, 45, 5, 20] 
numbers.sort(reverse=True)
if len(numbers) >= 2:
 second_largest = numbers[1]
 print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number.")

    even number

numbers=[1,2,3,4,5,6,7,8,9,10]
evennumbers=[num for num in numbers if num%2==0]
print("even numbers in the list:",evennumbers)

    odd number

numbers=[1,2,3,4,5,6,7,8,9,10]
evennumbers=[num for num in numbers if num%2!=0]
print("odd number in the list:",evennumbers)

remove empty list

list_of_lists=[[1,2,3],[],[4,5],[],[6,7],[]]
filtered_list=[i for i in list_of_lists if i]
print("list sfter removing lists:",filtered_list)