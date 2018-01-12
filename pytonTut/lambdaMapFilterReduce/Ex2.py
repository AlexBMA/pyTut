# Create a random list filled with the characters H adn T
# for heads and tails. Output the number of Hs and Ts
# Example Output
# Heads: 46
# Tails: 54

import random

number = random.randrange(100)
hAndTList = []
list2 = ["H", "T"]

for i in range(number):
    val = random.choice(list2)
    hAndTList.append(val)

countH = 0
countT = 0
for item in hAndTList:
    if item == "H":
        countH += 1
    if item == "T":
        countT += 1

print("Size of list", len(hAndTList))
print("Number of H", countH)
print("Number of T", countT)
