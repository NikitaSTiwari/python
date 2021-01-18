# take input from user
# if condition : number > 0, number < 0
# output


n = int(input('Enter a number : '))

def check(n) :

 if n > 0 : 
    print ('n','is positive')
 elif n < 0 :
    print ('n','is negative')
 else:
    print ('zero')

check (n)