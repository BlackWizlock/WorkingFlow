user_input = '''Зашел: пришелец Хррзззз
Вышел: пришелец Хррзззз
Зашел: человек Архип
Зашел: пришелец Гззззззр
Вышел: пришелец Гззззззр
Зашел: животное кот
Вышел: животное кот
Зашел: животное кот
Вышел: животное кот
Зашел: животное кот
Вышел: животное кот'''


user_lst = user_input.split("\n")
user_dct = {}
for i in user_lst:
    k, v = i.split(": ")
    user_dct.setdefault(v, 0)
    if k == "Зашел":
        user_dct[v] = user_dct[v] + 1
    elif k == "Вышел":
        user_dct[v] = user_dct[v] - 1
print("Зашли, но не вышли :")
for k, v in user_dct.items():
    if v > 0:
        print(k)
print("Вышли, но не зашли :")
for k, v in user_dct.items():
    if v < 0:
        print(k) 
