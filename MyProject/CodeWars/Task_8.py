def high_and_low(numbers):
    # numbers = str(sorted([int(x) for x in numbers.split(" ")])[0])
    return str(sorted([int(x) for x in numbers.split(" ")])[-1]) + "" + str(sorted([int(x) for x in numbers.split(" ")])[0])


high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")