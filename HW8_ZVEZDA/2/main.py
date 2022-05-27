class Hero:
    def __init__(self, name: str = "Скиталец"):
        self.name: str = name
        self.health: int = 100
        self.experience: int = 0
        self.level: int = 1
        self.exp_on_current_level: int = 15
        self.exp_over: int = 0
        print(f"{self.name} - был создан!")
        print(f"Настало твоё время! {self.name}\n")

    def get_level(self):
        return print(f"Уровень персонажа {self.name}: {self.level}")

    def get_health(self):
        return print(f"Здоровье персонажа {self.name}: {self.health}")

    def _round_up(self, num: float) -> int:
        if num % 10 != 0:
            return int(((num // 10) + 1) * 10)
        else:
            return int(num)

    def add_experience(self, exp: int):
        exp = exp + self.exp_over
        while exp != 0:
            if exp > 0 and exp > self.exp_on_current_level:
                self.level += 1
                exp -= self.exp_on_current_level
                self.exp_on_current_level += self.exp_on_current_level
                self.health = self._round_up(self.health * 1.5)
                print(
                    f"{self.name} повышен уровень! {self.level}!\n"
                    f"Экспы до следующего уровня: {self.exp_on_current_level}\n"
                    f"Здоровье повысилось! Теперь оно: {self.health}\n"
                )
            else:
                self.exp_over += exp
                break


def main():
    Player_1 = Hero("Валера")
    Player_1.add_experience(20)
    Player_1.add_experience(100)
    Player_1.add_experience(1000)
    Player_1.add_experience(20)

    Player_1.get_level()
    Player_1.get_health()


if __name__ == "__main__":
    main()
