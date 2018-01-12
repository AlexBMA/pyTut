def multiply_by_2(num):
    return num * 2


def do_math(func, num):  # passing a function as an argument to another function
    return func(num)


def get_func_mult_by_num(num):  # function defined in a function
    def mult_by(value):
        return num * value

    return mult_by


times_two = multiply_by_2
print("4 * 2 =", times_two(4))

print("8 * 2 = ", do_math(multiply_by_2, 8))

generated_func = get_func_mult_by_num(5)

print("5 * 10 = ", generated_func(10))

listOfFuncs = [times_two, generated_func]

print("5 * 9 = ", listOfFuncs[1](9))
