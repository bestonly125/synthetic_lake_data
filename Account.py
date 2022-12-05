import numpy as np
from datetime import datetime, timedelta
from openpyxl import load_workbook



wb_name = load_workbook("data_names.xlsx")
ws_data = wb_name["names"] # набор = Ф.И.О, адрес, email, ТЦ

class Account():
    def __init__(self, acc_last_day=None):
        global date_open
        global date_close
        date_open = self.gen_datetime(min_year=2019,max_year=2019)
        date_close = self.gen_datetime(min_year=2022)

        self.account = np.random.randint(100000000000,999999999999)
        self.acc_date = date_open.strftime("%d/%m/%Y")
        self. acc_close_date = date_close.strftime("%d/%m/%Y")
        self.currency = self.gen_curreny()
        self.turn_per_day = self.gen_turn_per_day()
        self.acc_balance = self.gen_balance()
        self.acc_last_day = acc_last_day
        # генератор времени
    def set_date(self,data):
        self.acc_last_day = data
    def gen_datetime(self, min_year=2019, max_year=datetime.now().year):
        # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        date = start + (end - start) * np.random.random()
        return date

        # генератор валюты
    def gen_curreny(self):
        popultion = np.random.randint(1,100)
        if popultion < 45:
            currency = 0  # 0 – RUB
        else:
            currency = np.random.randint(1,3)  # 1 – USD | 2 - EUR
        return currency

    def gen_balance(self):
        if self.currency == 0:
            balance = np.random.uniform(10000.00,500000.99)
        else:
            balance = np.random.uniform(1000.0, 50000.99)
        return round(balance,2)

    def gen_turn_per_day(self):
        if self.currency == 0:
            balance = np.random.uniform(500.00, 5000.99)
        else:
            balance = np.random.uniform(10.0, 350.99)
        return round(balance, 2)

class Transaction():
    def __init__(self, txdate=None, currency=None):
        self.txdate = txdate
        self.txsum = self.gen_txsum(currency)
        self.txplace = ws_data["J" + str(np.random.randint(1,100))].value

    def gen_txsum(self, currency):
        if currency == 0:
            txsum = np.random.uniform(500.00,100000.99)
        else:
            txsum = np.random.uniform(10.0, 1000.99)
        return round(txsum,2)
