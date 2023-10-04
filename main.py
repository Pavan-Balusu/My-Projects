#Concatenate
import math

name = "John Smith"
age = 20
is_new= "True"
print(name.title())
print('John' in name)
print(name.find('J'))
print(name.replace('John','will'))
#if functions
is_having_good_credit = False
if is_having_good_credit:
    print('need to put 1,00,000 down payment')
else:
    print('need to put 2,00,000 down payment')
#elif functions
is_having_good_credit = False
is_having_bad_credit = False
if is_having_good_credit:
    print('need to put 1,00,000 down payment')
elif is_having_bad_credit:
    print('need to put 2,00,000 down payment')
else:
    print('No credit history not eligible for financing')
#Other conditions
price = 1000000
is_having_good_credit = False
if is_having_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
    print(f"down_payment: ${down_payment}")
#Comparison Operators
name = "Pavan"
if len(name)<3:
    print("name must be at least 3 characters")
elif len(name)>50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")
#weight conversion program
weight = int(input("What is your weight"))
Lbs_or_kgs = input("is it in (L)bs or (K)gs")
if Lbs_or_kgs.upper() =="L":
    conversion=weight*0.45
    print(f"your weight is {conversion} kilos")
else:
    conversion = weight / 0.45
    print(f"your weight is {conversion} pounds")
#while loop
X=1
while X<10:
    X = X+1
    print("pavan " * X)
print("Done")
#guess Game
Secret_Number = 10
guess_count = 0
no_of_guesses = 3
while guess_count < no_of_guesses:
    guess = int(input('guess the number:'))
    guess_count += 1
    if guess == Secret_Number:
        print('You won million dollors')
        break
    else:
        print('You lost')
        break
#Guess Name
Secret_name = 'Pavan'
no_of_chances = 3
guess_count = 0
while guess_count <= no_of_chances:
    guess = input('Guess Name:'.title())
    if guess == Secret_name:
        print('You won million dollars')
        break
    else:
         print('you lost pay 10 dollors back')
         break


