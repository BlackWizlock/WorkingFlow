def second_divider(sec: int) -> str:
    hours = sec // 3600
    sec = sec - hours * 3600
    minutes = sec // 60
    seconds = sec % 60
    output = str()
    if hours:
        output += f'{hours:4} ч'
    if minutes:
        output += f'{minutes:4} мин'
    return f'{output} {seconds:4} сек'


def main():
    return print(second_divider(366700))


if __name__ == '__main__':
    main()
