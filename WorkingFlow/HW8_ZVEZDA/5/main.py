class Hero:
    def __init__(self):
        self.coins = []
        self.gold_coins = 0
        self.silver_coins = 0
        self.bronze_coins = 0

    def get_money(self):
        """
        1 золотая = 1 золотой
        10 серебра = 1 золотая
        100 бронза = 1 золотая
        """
        for coin in self.coins:
            if coin.metal == "gold":
                self.gold_coins += coin.value
            elif coin.metal == "silver":
                self.gold_coins += coin.value // 10
                self.silver_coins += coin.value % 10
            elif coin.metal == "bronze":
                self.gold_coins += coin.value // 100
                self.bronze_coins += coin.value % 100
        return print(self.gold_coins + self.silver_coins / 10 + self.bronze_coins / 100)

class Coin:
    def __init__(self, value, metal) -> None:
        self.metal = metal
        self.value = value


def main():
    hero = Hero()
    coins = [Coin(5, "gold"), Coin(30, "silver"), Coin(15, "bronze"), Coin(8, "gold")]
    hero.coins = coins
    hero.get_money()


if __name__ == "__main__":
    main()
