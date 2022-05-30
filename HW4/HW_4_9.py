user_array = [
    "Водород",
    "Гелий",
    "Литий",
    "Бериллий",
    "Бор",
    "Углерод",
    "Азот",
    "Кислород",
    "Фтор",
    "Неон",
    "Натрий",
    "Магний",
    "Алюминий",
    "Кремний",
    "Фосфор",
    "Сера",
    "Хлор",
    "Аргон",
    "Калий",
    "Кальций",
    "Скандий",
    "Титан",
    "Ванадий",
    "Хром",
    "Марганец",
    "Железо",
    "Кобальт",
    "Никель",
    "Медь",
    "Цинк",
    "Галлий",
    "Германий",
    "Мышьяк",
    "Селен",
    "Бром",
    "Криптон",
    "Рубидий",
    "Стронций",
    "Иттрий",
    "Цирконий",
    "Ниобий",
    "Молибден",
    "Технеций",
    "Рутений",
    "Родий",
    "Палладий",
    "Серебро",
    "Кадмий",
    "Индий",
    "Олово",
    "Сурьма",
    "Теллур",
    "Иод",
    "Ксенон",
    "Цезий",
    "Барий",
    "Лантан",
    "Церий",
    "Празеодим",
    "Неодим",
    "Прометий",
    "Самарий",
    "Европий",
    "Гадолиний",
    "Тербий",
    "Диспрозий",
    "Гольмий",
    "Эрбий",
    "Тулий",
    "Иттербий",
    "Лютеций",
    "Гафний",
    "Тантал",
    "Вольфрам",
    "Рений",
    "Осмий",
    "Иридий",
    "Платина",
    "Золото",
    "Ртуть",
    "Таллий",
    "Свинец",
    "Висмут",
    "Полоний",
    "Астат",
    "Радон",
    "Франций",
    "Радий",
    "Актиний",
    "Торий",
    "Протактиний",
    "Уран",
    "Нептуний",
    "Плутоний",
    "Америций",
    "Кюрий",
    "Берклий",
    "Калифорний",
    "Эйнштейний",
    "Фермий",
    "Менделевий",
    "Нобелий",
    "Лоуренсий",
    "Резерфордий",
    "Дубний",
    "Сиборгий",
    "Борий",
    "Хассий",
    "Мейтнерий",
    "Дармштадтий",
    "Рентгений",
    "Коперниций",
    "Нихоний",
    "Флеровий",
    "Московий",
    "Ливерморий",
    "Теннессин",
    "Оганесон",
    "Унуненний",
    "Унбинилий",
    "Унбиуний",
    "Унбибий",
    "Унбитрий",
    "Унбиквадий",
    "Унбипентий",
    "Унбигексий",
    "Унбисептий",
]

user_dict = {v + 1: k for v, k in enumerate(user_array)}

# user_input = input("Enter number for element :\t")
user_input = 29
if user_input == 1:
    print(
        f"{user_input} это {user_dict.get(user_input)}\nСоседи:\n{user_dict.get(user_input+1)}"
    )
elif user_input == len(user_dict):
    print(
        f"{user_input} это {user_dict.get(user_input)}\nСоседи:\n{user_dict.get(user_input-1)}"
    )
else:
    print(
        f"{user_input} это {user_dict.get(user_input)}\nСоседи:\n{user_dict.get(user_input-1)}\n{user_dict.get(user_input+1)}"
    )