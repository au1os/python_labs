from pathlib import Path
import sys
import csv
from collections import Counter
import os

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from src.lib.text import normalize, tokenize


def ensure_parent_dir(path: str | Path) -> None:
    path.parent.mkdir(
        parents=True, exist_ok=True
    )  # создаю родительские директории (Parents=True)/ НЕ вызываю ошибку при их отсуцтвии (exist_ok=True)


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    path = Path(path)
    if path.suffix != ".txt":
        raise TypeError("Неверный тип файла")
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    try:
        with open(path, "r", newline="", encoding=encoding) as file:
            in_file = str(file.read())
            if in_file == None:
                raise ValueError(f"Файл пуст")
        return normalize(in_file)
    except UnicodeDecodeError:
        print("Ошибка декодирования файла")

    if not path.is_file():
        raise ValueError(f"Указанный путь не является файлом")


# print({Path.cwd()})
# for item in Path.cwd().iterdir():
#     print(f"  {item.name}")
# print(read_text(Path("data") / "input.txt"))

# def ensure_parent_dir(path: str | Path) -> None:
#     if


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    path = Path(path)
    ensure_parent_dir(path)
    len_form = len(rows[0])
    # print("len_form ---->",len_form)
    # print("len(header) ---->",len(header))
    # if len(header) != len_form:
    #     raise ValueError(f"Длина заголовка ({len(header)}) не соответствует длине строк данных")
    for x in rows:
        if len_form != len(x):
            raise ValueError("Ошибка чтения файла")
            break
    with open(path, "w", newline="", encoding="utf-8") as file:
        if header is not None:
            csv.writer(file, delimiter=",").writerow(header)
        # print(rows)
        csv.writer(file, delimiter=",").writerows(rows)
    print("файл создан/изменен")


def frequencies_from_text(text: str) -> dict[str, int]:
    if text == None:
        raise ValueError("Текст не должен быть пустой строкой")
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    if not freq:
        raise ValueError("Словарь частот не может быть пустым")
    if not isinstance(freq, dict):
        raise TypeError("Аргумент freq должен быть словарем")
    for key, val in freq.items():
        if not isinstance(key, str):
            raise TypeError(f"Ключи словаря должны быть строками")
        if not isinstance(val, int):
            raise TypeError(f"Значения словаря должны быть целыми числами")
        if val < 0:
            raise ValueError(f"Частота не может быть отрицательной")
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
