class Dragon:
    def __init__(self, color, health) -> None:
        self.color = color
        self.health = health
        self.is_alive = True

    def bite(self):
        if self.is_alive:
            self.health += 10
            return print(f"Кусь на 10")
        else:
            return print(f"Кусь невозможен, дракон мертв")

    def get_damage(self, dmg):
        if dmg_twice(dmg):
            self.health = up_twice(self.health)
        else:
            self.health -= dmg
        if self.health <= 0:
            self.is_alive = False
            self.die()

    def get_health(self):
        return print(self.health if self.health > 0 else 0)

    def die(self):
        return print(f"Дракон умер")


def dmg_twice(dmg: int) -> bool:
    i = 2
    while i < dmg:
        i *= 2
    return i == dmg


def up_twice(health):
    i = 2
    while i < health:
        i *= 2
    return i


def main():
    dragon = Dragon("black", 500)
    dragon.get_health()
    dragon.get_damage(260)
    dragon.get_health()
    dragon.get_damage(4)
    dragon.get_health()
    dragon.bite()
    dragon.get_health()
    dragon.get_damage(266)
    dragon.bite()
    dragon.get_health()


if __name__ == "__main__":
    main()
