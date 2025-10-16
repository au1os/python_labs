import sys
import os
src_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, src_root)
from lib.text import normalize, tokenize, count_freq, top_n

def main():
    text = sys.stdin.readline().strip()
    if not text:
        print('Всего слов: 0')
        print('Уникальных слов: 0')
        print('Топ-5:')
        return
    
    print(f'Всего слов: {len(tokenize(text))}')
    print(f'Уникальных слов: {len(count_freq(tokenize(text)))}')
    print('Топ-5:')
    for variable, freq in top_n(count_freq(tokenize(text)), 5):
        print(f'      {variable}:    {freq}')
main()