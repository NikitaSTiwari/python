#Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.



Odd = []
Even = []

for i in range (1,101):
	if i%2 == 0:
		Even.append(i)
	else:
		Odd.append(i) 

