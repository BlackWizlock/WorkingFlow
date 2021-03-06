import requests
from random import choice

URL_JSON = r"https://jsonkeeper.com/b/B2TA"


class Question:
    def __init__(
        self,
        question_text,
        level,
        question_answer,
        score=0,
        usr_answer=None,
        bool_loop=False,
    ):
        # текст вопроса <- json
        self.question_text = str(question_text)
        # уровень сложности вопроса <- json
        self.level = int(level)
        # правильный ответ на вопрос <- json
        self.question_answer = str(question_answer)
        # баллы за правильный ответ <- json * 10
        self.score = int(score)
        # ответ пользователя -> json
        self.usr_answer = str(usr_answer)
        # проверка наличия ответ после random.choice -> json
        self.bool_loop = bool(bool_loop)

    def get_points(self) -> int:
        """
        Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.level * 10

    def is_correct(self) -> bool:
        """
        Возвращает True, если ответ пользователя совпадает с верным ответом иначе False.
        """
        return self.question_answer == self.usr_answer

    def build_question(self) -> None:
        """
        Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return print(f"{self.question_text}\nСложность {self.level}/5")

    def build_positive_feedback(self) -> None:
        """
        Возвращает
        "Ответ верный, получено __ баллов"
        """
        return print(f"Ответ верный, получено {self.get_points()} баллов")

    def build_negative_feedback(self) -> None:
        """Возвращает :
        Ответ неверный, верный ответ __
        """
        return print(f"Ответ неверный, верный ответ {self.question_answer}")

    def setattr_bool_loop(self, value: bool) -> bool:
        self.bool_loop = value
        return self.bool_loop


def json_get(url_link: str = URL_JSON):
    """
    url_link = глобальная переменная со ссылкой на БД - по умолчанию указан путь
    Получение базы вопросов модулем request, форматирование методом json под тип БД
    """
    return requests.get(url_link).json()


def get_statistic(question_list: list) -> str:
    """
    :param question_list: лист экземляров
    :return: строка статистики
    """
    usr_score = 0
    usr_correct_answers = 0
    for i in range(len(question_list)):
        if question_list[i].usr_answer == question_list[i].question_answer:
            usr_score += question_list[i].get_points()
            usr_correct_answers += 1
    return f"Вот и всё!\nОтвечено {usr_correct_answers} вопроса из {len(question_list)}\nНабрано баллов: {usr_score}"


def main():
    # Инициализация листа
    question_list = []
    # Получение базы вопросов
    question_db = json_get()
    # Инициализация очков
    usr_score = 0

    # Заполнение листа экземплярами класса, сортировка базы
    for line in question_db:
        question_list.append(
            Question(
                question_text=line["q"],
                level=line["d"],
                question_answer=line["a"],
                score=int(line["d"]) * 10,
            )
        )

    # Счётчик вопросов
    questions_cnt = 0
    while questions_cnt != len(question_list):
        line = choice(question_list)
        # Проверка на уникальность вопроса из БД
        if line.bool_loop:
            continue
        # Грузим вопрос из БД
        line.build_question()
        # Сеттер уникального вопроса
        line.setattr_bool_loop(True)
        line.usr_answer = input(">>>\t")
        if line.is_correct():
            line.build_positive_feedback()
            usr_score += line.get_points()
        else:
            line.build_negative_feedback()
        questions_cnt += 1

    # Вывод статистики
    print(get_statistic(question_list))


if __name__ == "__main__":
    main()
