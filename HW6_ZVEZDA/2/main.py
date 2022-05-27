import csv


def read_fl(fl_name: str) -> dict:
    """
    Чтение файла по имени
    Результат: лист данных
    fl_name : имя файла
    """
    usr_dct = dict()
    with open(fl_name, encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            usr_dct.update({row[0].lower(): row[1].lower()})
    return usr_dct


def main():
    user_loop = True
    while user_loop:
        user_loop = True
        usr_dct = read_fl("db.csv")
        usr_rqst = input().lower().strip()
        if usr_rqst in usr_dct.keys():
            print(f"{usr_rqst.capitalize()} - {usr_dct[usr_rqst]}")
        else:
            print("По Вашему запросу ничего не найдено, могу предложить:")
            for i in usr_dct.keys():
                print(f"- {i.capitalize()}")
        one_more_time = input("Повторить? y/n\t")
        if one_more_time == "n":
            user_loop = False


if __name__ == "__main__":
    main()
