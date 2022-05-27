user_db = {
    "Носят шапочку": {"Бычок", "Сельдь", "Лосось", "Скумбрия", "Толстолобик", "Карась"},
    "Любят гулять": {"Карась", "Анчоус", "Карп", "Треска", "Лещ", "Лосось"},
    "Поют": {"Лещ", "Камбала", "Толстолобик", "Сельдь", "Бычок"},
    "Задумчивые": {"Окунь", "Щука", "Осетр", "Бычок", "Сельдь", "Скумбрия"},
}


def check_diff(first_set: set, second_set: set):
    return first_set.intersection(second_set)


def main():
    for i in user_db:
        for j in user_db:
            if j == i:
                continue
            else:
                print("-" * 20)
                print(f"{i} и {j}")
                print(", ".join(check_diff(set(user_db[i]), set(user_db[j]))))


if __name__ == "__main__":
    main()
