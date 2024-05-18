#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Продолжая тему предыдущего упражнения, в тех же операционных
системах на базе Unix обычно есть и утилита с названием tail,
которая отображает последние десять строк содержимого файла,
имя которого передается в качестве аргумента командной строки.
Реализуйте программу, которая будет делать то же самое.
В случае отсутствия файла, указанного пользователем,
или аргумента командной строки вам нужно вывести соответствующее  сообщение
"""

import sys


def tail(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            sentences = file.readlines()

        if len(sentences) > 10:
            for sentence in sentences[-10:]:
                print(sentence, end="")
        else:
            for sentence in sentences:
                print(sentence, end="")

    except FileNotFoundError:
        print(f"File {filename} not found")


def main():
    if len(sys.argv) != 2:
        print("Использование: python indv2.py <имя_файла>")
    else:
        tail(sys.argv[1])


if __name__ == "__main__":
    main()
