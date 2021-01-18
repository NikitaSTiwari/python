import time
t = time.time()
T = time.localtime()
print(T)
t1 = time.asctime(T)   #formatted time function
print(t1)


import calendar
c = calendar.month(2020, 4)
print(c)

