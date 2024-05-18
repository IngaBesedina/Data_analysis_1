#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    word = input()

    with open("text.txt", "r") as text:
        sentences = text.readlines()

    for sentence in sentences:
        if word in sentence:
            print(sentence)
