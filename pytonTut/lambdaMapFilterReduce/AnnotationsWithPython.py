def random_func(name: str, age: int, weight: float) -> str:
    print("Name :", name)
    print("Age :", age)
    print("Weight :", weight)

    return "{} is {} years odl and weighs {}".format(name, age, weight)


print(random_func("Alex", 25, 69))
print(random_func.__annotations__)
