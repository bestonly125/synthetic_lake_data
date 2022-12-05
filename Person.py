from openpyxl import load_workbook
import numpy as np
from datetime import datetime, timedelta

wb_name = load_workbook("data_names.xlsx")
ws_personal_data = wb_name["names"] # набор = Ф.И.О, адрес, email


class Person():

    def __init__(self):
        global persons
        persons = self.gen_person()
        self.firstname = persons[0]
        self.lastname = persons[1]
        self. thirdname = persons[2]
        self.birthday = self.gen_datetime()
        self.sex = persons[3]
        self.marg_status =np.random.randint(0,3)
        self.nationality = self.gen_nation()[0]
        self.snils = f"{str(np.random.randint(100,500))}-{str(np.random.randint(100,999))}" \
                     f"-{str(np.random.randint(100,999))} {str(np.random.randint(10,99))}"
        self.born_place = self.gen_nation()[1]


    # генератор времени
    def gen_datetime(self,min_year=1960, max_year=datetime.now().year-18):
        # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        date = start + (end - start) * np.random.random()
        return date.strftime("%d/%m/%Y")

    # генератор национальности и место рождения
    def gen_nation(self):
        popultion = np.random.randint(1,100)
        if popultion < 90:
            nationality = np.random.randint(0,2)  # 0 – Не определено | 1- Русский
            born_place = np.random.randint(0,5)  # 0 – Москва | 1 – Санкт-Петербург | 2 – Нижний Новгород | 3 - Тула | 4 - Орел
        else:
            nationality = np.random.randint(2,4)  # 2 - Узбек | 3 - Француз
            born_place = np.random.randint(5,7)  # 5 – Узбекистан | 6 - Париж
        return nationality, born_place

    # генератор персоналных данных ФИО и гендер
    def gen_person(self):
        num = np.random.randint(1,100)
        if (num < 50): #Ж
            firstname = ws_personal_data["D" + str(np.random.randint(200,400))].value
            lastname = ws_personal_data["B" + str(np.random.randint(1,250))].value + "а"
            middlename = ws_personal_data["D" + str(np.random.randint(1,200))].value + "вна"
            sex = 0
        else: #М
            firstname = ws_personal_data["D" + str(np.random.randint(100,200))].value
            lastname = ws_personal_data["B" + str(np.random.randint(1,250))].value
            middlename = ws_personal_data["D" + str(np.random.randint(1,200))].value + "вич"
            sex = 1
        return firstname, lastname, middlename, sex



