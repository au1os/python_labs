import json, csv, sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from src.lib.f_read_to_write import r_csv, w_csv, r_json, w_json




def json_to_csv(json_path: str | Path, csv_path: str | Path) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)
    if json_path.stat().st_size == 0:
        raise ValueError("Файл пуст")
    if json_path.suffix != ".json":
        raise TypeError("Неверный тип файла: Исходный файл должен быть типа .json")
    if csv_path.suffix != ".csv":
        raise TypeError("Неверный тип файла: Файл на выхлопе должен быть типа .csv")
    if not json_path.exists():
        raise FileNotFoundError("json файл не найден")
    read_t_json = r_json(json_path)
    w_csv(read_t_json, csv_path)
    print("json_to_csv: Данные записаны")




def csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    json_path = Path(json_path)
    csv_path = Path(csv_path)
    if csv_path.stat().st_size == 0:
        raise ValueError("файл пуст")
    if csv_path.suffix != ".csv":
        raise TypeError("Неверный тип файла: Исходный файл должен быть типа .csv")
    if json_path.suffix != ".json":
        raise TypeError("Неверный тип файла: Файл на выхлопе должен быть типа .json")
    if not csv_path.exists():
        raise FileNotFoundError("Файл не найден")
    read_t_csv = r_csv(csv_path)
    w_json(read_t_csv, json_path)
    print("csv_to_json: Данные записаны")