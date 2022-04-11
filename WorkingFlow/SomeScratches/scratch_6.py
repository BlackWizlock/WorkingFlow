def mars_check(h: int, w: int) -> bool:
    if 157 <= h <= 175 and 50 <= w <= 70:
        return True
    else:
        return False


def validate(dct: dict) -> bool:
    return mars_check(dct.get('h'), dct.get('w'))


def income_for_check(lst: list) -> bool:
    for i in lst:
        return validate(i)


def main():
    candidates = [{'name': 'Юрий', 'h': 157, 'w': 60}, {'name': 'Олег', 'h': 177, 'w': 65}, {
        'name': 'Юлия', 'h': 165, 'w': 57}, {'name': 'Аркадий', 'h': 174, 'w': 59}]
    income_for_check(candidates)
    assert validate({'h': 160, 'w': 60}), 'Error for 160 and 60'
    assert validate({'h': 180, 'w': 60}) == False, 'Error for 180 and 60'
    assert validate({'h': 164, 'w': 75}) == False, 'Error for 164 and 75'
    assert validate({'h': 180, 'w': 80}) == False, 'Error for 180 and 80'


if __name__ == '__main__':
    main()
