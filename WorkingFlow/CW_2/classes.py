class BasicWord:
    def __init__(self, raw_word: str, lst_word: list) -> None:
        """Конструктор класса

        Args:
            raw_word (str): слова из словаря
            lst_word (list): лист правильных ответов
        """
        self.raw_word = raw_word
        self.lst_word = lst_word

    def check_usr_input(self, usr_word: str) -> bool:
        """Проверка ввода пользователя

        Args:
            usr_word (str): ввод от пользователя

        Returns:
            bool: возвращает булевое значение, если полученное слово в листе правильных ответов
        """
        return usr_word in self.lst_word

    def lst_word_cnt(self) -> int:
        """Расчет кол-ва возможных ответов

        Returns:
            int: возврат числа длинны списка правильных ответов
        """
        return len(self.lst_word)


class Player:
    def __init__(self, name: str) -> None:
        """Конструктор класса

        Args:
            name (str): Имя игрока
        """
        self.name = name
        self.lst_word = []

    def lst_word_cnt(self) -> int:
        """Расчет кол-ва возможных ответов

        Returns:
            int: возврат числа длинны списка правильных ответов от пользователя для статистики
        """
        return len(self.lst_word)

    def lst_append(self, word: str) -> None:
        """аппенд в лист с ответами, проверка если такой ответ уже давали то скипаем

        Args:
            word (str): слово на внесение в список
        """
        if not self.word_already_used(word):
            self.lst_word.append(word)

    def word_already_used(self, word: str) -> bool:
        """Проверка наличия уникального ответа от пользователя

        Args:
            word (str): слово для проверки

        Returns:
            bool: возврат булевого значения если слово уже в листе ответов
        """
        return word in self.lst_word
