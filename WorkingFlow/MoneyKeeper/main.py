class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.capacity - v >= 0:
            return True
        else:
            return False

    def add(self, v):
        if MoneyBox.can_add(self, v):
            self.capacity -= v
            print(self.capacity)
        else:
            print("no")
        # положить v монет в копилку


x = MoneyBox(100)
x.add(10)
