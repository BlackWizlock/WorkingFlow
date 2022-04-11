lst = [1, 2, 3, 4, 5, 6]


def modify_list(l):
    i = 0
    while i != len(l):
        if l[i] % 2 != 0:
            lst.pop(i)

        else:
            lst[i] = lst[i] // 2
            i += 1


print(modify_list(lst))
