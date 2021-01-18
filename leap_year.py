# Take input from user
# if condition : year / 400 == 0 or year / 4 == 0 and year / 100 != 0
# ouput


y = int(input('Enter the year : '))
if y / 400 == 0 or y / 4 == 0 and y / 100 != 0 : 
    print(y, 'is a leap year')
else:
    print(y, 'is not a leap year')