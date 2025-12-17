from pathlib import Path
from dataclasses import dataclass
from lib.text import normalize
from lib.f_read_to_write import r_csv
from lab08.models import Student
import csv

@dataclass
class Group:
    head=["fio", "birthdate", "group", "gpa"]
    path: Path
    def _ensure_storage_exists(self):
        self.path.write_text("", encoding="utf-8",newline="")
        with self.path.open("w",encoding="utf-8",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(self.head)

    def __init__(self, storage_path: str):
        try:
            self.path = Path(storage_path)
        except:
            raise ValueError(" -- Path Error")
        if not self.path.exists():
            self._ensure_storage_exists()
            print(" -- no headers")

    def _read_all(self):
        all=r_csv(self.path)
        group=[]
        for student in all:
            group.append(Student.from_dict(student))
        return group

    def list(self):
        return self._read_all()

    def add(self, student: Student):
        with open(self.path, "a",encoding="utf-8",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([student.fio,student.birthdate,student.group,student.gpa])
        return f"{student.fio} -- appended"

    def find(self, substr: str):
        rows=[]
        substr=normalize(substr).title()
        for student in self._read_all():
            rows.append(Student.to_dict(student))
        find_s=[r for r in rows if substr in r["fio"]] 
        if find_s==[]:
            return f"{substr} -- unfound"
        else:
            return find_s

    def remove(self, fio: str):
        if self.find(fio) ==  f"{fio} -- unfound":
            return f"{fio} -- unfound"
        else: fio = self.find(fio)[0]["fio"]
        students=self._read_all()
        clean_file=[r for r in students if r.fio != fio] 
        with open(self.path, "w",encoding="utf-8",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(self.head)
            for student in clean_file:
                writer.writerow([student.fio,student.birthdate,student.group,student.gpa])
        return f"{fio} -- deleted"

    def update(self, fio: str, **fields):
        if self.find(fio) ==  f"{fio} -- unfound":
            return f"{fio} -- unfound"
        else: fio = self.find(fio)[0]["fio"]
        students=self._read_all()
        for s in students:
            if s.fio==fio:
                for key, data in fields.items():
                    setattr(s,key,data) #key from data to student
                break
        with open(self.path, "w",encoding="utf-8",newline="") as file:
            writer=csv.writer(file)
            writer.writerow(self.head)
            for student in students:
                writer.writerow([student.fio,student.birthdate,student.group,student.gpa])
        return f"{list(fields.keys()), fio} -- info is changed"

if __name__ == "__main__":
    student=Student(
        fio = "Нормов Норм Нормисов",
        birthdate = "16.09.2000",
        group = "NORM-25-6",
        gpa = 4.0
    )
    group=Group("data002/lab09/students.csv")

    print("Check list()")
    print(group.list(), "\n")
    print("Check _read_all()")
    print(group._read_all(), "\n")
    print(group.add(student=student), "\n")
    print("Check find()")
    print(group.find("Македонский Аленксандр Александрович"), "\n")
    print("Check remove()")
    print(group.remove("Македонский Аленксандр Александрович"), "\n")
    print("Check update()")
    print(group.update("Адекватный Адекват Адекватович",group = "BODD-14-33"))