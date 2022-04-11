usr_str_input = "начнем готовы старт добро пожаловать стоп снято вот и закончим"


def line_cutter(line: str) -> str:
    lst_line = line.lower().split()
    pos_start_int = lst_line.index("старт")
    pos_end_int = lst_line.index("стоп")
    lst_line = lst_line[pos_start_int + 1:pos_end_int]
    return " ".join(lst_line)


def main():
    print(line_cutter(usr_str_input))


if __name__ == '__main__':
    main()
