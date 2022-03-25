class Buffer:
    def __init__(self):
        self.counter = []
        self.five_cnt = 0
        # конструктор без аргументов
        pass

    def add(self, *a):
        for i in a:
            self.counter.append(i)
            if len(self.counter) % 5 in (0, 5):
                print(sum(self.counter[self.five_cnt * 5:(self.five_cnt + 1) * 5]))
                self.five_cnt += 1

    def get_current_part(self):
        return self.counter[self.five_cnt * 5:]


buf = Buffer()
buf.add(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
