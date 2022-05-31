from tkinter import *
from tkinter import filedialog
from pprint import pprint as pp
from tkinter import ttk
from .app_dao import DataBase
import json


def database_define(date, path_to_workers, path_to_templates, path_to_file_to_be_copy):
    path_to_templates += fr"\{date}_Табели"
    path_to_file_to_be_copy += fr"\_Шаблон_Табеля_{date}.xlsx"
    database = DataBase(path_to_workers)  # копируем шаблон и переименовываем под БД
    # database.create_files(date, path_to_file_to_be_copy, path_to_templates)  # создаем файлы по шаблону БД


class Window:
    def __init__(self, width, height, title="Создание табелей", resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
        self.first_line = Frame(self.root)
        self.second_line = Frame(self.root)
        self.third_line = Frame(self.root)
        self.btn_line = Frame(self.root)
        self.label_1 = Label(self.first_line, text="Список сотрудников:", width=20)
        self.path_1 = Entry(self.first_line, width=40)
        self.btn_1 = Button(self.first_line, text="Открыть", width=10, command=self._btn_1)
        self.label_2 = Label(self.second_line, text=fr'Папка "Табели":', width=20)
        self.path_2 = Entry(self.second_line, width=40)
        self.btn_2 = Button(self.second_line, text="Открыть", width=10, command=self._btn_2)
        self.label_3 = Label(self.third_line, text="Шаблон:", width=20)
        self.path_3 = Entry(self.third_line, width=40)
        self.btn_3 = Button(self.third_line, text="Открыть", width=10, command=self._btn_3)
        self.label_4 = Label(self.btn_line, text="На какой месяц:", width=20)
        self.combo_4 = ttk.Combobox(self.btn_line, values=[
                "2201", "2202", "2203", "2204", "2205", "2206", "2207", "2208", "2209", "2210", "2211", "2212"
        ])
        self.btn_4 = Button(self.btn_line, text="Создать табели", width=30, command=self._btn_4)
        self.path_to_file_1 = self._config_loader()["path_1"]
        self.path_to_file_2 = self._config_loader()["path_2"]
        self.path_to_file_3 = self._config_loader()["path_3"]

    def draw_widgets(self):
        self.first_line.pack()
        self.second_line.pack()
        self.third_line.pack()
        self.btn_line.pack()
        self.label_1.pack(side=LEFT, padx=5, pady=5)
        self.path_1.pack(side=LEFT, padx=5, pady=5)
        self.path_1.insert(0, self._default_values("path_1"))
        self.btn_1.pack(side=LEFT, padx=5, pady=5)
        self.label_2.pack(side=LEFT, padx=5, pady=5)
        self.path_2.pack(side=LEFT, padx=5, pady=5)
        self.path_2.insert(0, self._default_values("path_2"))
        self.btn_2.pack(side=LEFT, padx=5, pady=5)
        self.label_3.pack(side=LEFT, padx=5, pady=5)
        self.path_3.pack(side=LEFT, padx=5, pady=5)
        self.path_3.insert(0, self._default_values("path_3"))
        self.btn_3.pack(side=LEFT, padx=5, pady=5)
        self.label_4.pack(side=LEFT, padx=5, pady=5)
        self.combo_4.pack(side=LEFT, padx=5, pady=5)
        self.combo_4.insert(0, self._default_values("combo_4"))
        self.btn_4.pack(side=LEFT, padx=5, pady=5)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def _config_loader(self):
        with open("default_values.json", "r", encoding="UTF-8") as f:
            return json.load(f)

    def _config_writer(self, setting, input_from_user):
        db = self._config_loader()
        db[setting] = input_from_user
        with open("default_values.json", "w", encoding="UTF-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=2)

    def _default_values(self, setting):
        config = self._config_loader()
        for key, value in config.items():
            if setting == key and value:
                return value
        return ""

    def _btn_1(self):
        self.path_1.delete(0, END)
        file_1 = filedialog.askopenfilename(filetypes=(("XLSX", "*.xlsx"), ("XLS", "*.xls")))
        self.path_1.insert(1, str(file_1))
        self.path_to_file_1 = file_1

    def _btn_2(self):
        self.path_2.delete(0, END)
        file_2 = filedialog.askdirectory()
        self.path_2.insert(1, str(file_2))
        self.path_to_file_2 = file_2

    def _btn_3(self):
        self.path_3.delete(0, END)
        file_3 = filedialog.askdirectory()
        self.path_3.insert(1, str(file_3))
        self.path_to_file_3 = file_3

    def _btn_4(self):
        if self.combo_4.get() and self.path_to_file_1 and self.path_to_file_2 and self.path_to_file_3:
            self._config_writer("path_1", self.path_to_file_1)
            self._config_writer("path_2", self.path_to_file_2)
            self._config_writer("path_3", self.path_to_file_3)
            self._config_writer("combo_4", self.combo_4.get())
            database_define(self.combo_4.get(), self.path_to_file_1, self.path_to_file_2, self.path_to_file_3)
