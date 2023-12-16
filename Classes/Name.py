from Classes.Field import Field


class Name(Field):
    name = Field

    def __str__(self):
        return str(self.value)
