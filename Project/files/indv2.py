#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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


