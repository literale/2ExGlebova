#!/usr/bin/python3

"""Упражнение "Количество слов"

Функция main() ниже уже определена и заполнена. Она вызывает функции 
print_words() и print_top(), которые вам нужно заполнить.

1. Если при вызове файла задан флаг --count, вызывается функция 
print_words(filename), которая подсчитывает, как часто каждое слово встречается 
в тексте и выводит:
слово1 количество1
слово2 количество2
...

Выводимый список отсортируйте в алфавитном порядке. Храните все слова 
в нижнем регистре, т.о. слова "Слон" и "слон" будут обрабатываться как одно 
слово.

2. Если задан флаг --topcount, вызывается функция print_top(filename),
которая аналогична функции print_words(), но выводит только топ-20 наиболее 
часто встречающихся слов, таким образом первым будет самое часто встречающееся 
слово, за ним следующее по частоте и т.д.

Используйте str.split() (без аргументов), чтобы разбить текст на слова.

Отсекайте знаки припинания при помощи str.strip() с знаками припинания 
в качестве аргумента.

Совет: не пишите всю программу сразу. Доведите ее до какого-то промежуточного 
состояния и выведите вашу текущую структуру данных. Когда все будет работать 
как надо, перейдите к следующему этапу.

Дополнительно: определите вспомогательную функцию, чтобы избежать дублирования 
кода внутри print_words() и print_top().

"""

import sys
from string import punctuation
import operator
# +++ваш код+++
# Определите и заполните функции print_words(filename) и print_top(filename).
# Вы также можете написать вспомогательную функцию, которая читает файл,
# строит по нему словарь слово/количество и возвращает этот словарь.
# Затем print_words() и print_top() смогут просто вызывать эту вспомогательную функцию.


def count_word(filename):
    big_str_file = open(filename, "r", encoding="utf-8").read()
    big_str_file = big_str_file.lower()
    # удаляем пунктуацию
    big_str_file = ''.join(ch for ch in big_str_file if ch not in punctuation)
    big_list_file = big_str_file.split()
    diction = {str: int}

    for word in big_list_file:   # возможно можно не через трайкетч, но я не нашла как
        try:
            diction[word] += 1
        except KeyError:
            diction[word] = 1

    return diction


def print_words(filename):
    diction = count_word(filename)
    i = 0
    for keys in diction:
        print(i, keys, ": ", diction[keys])
        i+=1

    return diction


def print_top(filename):
    diction = count_word(filename)
    top = {str: int}
    sorted_d = sorted(diction.items(), key=lambda x: str(x[1]), reverse=True)
    for i in range(21):
        top[sorted_d[i][0]] = sorted_d[i][1]

    i = 1
    for keys in top:
        if type(keys) == str:   # что бы не выводило str: int
            print(i, keys, ": ", top[keys])
            i += 1

    return top
###

# Это базовый код для разбора аргументов коммандной строки.
# Он вызывает print_words() и print_top(), которые необходимо определить.


def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
    sys.exit(1)


if __name__ == '__main__':
    main()
