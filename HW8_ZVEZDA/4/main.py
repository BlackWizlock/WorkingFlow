class Teller:
    def __init__(self):
        self.shots = 1

    def ask(self, topic):
        if self.shots == 1:
            if topic == "дорога":
                self.shots -= 1
                return print(
                    "Отправляйся на север, держись самого края леса, найдешь пещеру, пройдешь внутри, от нее 2-3 лиги до городка"
                )
            elif topic == "виверна":
                self.shots -= 1
                return print(
                    "Победить виверну можно только магическим оружием. Спроси в городке сотрудников гильдии магического метода"
                )
            elif topic == "дракон":
                self.shots -= 1
                return print(
                    "За сломанной горой в скалах живет дракон. С ним вообще никогда проблем не было"
                )
        return print("Ты исчерпал свои попытки, странник. Уходи!")


def main():
    teller = Teller()
    teller.ask("дорога")
    teller.ask("виверна")
    teller.ask("дракон")


if __name__ == "__main__":
    main()
