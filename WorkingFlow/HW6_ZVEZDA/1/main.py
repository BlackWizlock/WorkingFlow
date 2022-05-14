def read_fl(fl_name: str) -> list:
    """
    Чтение файла по имени
    Результат: лист данных
    fl_name : имя файла
    """
    usr_lst = list()
    with open(fl_name, "r", encoding="utf-8") as f:
        for line in f:
            usr_lst.append(float(line.strip()))
    return usr_lst


def write_fl(fl_name: str, usr_km_list: list):
    """
    Запись файла по имени
    Результат: процедура, без возврата
    fl_name : имя файла
    """
    with open(
        fl_name,
        "w",
        encoding="utf-8",
    ) as f:
        f.writelines(usr_km_list)


def miles_to_km_convert(miles: float) -> float:
    """
    Конвертер миль в км
    Результат флоат с км
    miles: флоат мили
    """
    return miles * 1.6


def main():
    # читаем файл
    usr_mile_lst = read_fl("miles.txt")
    # переводим мили в км
    usr_km_lst = list()
    for mile in usr_mile_lst:
        usr_km_lst.append(str(round(miles_to_km_convert(float(mile)), 1)) + "\n")
    # пишем в файл
    write_fl("kilometers.txt", usr_km_lst)


if __name__ == "__main__":
    main()
