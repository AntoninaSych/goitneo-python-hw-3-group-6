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
            try:
                command = input("Enter command: ").strip()
                command_name, args = self.parse_input(command)
                # -----  Hello  command
                if command_name.lower() == "hello":
                    print("How can I help you?")
                # ----- Add  command
                elif command_name == "add":
                    try:
                        record = self.address_book.find(args[0])
                    except KeyError:
                        record = Record(args[0])
                    if len(args) == 1:
                        print("Please provide phone")
                        continue
                    record.add_phone(args[1])
                    self.address_book.add_record(record)
                # ----- Change  command
                elif command_name.startswith("change"):
                    record = self.address_book.find(args[0])
                    if len(args) == 1:
                        print("Phone can't be empty")
                        continue
                    record.edit_phone(record.phones[0], args[1])
                # ----- Phone  command
                elif command_name.startswith("phone"):
                    print(self.address_book.find(args[0]))
                # ----- All  command
                elif command_name == "all":
                    self.address_book.all()
                # ----- Add Birthday  command
                elif command_name == "add-birthday":
                    try:
                        record = self.address_book.find(args[0])
                    except KeyError:
                        record = Record(args[0])
                    if len(args) == 1:
                        print("Please provide birthday")
                        continue
                    record.add_birthday(args[1])
                    self.address_book.add_record(record)
                # ----- Show Birthday  command
                elif command_name == "show-birthday":
                    record = self.address_book.find(args[0])
                    print(record.birthday)
                # ----- Birthdays  command
                elif command_name == "birthdays":
                    self.address_book.get_birthdays_per_week()
                # ----- Exit  command
                elif command_name in ["close", "exit"]:
                    print("Good bye!")
                    break
                else:
                    print("Invalid command.")
            except:
                pass
            finally:
                self.address_book.save_to_file()
