#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Написать программу, которая считывает текст из файла и выводит на экран только
предложения, содержащие введенное с клавиатуры слово.
"""

if __name__ == "__main__":
    word = input()

    with open("text.txt", "r") as text:
        sentences = text.readlines()

    for sentence in sentences:
        if word in sentence:
            print(sentence)
