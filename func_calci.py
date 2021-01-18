def add (a,b) :               #function to add two numbers
    return a + b

def sub (a,b) :               #funtion to subtract two numbers
    return a - b

def mul (a,b) :               #function to multiply two numbers
    return a * b

def div (a,b) :               #funtion to divide two numbers
    return a / b 

a = int(input('enter first number : '))
b = int(input('enter second number : '))
c = int(input(1 == add, 2 == sub, 3 == multiply, 4 == divide))
if c==1 :
  print (a+b)
elif c==2 :
  print (a-b)
elif c==3 :
  print (a**b)
elif c==4 :
  print (a//b)
else : print('invalid choice')