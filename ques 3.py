q = int(input('enter quantity : '))
if q*100>1000:
    print ('cost is',(q*100)-(.1*q*100))
else:
    print('cost is', q*100)