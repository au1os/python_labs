import sys
import os
from pathlib import Path


current_dir = Path(file).parent
sys.path.insert(0, str(current_dir))


print("Попытка импорта модулей ЛР5")
print("-" * 50)

try:
    
    sys.path.insert(0, str(current_dir / "src"))
    
    
    from lab05.json_csv import json_to_csv, csv_to_json
    from lab05.csv_xlsx import csv_to_xlsx
    
    print(" Все модули успешно импортированы")
    
except ImportError as e:
    print(f" Ошибка импорта: {e}")
    print("\nПроверьте:")
    print("1. Файл src/lab05/json_csv.py существует и содержит функции")
    print("2. Файл src/lab05/csv_xlsx.py существует и содержит функции")
    print("3. Структура директорий правильная")
    
    
    print("\nТекущая структура:")
    for root, dirs, files in os.walk("src"):
        level = root.replace("src", "").count(os.sep)
        indent = " " * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = " " * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")
    
    sys.exit(1)


print("\n" + "="*50)
print("Запуск тестов ЛР5")
print("="*50)


import json

test_data_dir = Path("data/samples")
test_data_dir.mkdir(parents=True, exist_ok=True)
output_dir = Path("data/out")
output_dir.mkdir(parents=True, exist_ok=True)


people_json = [
    {"name": "Анна", "age": 28, "city": "Москва", "job": "Инженер"},
    {"name": "Петр", "age": 35, "city": "СПб", "job": "Менеджер"},
    {"name": "Мария", "age": 22, "city": "Казань", "job": "Дизайнер"}
]

with open(test_data_dir / "people.json", "w", encoding="utf-8") as f:
    json.dump(people_json, f, ensure_ascii=False, indent=2)


people_csv = """name,age,city,job
Анна,28,Москва,Инженер
Петр,35,СПб,Менеджер
Мария,22,Казань,Дизайнер"""

with open(test_data_dir / "people.csv", "w", encoding="utf-8") as f:
    f.write(people_csv)


print("\n1. Тест JSON → CSV")
try:
    json_to_csv("data/samples/people.json", "data/out/from_json.csv")
    print("    Успешно")
except Exception as e:
    print(f"    Ошибка: {e}")

print("\n2. Тест CSV → JSON")
try:
    csv_to_json("data/samples/people.csv", "data/out/from_csv.json")
    print("    Успешно")
except Exception as e:
    print(f"    Ошибка: {e}")

print("\n3. Тест CSV → XLSX")
try:
    csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
    print("    Успешно")
except Exception as e:
    print(f"    Ошибка: {e}")