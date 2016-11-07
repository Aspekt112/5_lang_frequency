# -*- coding: utf-8 -*-

import os
import re
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text, re.UNICODE)
    return Counter(words)


if __name__ == '__main__':
    path = str(input('Введите путь к файлу: '))
    text = load_data(path)
    if text is None:
        print('Файл не найден. См. пример использования.')
    else:
        words_count = get_most_frequent_words(text).most_common(10)

        for word, count in words_count:
            print('{0} {1}'.format(
                word.ljust(10, '.'),
                count)
            )
