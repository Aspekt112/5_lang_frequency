# -*- coding: utf-8 -*-

import os
import re
from collections import OrderedDict


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    splited_text = text.split()
    words = set(splited_text)
    counts = {}
    for word in words:
        counts[word] = splited_text.count(word)
    ordered_counts = OrderedDict(sorted(counts.items(),
                                        key=lambda t: t[1], reverse=True))
    for count_number, count in enumerate(ordered_counts):
        print('{0} - {1}'.format(count, ordered_counts[count]))
        if count_number == 9:
            break


def clear_text(raw_text):
    return re.sub('–|\.|,|…|\[|\]|!|\?|\(|\)|«|»|;|:|[0-9]|', '', raw_text)


if __name__ == '__main__':
    path = str(input('Введите путь к файлу: '))
    text = load_data(path)
    if text is None:
        print('Файл не найден. См. пример использования.')
    else:
        cleared_text = clear_text(text)
        get_most_frequent_words(cleared_text)
