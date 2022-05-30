from calendar import monthrange


def allDays(y, m):
    return ['{:02d}.{:02d}.{:04d}'.format(d, m, y) for d in range(1, monthrange(y, m)[1] + 1)]


print(allDays(2022, 6))
