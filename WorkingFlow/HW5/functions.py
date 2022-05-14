def shuffle_letters(word):
    """
    Функция для перемешивания букв в слове
    """
    import random

    items = random.sample(word, len(word))
    encoded_word = "".join(items)
    return encoded_word.replace("\n", "")


def get_statistic():
    """
    Функция, возвращающая рекорд и количество игр
    """
    game_counter = 0
    get_score = []
    with open("history.txt", "r") as file:
        for item in file:
            game_counter += 1
            name, score = item.strip().split(" ")
            get_score.append(score)
            max_score = max(get_score)
        return [game_counter, max_score]


def print_statistic():
    """
    Функция, выводящая на экран рекорд и количество игр
    """
    game_statistic, max_statistic = get_statistic()
    print(f"Всего игр сыграно: {game_statistic}")
    print(f"Максимальный рекорд: {max_statistic}")


def write_to_the_top(name, score):
    """
    Функция, записывающая результат в топ
    """
    with open("history.txt", "a") as file:
        file.write(f"{name} {score}\n")
