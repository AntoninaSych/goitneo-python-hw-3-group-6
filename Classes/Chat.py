from datetime import datetime
import collections
from Classes.AddressBook import AddressBook
from Classes.Record import Record


class Chat:
    def __init__(self):

        self.address_book = AddressBook()

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

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

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
                pass
            elif command_name == "birthdays":
                pass
            elif command_name in ["close", "exit"]:
                print("Good bye!")
                break
            else:
                print("Invalid command.")
