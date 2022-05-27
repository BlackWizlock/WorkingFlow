from random import randint


class Dice:
    def __init__(self, num_dice):
        self.num_dice = num_dice
        self.dice_cnt = (4, 6, 8, 10, 20, 100)
        self.dice_hist = list()
        self.dice_thr = None
        if self.num_dice not in self.dice_cnt:
            print(f'Допустимые кубики {", ".join(map(str, self.dice_cnt))}')
            quit()
        else:
            print(f"Кубик был создан! Кол-во граней: {self.num_dice}")

    def dice_throw(self):
        self.dice_thr = randint(1, self.num_dice)
        self.dice_hist.append(str(self.dice_thr))
        return self.dice_thr

    def dice_history(self):
        return ", ".join(self.dice_hist)


def main():
    dice_4 = Dice(int(input("Введите кол-во граней: \t")))
    print(dice_4.dice_throw())
    print(dice_4.dice_throw())
    print(dice_4.dice_throw())
    print(dice_4.dice_throw())
    print(dice_4.dice_history())


if __name__ == "__main__":
    main()
