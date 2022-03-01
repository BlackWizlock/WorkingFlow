def solution(number):
    summa = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            summa += i
    return print(summa)


solution(4)
