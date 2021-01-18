# Take two numbers as input from user
# 1st number = 1st number + 2nd number
# 2nd number = 1st number - 2nd number
# 1st number = 1st number - 2nd number
# output : numbers swapped


x = int(input('Enter first number : '))
y = int(input('Enter second number : '))
print('Numbers before swapping : ',x,y)
x = x + y
y = x - y
x = x - y
print('Numbers after swapping : ',x,y)""?\\\\