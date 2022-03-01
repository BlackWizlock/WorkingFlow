def square_digits(num):
    return int("".join(str(int(num)**2) for num in str(num)))


print(square_digits(9119))
