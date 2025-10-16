import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold == True: text = text.casefold()
    if yo2e == True: text = text.replace("ё", "е")
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
        freq_dict [f'{text}'] = tokens.count(text)
    return freq_dict
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    dict_items_sorted = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return dict_items_sorted[:n]