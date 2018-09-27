#!/usr/bin/python3

"""Имитация текста

Прочитайте файл, указанный в командной строке.
Используйте str.split() (без аргументов) для получения всех слов в файле.
Вместо того, чтобы читать файл построчно, проще считать
его в одну гигантскую строку и применить к нему split() один раз.

Создайте "имитационный" словарь, который связывает каждое слово
со списком всех слов, которые непосредственно следуют за этим словом в файле.
Список слов может быть в любом порядке и должен включать дубликаты. 

Так, например, для текста "Привет, мир! Привет, Вселенная!" мы получим такой
имитационный словарь:
{'': ['Привет,'], 'Привет,': ['мир!', 'Вселенная!'], 'мир!': ['Привет,']}
Будем считать, в качестве ключа для первого слова в файле используется пустая строка.

С помощью имитационного словаря довольно просто генерировать случайные тексты, 
имитирующие оригинальный. Возьмите слово, посмотрите какие слова могут за ним, 
выберите одно из них наугад, выведите его и используйте это слово 
в следующей итерации.

Используйте пустую строку в качестве ключа для первого слова.
Если вы когда-нибудь застрянете на слове, которого нет в словаре,
вернетесь к пустой строке, чтобы продолжать генерацию текста.

Примечание: стандартный python-модуль random включает в себя метод 
random.choice(list), который выбирает случайный элемент из непустого списка.

"""

import random
import sys
from typing import List


def mimic_dict(filename):
    """Возвращает имитационный словарь, сопоставляющий каждое слово 
    со списом слов, которые непосредственно следуют за ним в тексте"""
    # +++ваш код+++
    big_str_file = open(filename, "r", encoding="utf-8").read()
    big_list_file = big_str_file.split()
    diction = {" ": big_list_file[0]}

    for word in big_list_file:   # пытаемся удалить лишние символы (не очень успешно) #TODO плохо че
        if word == " " or word == "" or word == "/n":
            big_list_file.remove(word)

    for i in range(len(big_list_file)-2):   # составляем мимик
        word_in_d = str(big_list_file[i])
        word_a_word = str(big_list_file[i+1])
        try:
            diction[word_in_d] = diction[word_in_d] + " " + word_a_word
        except KeyError:
            diction[word_in_d] = word_a_word

    return diction


def print_mimic(mimic_dict, word):
    """Принимает в качестве аргументов имитационный словарь и начальное слово,
    выводит 200 случайных слов."""
    # +++ваш код+++
    random.seed()
    mimic_text = word

    for i in range(199):
        buf_words = str(mimic_dict.get(word))
        buf_words = buf_words.split(" ")
        r = random.randint(0, len(buf_words)-1)
        buf_word = buf_words[r]
        mimic_text = mimic_text + " " + buf_word
        word = buf_word

    print(mimic_text)
    return mimic_text


def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    d = mimic_dict(sys.argv[1])

    print_mimic(d, ' ')
    # d = mimic_dict("./alice.txt")
    # наркомания конечно выходит



if __name__ == '__main__':
    main()
