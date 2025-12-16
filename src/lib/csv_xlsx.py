from openpyxl import Workbook
from pathlib import Path
import csv, sys
PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from src.lib.f_read_to_write import r_json, r_csv




def csv_to_xlsx(csv_path: str | Path, xlsx_path: str | Path) -> None:
    csv_data = r_csv(csv_path)
    mas = []
    lis = []
    for key in csv_data[0].keys():
        lis.append(str(key))
    mas.append(lis)
    lis = []
    for row in csv_data:
        for key in csv_data[0].keys():
            lis.append(row[key])
        mas.append(lis)
        lis = []
    with open(csv_path, encoding="utf-8") as file:
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"
        for row in mas:
            ws.append(row)
        wb.save(xlsx_path)
