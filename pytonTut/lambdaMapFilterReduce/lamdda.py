sum = lambda x, y: x + y

print("Sum :", sum(2, 10))

can_vote = lambda age: True if age >= 18 else False

print("Can Vote :", can_vote(19))

# lambda in lust
powerList = [lambda x: x ** 2,
             lambda x: x ** 3,
             lambda x: x ** 4]

for func in powerList:
    print(func(4))

# lambda in Dictionary

attack = {'quick': (lambda: print("Quick Attack")),
          'power': (lambda: print("Power Attack")),
          'miss': (lambda: print("Missed Attack"))}

import random

attackkey = random.choice(list(attack.keys()))

attack[attackkey]()
