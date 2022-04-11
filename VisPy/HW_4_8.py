stuff_db = {
    "Мария А": "Фронтендер",
    "Алексей А": "Фронтендер",
    "Иван Б": "Бэкендер",
    "Тоня И": "Бэкендер",
    "Дарья У": "Тестировщик",
    "Валерия К": "Бэкендер",
    "Дарья У": "Тестировщик",
    }

# user_input = input("Enter proffession : \t")
user_input = "Бэкендер"

for k, v in stuff_db.items():
    if v is user_input:
        print(k, end=", ")