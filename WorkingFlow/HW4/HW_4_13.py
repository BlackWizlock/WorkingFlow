students = {
    "Мария А.": 55,
    "Алексей А.": 78,
    "Иван Б.": 82,
    "Тоня И.": 79,
    "Дарья У.": 62,
    "Валерия К.": 69,
    "Дарья У.": 71,
}

user_input = 20

print("Поступили:")
print(*(k + "\n" for k, v in students.items() if v >= user_input), sep="")
