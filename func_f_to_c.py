f = float(input('Enter the degree of temprature you want to convert : '))

def temp(f) :                           #function to convert temperature

  c = ((f-32)*5)/9
  print('converted temprature in celcius ',c)

temp(f)