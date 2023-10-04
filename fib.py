fib = [1, 2]
while fib[-1] < 100:
    next_number = fib[-1] + fib[-2]
    fib.append(next_number)
    print(fib)
#Finding max number in List
list = [8, 9, 56, 98, 3, 45, 8, 0]
max_number = list[0]
for number in list:
    if number > max_number:
        max_number = number
print(f'max number is {max_number}')
#lists
numbers = [1, 3, 5, 6, 10, 11]
local = 1
numbers.append(local)
numbers.insert(3, 0)
print(numbers)
#Removing Duplicate from lists
List = [3, 8, 10, 45, 10, 8]
unique_numbers = []
for x in List:
    if x not in unique_numbers:
        unique_numbers.append(x)
print(unique_numbers)
