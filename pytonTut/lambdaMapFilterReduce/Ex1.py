# Create a function that receives a list and a function
# The function passed will return True or False if a list
# value is odd
# The surrounding function will return a list of odd


def is_it_odd(x):
    if x % 2 == 0:
        return True
    else:
        return False


def change_list(a, func):
    oddList = []
    for item in a:
        if func(item) is True:
            oddList.append(item)
    return oddList


def main():
    aList = range(1, 20)
    print(change_list(aList, is_it_odd))
    print("done")


main()
