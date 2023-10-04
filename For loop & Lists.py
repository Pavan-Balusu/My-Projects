#For Loop
prices = [10,20,30]
total = 0
for price in prices:
    total += price
    print(f' Total is {total}')
#Nested Loop
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
#Nested Loop exercise how to print F shaped stars(****I DID IT*****)
number = [5, 2, 5, 2, 2]
Variable = 'X'
for x in number:
    for y in Variable:
        function = x*y
        print(function)
#lists
numbers = [5, 20, 80, 3, 40]
print(max(numbers))
numbers = [5, 20, 80, 3, 40]
Max = numbers[0]
for number in numbers:
    if number > Max:
        Max = number
        print(number)
x=("cherry", "banana", "mango")
print(x)
x = {"name" : "John", "age" : 36}
print(x)
xyz = "pavan"
x = xyz[2:3]
print(x)
txt = " Hello World "
X = txt.replace("Hello","J")
print(X)
old = "Ram"
txt = "My name is John, and I am {}"
print(txt.format(old))
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
print(i)
