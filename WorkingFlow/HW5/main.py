# Это программа помогает учить английский

import functions

score = 0  # счётчик баллов
name = input("Введите имя пользователя\n")

with open("words.txt", "r") as file:
    for word in file:
        cipher = functions.shuffle_letters(word)
        print(f"Угадай слово: {cipher}")
        answer = input()
        if answer.lower() == word.replace("\n", ""):
            print("Верно! Вы получаете 10 баллов\n")
            score += 10
        else:
            print(f"Неверно! Верный ответ - {word}")

functions.write_to_the_top(name, score)
functions.print_statistic()
