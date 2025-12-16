import re
import sys


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold == True:
        text = text.casefold()
    if yo2e == True:
        text = text.replace("ё", "е")
    for space in ['\n', '\t', '\r', '\v', '\f']:
        text = text.replace(space, ' ')
    return ' '.join(text.split())


def tokenize(text: str) -> list[str]:
    text = normalize(text)
    return re.findall(r'\w+(?:-\w+)*', text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    unique = set(tokens)
    freq_dict = {}
    for text in unique:
        freq_dict[f'{text}'] = tokens.count(text)
    return freq_dict


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    dict_items_sorted = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return dict_items_sorted[:n]


def text_stats(inp: str, flag: bool) -> str:
    print(f'Всего слов: {len(inp.split())}')
    print(f'Уникальных слов: {len(set(inp.split()))}')
    mas = tokenize(normalize(inp))
    # inp=normalize(inp,1,1)
    # print(inp)
    if flag:
        par_1 = max([len(x) for x in mas])
        # print(par_1)
        # print(par_1)
        # print(top_n(count_freq(inp.lower().split()))[0][0])
        if par_1 > 5:
            print("слово", " " * abs(par_1 - 5), "|", "частота")
        elif par_1 < 5:
            print("слово", " |", "частота")
            par_1 = 5
        print("-" * (par_1 + abs(par_1 - 5) + 3))
        # print(tokenize(inp))
        n = 5
        x = 0
        if len(top_n(count_freq(mas))) < 5:
            n = len(top_n(count_freq(mas)))
        for i in top_n(count_freq(mas)):
            if x == n:
                break
            print(f'{i[0]} {" "*(par_1-len(i[0]))} | {i[1]}')
            x += 1
    else:
        print("Топ 5:")
        x = 0
        n = 5
        if len(top_n(count_freq(mas))) < 5:
            n = len(top_n(count_freq(mas)))
        while x < n:
            i = top_n(count_freq(mas))[x]
            print(f'{i[0]}: {i[1]}')
            x += 1
