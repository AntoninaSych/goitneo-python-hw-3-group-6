import pickle
from Classes.DecoInputError import input_error
from Classes.Record import Record
from collections import UserDict
from datetime import datetime
from datetime import timedelta
from datetime import datetime, timedelta
from collections import defaultdict


class AddressBook(UserDict):
    def __init__(self):
        self.data = dict()
        self.filename = "AddressBookData.bob"

    @input_error
    def add_record(self, record: Record):
        name = str(record.name)
        self.data[name] = record

    # @input_error
    def find(self, name):
        return self.data[name]

    # @input_error
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def all(self):
        if len(self.data) == 0:
            print("Address Book is empty")
        for record in self.data.values():
            print(record)

    def get_birthdays_per_week(self):
        check = [i for i in self.data.values() if i.birthday.birthday != None]
        if len(check) == 0:
            return "You have no contacts with birthday in your list"
        birthdays_by_day = defaultdict(list)
        # Отримуємо поточну дату
        today = datetime.today().date()
        # Визначаємо день початку тижня (понеділок)
        start_of_week = today - timedelta(days=today.weekday())
        end_date = start_of_week + timedelta(days=6)
        # Вихідні - субота і неділя
        weekend_days = [5, 6]  # 5 - субота, 6 - неділя

        # Перебираємо користувачів і аналізуємо їх дати народження
        for record in self.data.values():
            if record.birthday.birthday == None:
                continue
            birthday = record.birthday.birthday
            user_name = record.name.value

            # Визначаємо дату народження на цьому році
            birthday_this_year = birthday.replace(year=today.year)

            # Перевіряємо, чи день народження вже відбувся цього року
            if birthday_this_year < today:
                # Якщо так, то переносимо його на наступний рік
                # birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                continue

            delta_days = (birthday_this_year - today).days

            # Визначаємо день тижня дня народження (переносимо на понеділок, якщо вихідний)
            day_of_week = (start_of_week + timedelta(days=delta_days)).weekday()
            # Якщо день тижня - субота або неділя, то переносимо на понеділок
            if day_of_week in weekend_days:
                day_of_week = 0  # Понеділок

            # Переводимо числове значення дня тижня у текстовий відповідно до календаря Python
            day_name = [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ][day_of_week]

            # Додаємо ім'я іменинника до відповідного дня тижня
            birthdays_by_day[day_name].append(user_name)
        if len(birthdays_by_day) == 0:
            print("There is no birthdays this week")
        # Виводимо результат
        for day, names in birthdays_by_day.items():
            print(f"{day}: {', '.join(names)}")

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        try:
            with open(self.filename, "rb") as file:
                self.data = pickle.load(file)
            return self.data
        except (OSError, IOError) as e:
            pass
