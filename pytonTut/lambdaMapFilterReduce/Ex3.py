# Find the multiples of 9 from random 100 value list
# values values between 1 and 1000

import random

a = []
for i in range(100):
    a.append(random.randrange(1, 1000))

randList = list(random.randint(1, 1001) for i in range(100))

print(a)
print(list(filter((lambda x: x % 9 == 0), a)))
print(randList)

print(list(filter((lambda x: x % 9 == 0), randList)))
