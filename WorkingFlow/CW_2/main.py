import classes
import utils
from random import choice


def show_intro(player, word) -> None:
    """Интро для игрока

    Args:
        player : экземпляр класса
        word : экземпляр класса
    """
    print(
        f"Привет, {player.name}\n"
        f"Составьте {word.lst_word_cnt()} слов из слова {word.raw_word.upper()}\n"
        f"Слова должны быть не короче 3 букв\n"
        f"Поехали, ваше первое слово?\n"
    )


def show_statistic(player) -> None:
    """Аутро для игрока

    Args:
        player : экземпляр класса
    """
    print(
        f"Слова и попытки угадать закончились, игра завершена!\nВы угадали {player.lst_word_cnt()} слов!"
    )


def main():
    # создаем экземпляр класса Player
    player = classes.Player(input("Введите имя игрока: \t"))
    # создаем экземпляр класса BasicWord
    word = utils.load_random_word()
    # вывод интро
    show_intro(player, word)
    # обработка логики
    i = 0
    while i != word.lst_word_cnt():
        usr_input = str(input(">>>")).lower()
        if usr_input in ("stop", "стоп"):
            print("Game Over")
            quit()
        elif player.word_already_used(usr_input):
            print(
                choice(
                    [
                        "Повторяться нельзя, записываю как ошибку.",
                        "Ты уже так отвечал - ошибочка.",
                        "Так уже было, Ты ошибся.",
                    ]
                )
            )
        elif word.check_usr_input(usr_input):
            print(
                choice(
                    [
                        "Такое слово есть!",
                        "Точно! Ты прав!",
                        "Продолжай, ты на верном пути!",
                    ]
                )
            )
            player.lst_append(usr_input)
        else:
            print(
                choice(
                    [
                        "Такого слова нет - ошибка.",
                        "Ошибочка - нет такого слова.",
                        "Я такого слова не знаю - попытку упустил.",
                    ]
                )
            )
        i += 1
    # вывод аутро
    show_statistic(player)


if __name__ == "__main__":
    main()
