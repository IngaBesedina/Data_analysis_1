#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


def find_files(directory):
    txt_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))
    return txt_files


def main():
    directory = input("Введите путь к директории: ")
    if os.path.isdir(directory):
        txt_files = find_files(directory)
        if txt_files:
            print("Найдены следующие файлы с расширением .txt:")
            for file in txt_files:
                print(file)
        else:
            print("В указанной директории и ее поддиректориях не найдено файлов с расширением .txt")
    else:
        print("Указанная директория не существует")


if __name__ == "__main__":
    main()


