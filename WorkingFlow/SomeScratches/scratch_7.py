def way_chose(dct: dict) -> list:
    tmp_lst = []
    for i in range(len(dct)):
        if dct.get(0)[i] or dct.get(1)[i] or dct.get(2)[i]:
            tmp_lst.insert(i, True)
        else:
            tmp_lst.insert(i, False)
    return tmp_lst


def way_chose_decode(lst: list) -> str:
    if all(lst):
        return 'stop'
    elif not lst[1]:
        return 'keep'
    elif not lst[0]:
        return 'left'
    elif not lst[2]:
        return 'right'


def main():
    lidar_data = {
        2: [False, False, True],
        1: [True, False, False],
        0: [False, False, False],
    }
    print(way_chose_decode(way_chose(lidar_data)))


if __name__ == '__main__':
    main()
