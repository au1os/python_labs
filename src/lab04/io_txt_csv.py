import os
import sys
import csv
from pathlib import Path
from typing import Iterable, Sequence, Union, Tuple, List
from collections import Counter
src_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, src_root)
from lib.text import normalize, tokenize, count_freq, top_n
def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    # Вторым параметром в функции можно указать желаемую кодировку
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    if path.suffix != '.txt':
        raise ValueError("Неправильно расширение файла")
    try:
        with open(path,"r",newline="",encoding=encoding) as file:
            in_file=str(file.read())
        return normalize(in_file)
    except UnicodeDecodeError: 
        print("Ошибка декодировки")
        raise
def write_csv(rows: Iterable[Sequence], path: str | Path, header: Union[Tuple[str, ...], None]) -> None:
    p = Path(path)
    rows = list(rows)
    for i in range(len(rows)):  
        if len(rows[0]) != len(rows[i]):
            raise ValueError("Строки разной длины")
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=',')
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like
def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))