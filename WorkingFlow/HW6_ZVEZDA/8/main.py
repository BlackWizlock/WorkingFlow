import csv


def read_file(filename: str):
    usr_sum = 0
    row_count = 0
    with open(filename, "r", encoding="utf-8") as f:
        usr_input = csv.reader(f)
        for row in usr_input:
            usr_sum += int(row[1])
            row_count += 1

    return usr_sum, row_count


def output_statistics(usr_sum: int, pos: int):
    print(f"Всего: \n" f"Позиций: {pos}\n" f"Сумма: {usr_sum}")


def main():
    output_statistics(*read_file("expenses.csv"))


if __name__ == "__main__":
    main()
