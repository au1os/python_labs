import os
import csv
from pathlib import Path
from typing import Iterable, Sequence
from lib.text import normalize
def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    # Вторым параметром в функции можно указать желаемую кодировку
    path = Path(path)
    if not path.exist():
        raise FileNotFoundError("Файл не найден")
    if path.suffix != '.txt':
        raise ValueError("Неправильно расширение файла")
    try:
        with open(path,"r",newline="",encoding=encoding) as file:
            in_file=str(file.read())
        return normalize(in_file)
    except UnicodeDecodeError: print("Ошибка декодировки")
def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)