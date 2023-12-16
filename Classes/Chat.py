from datetime import datetime
import collections
from Classes.AddressBook import AddressBook
from Classes.Record import Record
from Classes.DecoInputError import input_error


@input_error
class Chat:
    def __init__(self):

        self.address_book = AddressBook()
        self.address_book.read_from_file()
        self.menu = """
            # - hello
            # - add <username> <phone>
            # - change <username> <phone>
            # - phone <username>
            # - all: Всі контакти
            # - add-birthday <username> <birthday>: Додати дату народження для вказаного контакту.
            # - show-birthday <username>: Показати дату народження для вказаного контакту.
            # - birthdays: Показати дні народження, які від
            # - "close", "exit"
        """
        self.filename = "contacts.txt"
        self.main()

    def __str__(self):
        print(self.address_book)

    @input_error
    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    @input_error
    def main(self):
        print(self.menu)

        while True:
            command = input("Enter command: ").strip()
            command_name, args = self.parse_input(command)

            if command_name.lower() == "hello":
                print("How can I help you?")
            elif command_name == "add":
                try:
                    record = self.address_book.find(args[0])
                except KeyError:
                    record = Record(args[0])
                record.add_phone(args[1])
                self.address_book.add_record(record)
            elif command_name.startswith("change"):
                record = self.address_book.find(args[0])
                record.edit_phone(record.phones[0], args[1])
            elif command_name.startswith("phone"):
                print(self.address_book.find(args[0]))
            elif command_name == "all":
                self.address_book.all()
            elif command_name == "add-birthday":
                try:
                    record = self.address_book.find(args[0])
                except KeyError:
                    record = Record(args[0])
                record.add_birthday(args[1])
                self.address_book.add_record(record)
            elif command_name == "show-birthday":
                record = self.address_book.find(args[0])
                print(record.birthday)
            elif command_name == "birthdays":
                self.address_book.get_birthdays_per_week()
            elif command_name in ["close", "exit"]:
                print("Good bye!")
                break
            else:
                print("Invalid command.")
        self.address_book.save_to_file()
