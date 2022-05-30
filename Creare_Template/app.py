from openpyxl import Workbook, load_workbook
from pprint import pprint as pp
from os.path import exists
from os import mkdir
from shutil import copy
import datetime

date = input('Введите дату для создания шаблона (ГГММ):')
PATH_TO_WORKERS = r"\\pnk2.local\resources\Проектный отдел\Общие\Администрирование\Список сотрудников ПД\Список сотрудников ПД.xlsx"
PATH_TO_TEMPLATES = fr"\\pnk2.local\resources\Проектный отдел\Общие\Администрирование\Табель\{date}_Табели"
PATH_TO_FILE_TO_BE_COPY = fr"\\pnk2.local\resources\Проектный отдел\Общие\Администрирование\Табель\Шаблоны табелей\_Шаблон_Табеля_{date}.xlsx"


# создаем базу данных
class DataBase:
    def __init__(self, path):
        """
        Создаем базу данных
        :param path: Путь до списка сотрудников в формате xlsx
        """
        self.path = path
        self._db = []
        self._load_db()

    def _load_db(self):
        wb = load_workbook(self.path)
        sheet_ranges = wb["Лист1"]
        for row in sheet_ranges.iter_rows():
            for cell in row:
                self._db.append(cell.value)

    def __repr__(self):
        return "\n".join(self._db)

    @property
    def db(self):
        return self._db


def main():
    database = DataBase(PATH_TO_WORKERS)
    # создаем папку - если её нет
    start = datetime.datetime.now()
    if not exists(PATH_TO_TEMPLATES):
        mkdir(PATH_TO_TEMPLATES)
    # копируем шаблон и переименовываем под БД
    for item in database.db:
        try:
            copy(PATH_TO_FILE_TO_BE_COPY, fr"{PATH_TO_TEMPLATES}\{date}_{item}.xlsx")
            pp(f"Создание файла: {date}_{item} - создан!")
        except:
            pp(f"Ошибка при создании файла: {date}_{item}")
    pp(f"Затрачено времени на генерацию: {datetime.datetime.now() - start}")


if __name__ == '__main__':
    main()
