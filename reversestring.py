# Write a Python program that accepts a word from the user and reverse it.

w = (input('Enter a word'))
for char in range (len(w)-1,-1,-1) :
    print (w[char], end='')
    print('\n')
