#Practice - write a program that prints out all the elements of the list that are less than 5.
import random

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
number = int(input('Please enter number any number '))
for x in list:
    if x <= number:
        new_list.append(x)
print(new_list)
#write a program that returns a list that contains only the elements that are common between the lists (without duplicates)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
unique_list = []
for y in a:
    for z in b:
        if y == z:
           if y not in unique_list:
               unique_list.append(y)
print(unique_list)
#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
word = str(input("Please enter any word we'll tell you whether this string is a palindrome or not "))
new_word = word[::-1]
if word == new_word:
    print('this word is palindrome', new_word)
else:
    print('this word is not palindrome')


