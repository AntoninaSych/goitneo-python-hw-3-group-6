from Classes.DecoInputError import input_error
from Classes.Record import Record
from collections import UserDict


class AddressBook(UserDict):
    def __init__(self):
        self.data = dict()

    @input_error
    def add_record(self, record: Record):
        name = str(record.name)
        self.data[name] = record

    @input_error
    def find(self, name):
        return self.data[name]

    @input_error
    def delete(self, name):
        if name in self.data:
            del self.data[name]
