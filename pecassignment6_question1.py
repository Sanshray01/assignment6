num1 = int(input("enter a number : "))
list1 = []
for i in range(1,num1):
    if num1%i==0:
        list1.append(i)
print(list1)
if sum(list1) ==num1:
    print("it is a perfect number.")
else:
    print("it is not a perfect number.")