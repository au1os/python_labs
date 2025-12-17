import pytest

from src.lib.text import count_freq, top_n, normalize, tokenize


# ----------------------------------> Normalize func. testind
@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлки", "ежик, елки"),
        ("HeLlo\r\nWorld", "hello world"),
        ("  двойные      пробелы     ", "двойные пробелы"),
        ("", ""),
        ("\n\r\t", ""),
        ("123hello", "123hello"),
        ("123", "123"),
        ("www ssss", "www ssss"),
        ("Hi, new user!", "hi, new user!"),
        ("python_labs", "python_labs"),
    ],
)
def test_normalize_main(source: str, expected: str) -> None:
    assert normalize(source) == expected


def test_normalize_NO_yo2e() -> None:
    assert normalize("ёжик, Ёлки", yo2e=False) == "ёжик, ёлки"


# def test_normalize_NO_casefold() -> None:
#     assert normalize("НунИчЕгОСеБе_ЁмАЁ", casefold=False) == "НунИчЕгОСеБе_ЕмАЕ"

# ----------------------------------> Tokenize func. testing


@pytest.mark.parametrize(
    "source, expected",
    [
        ("Дарова      Ворлд", ["дарова", "ворлд"]),
        ("Hello my      project", ["hello", "my", "project"]),
        ("my world,Hello!!!!", ["my", "world", "hello"]),
        ("python_labs saved", ["python_labs", "saved"]),
        ("привет-пока, -пока-", ["привет-пока", "пока"]),
        ("hi!\nmi\ttoo.", ["hi", "mi", "too"]),
        (
            "7fw38rf3fgw7d_ysdufhsef-ef3 3-ffwsed    ef33_few33232",
            ["7fw38rf3fgw7d_ysdufhsef-ef3", "3-ffwsed", "ef33_few33232"],
        ),
        ("", []),
        ("%^&*()!@#$", []),
    ],
)
def test_tokenize(source: str, expected: str) -> None:
    assert tokenize(source) == expected


# ----------------------------------> count_freq func. testing


@pytest.mark.parametrize(
    "source, expected",
    [
        # (["a", "a", "you", "you", "b", "b", "YOU"], {'you': 3, 'b': 2, 'a': 2}),
        # (["Hello"], {'hello': 1}),
        (
            [
                "a",
                "a",
                "a",
                "a",
                "a",
                "a",
                "a",
            ],
            {'a': 7},
        ),
        (["a", "b", "c", "d", "e"], {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}),
        # (["12", "211", "12", "A", "a"], {'a': 2, '211': 1, '12': 2}),
        ([], {}),
    ],
)
def test_count_freq_main(source: str, expected: str) -> None:
    assert count_freq(source) == expected


# ----------------------------------> top_n func. testing


@pytest.mark.parametrize(
    "source, expected",
    [
        ({'you': 3, 'b': 2, 'a': 2}, [('you', 3), ('a', 2), ('b', 2)]),
        ({'hello': 1}, [('hello', 1)]),
        ({'a': 7}, [('a', 7)]),
        (
            {'e': 1, 'd': 1, 'c': 1, 'b': 1, 'a': 1},
            [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 1)],
        ),
        ({'a': 2, '211': 1, '12': 2}, [('12', 2), ('a', 2), ('211', 1)]),
        ({}, []),
    ],
)
def test_top_n_main(source: str, expected: str) -> None:
    assert top_n(source) == expected
