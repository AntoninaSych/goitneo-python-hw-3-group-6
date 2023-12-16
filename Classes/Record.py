from Classes.Phone import Phone
from Classes.Name import Name
from Classes.Birthday import Birthday
from Classes.DecoInputError import input_error


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = list()
        self.birthday = None

    def add_phone(self, number):
        if Phone.validate_phone_number(number):
            self.phones.append(Phone(number))
        else:
            raise ValueError("Invalid phone number format. It should have 10 digits.")

    @input_error
    def edit_phone(self, old_phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i] == old_phone:
                self.phones[i] = new_phone

    @input_error
    def find_phone(self, search_phone):
        for phone in self.phones:
            if str(phone) == search_phone:
                return phone
        return None

    @input_error
    def add_birthday(self, birthday: Birthday):
        birthday = Birthday(birthday)
        self.birthday = birthday

    def __str__(self):
        phone_numbers = ", ".join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phone_numbers}, birthday: {self.birthday}"
