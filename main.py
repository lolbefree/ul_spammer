import time
import pyodbc
import not_for_git
import telegram
import os


bot = telegram.Bot(token=not_for_git.token)


class MyBot:
    def __init__(self):
        self.server = not_for_git.db_server
        self.database = not_for_git.db_name
        self.username = not_for_git.db_user
        self.password = not_for_git.db_pw
        self.driver = '{ODBC Driver 17 for SQL Server}'
        self.numpad_mod = ""
        self.cnn = pyodbc.connect(
            'DRIVER=' + self.driver + ';PORT=port;SERVER=' + self.server + ';PORT=1443;DATABASE=' + self.database +
            ';UID=' + self.username +
            ';PWD=' + self.password)
        self.cursor = self.cnn.cursor()

    def set_data(self, val):
        self.cursor.execute(f"insert into sales_bill_id values('{val}')")
        self.cursor.commit()

    def spammer(self, data):
        bot.sendMessage(chat_id=not_for_git.chat_id, text=data)
        time.sleep(0.5)

    def get_data(self):
        res = [i for i in
               self.cursor.execute("select * from cars_bills where docnum not in (select * from sales_bill_id)")]
        for row in res:
            self.set_data(row[1])
            self.spammer(
                """Рахунок №: {}\nДоговір: {}\nДата: {}\nМенеджер: {}\nМодель: {}\nЦіна: {}\nКлієнт: {}\n""".format(
                    row[1], row[4], row[0], row[3], row[5], row[-1], row[2]))


def main():
    MyBot().get_data()
    time.sleep(60 * 20)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as Err:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            if not os.path.isfile(f'{dir_path}/error.txt'):
                with open(f'{dir_path}/error.txt', "w") as f:
                    f.write(str(Err) + '\n')
            else:
                with open(f'{dir_path}/error.txt', "a") as f:
                    f.write(str(Err) + '\n')
            main()
