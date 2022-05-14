def read_fl(fl_name: str) -> list:
    """
    Чтение файла по имени
    Результат: лист данных
    fl_name : имя файла
    """
    usr_lst = list()
    with open(fl_name, "r", encoding="utf-8") as f:
        for line in f:
            usr_lst.append(line.strip())
    return usr_lst


def main():
    move_dict = {
        "stay": 0,
        "right": -1,
        "left": 1,
    }
    start_pos = 2
    current_pos = 2
    f = open("furry_road3.txt", "r", encoding="utf-8")
    for line in f:
        usr_lst = line.strip().split(";")
        for move, delta in move_dict.items():
            new_move = current_pos + delta
            if new_move < 0 or new_move >= len(usr_lst):
                continue
            if usr_lst[new_move] == "0":
                print(move)
                current_pos = new_move
                break


if __name__ == "__main__":
    main()
