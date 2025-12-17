from dataclasses import dataclass
from datetime import date, datetime


@dataclass
class Student:

    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):

        if not self.birthdate or self.birthdate == "" or self.birthdate == None:
            raise ValueError("Поле birthday не может быть пустым.")
        if not self.fio or self.fio == "" or self.fio == None:
            raise ValueError("Поле fio не может быть пустым.")
        if not self.group or self.group == "" or self.group == None:
            raise ValueError("Поле group не может быть пустым")

        try:

            life_years = datetime.strptime(self.birthdate, "%d.%m.%Y").date()

            if life_years > date.today():
                raise ValueError("Вперед в прошлое")
            if (date.today() - life_years).days / 365 > 120:
                raise ValueError("Вы существуете?")
        except ValueError as errors:
            if "warning: birthdate format might be invalid" in str(errors):
                raise ValueError(
                    f"Неверный формат даты: {self.birthdate}. "
                    f"Ожидается формат DD.MM.YYYY"
                ) from errors

        if not self.gpa or self.gpa == "" or self.gpa == None:
            raise ValueError("Поле GPA не должно быть пустым")

        self.gpa = float(self.gpa)
        if type(self.gpa) != float:
            raise ValueError("GPA должен быть числом")
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"Средний балл должен быть в диапазоне от 0 до 5")

    def age(self) -> int:
        birth_date = datetime.strptime(self.birthdate, "%d.%m.%Y").date()
        age = date.today().year - birth_date.year
        today = date.today()

        if today.month < birth_date.month or (
            today.month == birth_date.month and today.day < birth_date.day
        ):
            age -= 1
        return age

    def to_dict(self) -> dict:
        if not self.fio:
            raise ValueError("Строка fio не должна быть пустой")
        if not self.group:
            raise ValueError("Строка group не должна быть пустой")
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio=d["fio"], birthdate=d["birthdate"], group=d["group"], gpa=d["gpa"]
        )

    def __str__(self):
        return f"{self.fio}, {self.group}, {self.gpa}"


if __name__ == "__main__":

    data = Student(
        fio="Нормов Норм Нормисов", birthdate="14.14.2000", group="NORM-25-6", gpa=5.0
    )

    answ = data.to_dict()
    print(data)
    print(f"Словарь: {answ}")
