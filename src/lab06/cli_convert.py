import argparse
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from src.lib.json_csv import json_to_csv, csv_to_json
from src.lib.csv_xlsx import csv_to_xlsx


def absoluting(path: Path | str) -> Path:
    path = Path(path)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    # if not path.exists():
    #     raise FileNotFoundError("Файл не найден")
    return path

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(
        dest="cmd"
    )  # по умолчанию активируется при запуске кода. прописывать не нужно

    p1 = sub.add_parser(
        "json2csv", help="конвертация json to csv"
    )  # Необходимо прописывать после импорта файла
    p1.add_argument(
        "-i",
        "--input",
        dest="input_file",
        help="Входной файл .json",
        required=True,
        type=str,
    )
    p1.add_argument(
        "-o",
        "--output",
        dest="output_file",
        help="Выходной .csv",
        required=True,
        type=str,
    )

    p2 = sub.add_parser(
        "csv2json", help="конвертация csv to json"
    )  # Необходимо прописывать после импорта файла
    p2.add_argument(
        "-i",
        "--input",
        dest="input_file",
        help="входной файл .csv",
        required=True,
        type=str,
    )
    p2.add_argument(
        "-o",
        "--output",
        dest="output_file",
        help="конечный файл .json",
        required=True,
        type=str,
    )

    p3 = sub.add_parser(
        "csv2xlsx", help="конвертация csv to xlsx"
    )  # Необходимо прописывать после импорта файла
    p3.add_argument(
        "-i",
        "--input",
        dest="input_file",
        help="входной файл .csv",
        required=True,
        type=str,
    )
    p3.add_argument(
        "-o",
        "--output",
        dest="output_file",
        help="выходной файл xlsx",
        required=True,
        type=str,
    )

    args = parser.parse_args()

    inf = absoluting(args.output_file)
    ouf = absoluting(args.input_file)

    if not ouf.is_file():
        parser.error(f"Указанный путь {ouf} не является файлом")

    if not inf.is_file():
        parser.error(f"Указанный путь {inf} не является файлом")

    if args.cmd == "json2csv":
        json_to_csv(absoluting(args.input_file), absoluting(args.output_file))

    if args.cmd == "csv2json":
        csv_to_json(absoluting(args.input_file), absoluting(args.output_file))

    if args.cmd == "csv2xlsx":
        csv_to_xlsx(absoluting(args.input_file), absoluting(args.output_file))


if __name__ == "__main__":
    main()