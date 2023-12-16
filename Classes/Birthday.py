from typing import Any
import re
from datetime import datetime


class Birthday:
    def __init__(self, birthday=None):
        self.birthday = None

        if birthday != None and not self.validate_birthday(birthday):
            raise ValueError(
                "Invalid birthday format. It should have in format DD.MM.YYYY."
            )

    def validate_birthday(self, birthday):
        regex = r"[0-9]{2}[\.]+[0-9]{2}[\.]+[0-9]{4}"
        result = re.findall(regex, birthday)
        if len(result) > 0:
            self.birthday = datetime.strptime(birthday, "%d.%m.%Y").date()
            return self.birthday
        else:
            return False

    def __str__(self):
        return (
            self.birthday.strftime("%d.%m.%Y")
            if self.birthday != None
            else "Not defined"
        )
