from io_txt_csv import read_text, write_csv, frequencies_from_text, sorted_word_counts
import csv
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from src.lib.text import text_stats, tokenize, top_n, count_freq


the_way = Path(input("Путь к файлу: "))
enc = input("Желаемая кодировка: ")
work_str = read_text(the_way, encoding=enc)
print(text_stats(work_str, False))
write_csv(
    top_n(count_freq(tokenize(work_str))),
    "data002/lab004/report.csv",
    ("word", "count"),
)
