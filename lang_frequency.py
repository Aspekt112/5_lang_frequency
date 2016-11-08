# -*- coding: utf-8 -*-

import os
import re
import argparse
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
    parser = argparse.ArgumentParser(description='Принимает текстовый файл в качестве аргумента '
                                                 'и выводит 10 самых популярных слов в нем.')
    parser.add_argument('-f', '--filepath',
                        type=str,
                        required=True,
                        help='Путь до файла.')

    args = parser.parse_args()

    text = load_data(args.filepath)
    if text is None:
        print('Файл не найден. См. пример использования.')
    else:
        words_count = get_most_frequent_words(text).most_common(10)

        for word, count in words_count:
            print('{0} {1}'.format(
                word.ljust(10, '.'),
                count)
            )
