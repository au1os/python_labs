import json, csv
from pathlib import Path

data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]




def r_json(path: Path | str) -> any:
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    if path.suffix != ".json" or path.stat().st_size == 0:
        raise ValueError("Неверный тип файла или файл пуст")
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
    



def w_json(data: any, path: Path | str) -> None:
    if data == None or data == [] or data == "":
        raise ValueError("Нет данных")
    if path.suffix != ".json":
        raise ValueError("Неверный тип файла")
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)



def r_csv(path: Path | str) -> list: #Возвращает список строк из CSV файла
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    if path.suffix != ".csv" or path.stat().st_size == 0:
        raise ValueError("Неверный тип файла или файл пуст")
    answ = []
    with open(path, "r", encoding="utf-8") as file:
        read = csv.DictReader(file)
        for row in read:
            answ.append(row)
    return answ



def w_csv(data: list[any], path: str | Path) -> None:
    if data == None or data == [] or data == "":
        raise ValueError("Нет данных")
    if path.suffix != ".csv":
        raise ValueError("Неверный тип файла")
    headers = list(data[0].keys())
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(
            file, fieldnames=headers
        )  # Записывает все кроме КЛЮЧАЙ в словарях, определяя ключи в этой строке под filednsmes
        writer.writeheader()
        writer.writerows(data)