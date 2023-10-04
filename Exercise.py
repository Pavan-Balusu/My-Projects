#Finding Leap year
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap
print(is_leap(2024))
n = 3
if n%2==0 and 2>=n<=5 or (n%2==0 and n>20):
    print('Not Weired')
else:
    print('weired')
