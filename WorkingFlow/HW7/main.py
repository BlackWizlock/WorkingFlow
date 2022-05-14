import functions as f

# global constants init section
STUDENTS_JSON_DB = r"students.json"
PROFESSIONS_JSON_DB = r"professions.json"


def main():
    # usr_pk_input = 1
    # usr_title_input = 'Backend'

    # Получаем ввод PK от пользователя
    usr_pk_input = int(input("Введите номер студента :\n"))
    # Обработка запроса JSON см. модуль functions
    income_student_info = f.get_student_by_pk(
        usr_pk_input, f.load_students(STUDENTS_JSON_DB)
    )
    if not income_student_info:
        print("У нас нет такого студента")
        quit()  # дроп программы, если введен отсутствующий элемент базы
    else:
        print(
            f'Студент {income_student_info["full_name"]}\nЗнает: {", ".join(income_student_info["skills"])}'
        )

    # Получаем ввод title от пользователя
    usr_title_input = str(
        input(
            f"Выберите специальность для оценки "
            f'студента {income_student_info["full_name"]}\n'
        )
    ).title()
    income_profession_info = f.get_profession_by_title(
        usr_title_input, f.load_professions(PROFESSIONS_JSON_DB)
    )
    # Обработка запроса JSON см. модуль functions
    if not income_profession_info:
        print("У нас нет такой специальности")
        quit()  # дроп программы, если введен отсутствующий элемент базы
    else:
        # Обработка запроса JSON см. модуль functions
        check_income = f.check_fitness(
            set(income_student_info["skills"]), set(income_profession_info["skills"])
        )
        print(
            f'Пригодность: {check_income["fit_percent"]}%\n'
            f'Студент знает: {", ".join(check_income["has"])}\n'
            f'Студент не знает: {", ".join(check_income["lacks"])}'
        )


if __name__ == "__main__":
    main()
