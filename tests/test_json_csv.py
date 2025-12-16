import csv
import json
from pathlib import Path
import pytest

from src.lib.json_csv import csv_to_json, json_to_csv


def test_json_to_csv_basic(tmp_path: Path):
    start = tmp_path / "people.json"
    end = tmp_path / "people.csv"

    data = [
        {"Name": "Emily", "Surname": "Johnson", "Age": "24"},
        {"Name": "Daniel", "Surname": "Williams", "Age": "31"},
    ]
    start.write_text(json.dumps(data, ensure_ascii=False, indent=3), encoding="utf-8")
    json_to_csv(start, end)

    with end.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"Name", "Surname", "Age"} <= set(rows[0].keys())
    assert rows[0]["Name"] == "Emily"
    assert rows[0]["Surname"] == "Johnson"
    assert rows[0]["Age"] == "24"
    assert rows[1]["Name"] == "Daniel"
    assert rows[1]["Surname"] == "Williams"
    assert rows[1]["Age"] == "31"


def test_json_to_csv_file_not_found(tmp_path: Path):
    src = tmp_path / "nonexistent.json"
    dst = tmp_path / "output.csv"

    with pytest.raises(FileNotFoundError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_multiple_fields(tmp_path: Path):
    src = tmp_path / "data.json"
    dst = tmp_path / "data.csv"

    data = [
        {"id": "1", "name": "Olegator", "city": "Moscow", "salary": "54000"},
        {"id": "2", "name": "Jane", "city": "Paris", "salary": "61200"},
        {"id": "3", "name": "Jack", "city": "London", "salary": "55300"},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 3
    assert {"id", "name", "city", "salary"} <= set(rows[0].keys())


def test_json_to_csv_cyrillic(tmp_path: Path):
    src = tmp_path / "russian.json"
    dst = tmp_path / "russian.csv"

    data = [
        {"имя": "Алексей", "возраст": "30"},
        {"имя": "Мария", "возраст": "28"},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert rows[0]["имя"] == "Алексей"
    assert rows[1]["имя"] == "Мария"


def test_json_to_csv_invalid_json(tmp_path: Path):
    src = tmp_path / "invalid.json"
    dst = tmp_path / "output.csv"

    src.write_text("{ this is not valid json }", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_empty_file(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "output.csv"

    src.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError, match="Нет данных"):
        json_to_csv(str(src), str(dst))


# def test_json_to_csv_wrong_extension(tmp_path: Path):

#     src = tmp_path / "empty.txt"
#     dst = tmp_path / "output.csv"

#     with pytest.raises(TypeError, match="Неверный тип файла"):
#         json_to_csv(str(src), str(dst))


def test_json_to_csv_wrong_csv_extension(tmp_path: Path):
    src = tmp_path / "file.json"
    dst = tmp_path / "output.txt"

    src.write_text('[{"name": "test"}]', encoding="utf-8")

    with pytest.raises(TypeError, match="Неверный тип файла"):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_memply(tmp_path: Path):
    src = tmp_path / "data.json"
    dst = tmp_path / "data.csv"

    data = []
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    with pytest.raises(ValueError, match="Нет данных"):
        json_to_csv(str(src), str(dst))


def test_csv_to_json_basic(tmp_path: Path):

    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "22"})
        writer.writerow({"name": "Bob", "age": "25"})

    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["name"] == "Alice"
    assert data[0]["age"] == "22"
    assert data[1]["name"] == "Bob"
    assert data[1]["age"] == "25"


def test_csv_to_json_multiple_fields(tmp_path: Path):
    src = tmp_path / "data.csv"
    dst = tmp_path / "data.json"

    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "city", "salary"])
        writer.writeheader()
        writer.writerow(
            {"id": "1", "name": "John", "city": "Moscow", "salary": "50000"}
        )
        writer.writerow({"id": "2", "name": "Jane", "city": "Paris", "salary": "60000"})

    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert set(data[0].keys()) == {"id", "name", "city", "salary"}


def test_csv_to_json_cyrillic(tmp_path: Path):
    src = tmp_path / "russian.csv"
    dst = tmp_path / "russian.json"

    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["имя", "возраст"])
        writer.writeheader()
        writer.writerow({"имя": "Алексей", "возраст": "30"})
        writer.writerow({"имя": "Мария", "возраст": "28"})

    csv_to_json(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["имя"] == "Алексей"
    assert data[1]["имя"] == "Мария"


def test_csv_to_json_file_not_found(tmp_path: Path):
    src = tmp_path / "nonexistent.csv"
    dst = tmp_path / "output.json"

    with pytest.raises(FileNotFoundError):
        csv_to_json(str(src), str(dst))


def test_csv_to_json_empty_file(tmp_path: Path):
    src = tmp_path / "empty.csv"
    dst = tmp_path / "output.json"

    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="пуст"):
        csv_to_json(str(src), str(dst))


def test_csv_to_json_only_header(tmp_path: Path):
    src = tmp_path / "header_only.csv"
    dst = tmp_path / "output.json"

    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()

    with pytest.raises(ValueError, match="Нет данных"):
        csv_to_json(str(src), str(dst))


# def test_csv_to_json_wrong_extension(tmp_path: Path):

#     src = tmp_path / "file.txt"
#     dst = tmp_path / "output.json"

#     with pytest.raises(TypeError, match="Неверный тип файла"):
#         csv_to_json(str(src), str(dst))


def test_csv_to_json_wrong_json_extension(tmp_path: Path):
    src = tmp_path / "file.csv"
    dst = tmp_path / "output.txt"

    src.write_text("name,age\ntest,25", encoding="utf-8")

    with pytest.raises(TypeError, match="Неверный тип файла"):
        csv_to_json(str(src), str(dst))
