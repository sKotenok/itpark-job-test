#!/usr/bin/env python3

"""
Реализовать скрипт, принимающий в качестве аргумента строку, и удаляющий из данной строки незакрые скобки вместе с их содержимым, если после них нет закрытых блоков. Пример: qlqksq((ewwe)(pll -> qlqksq((ewwe).

Обязательно:
    Наличие тестов для кода.
    Логирование входящих аргументов и результата.
    Реализация в двух вариантах: с помощью регулярных выражений и без них.


Т.е. если после серии открывающих скобок нет хотя бы 1й закрывающей - удаляем всё до конца строки.
"""
# Code
import re

def del_unpaired_brackets(input_str):
    str_end = False
    for i, s in enumerate(input_str):
        if str_end:
            if s == ')':
                str_end = False
        elif s == '(':
            str_end = i
    result = input_str[0:str_end] if str_end else input_str
    return result


def del_unpaired_brackets_re(input_str):
    brackets_re = re.compile(r'(?:(?:\((?=.*\)))|[^\(])*')
    result = brackets_re.match(input_str)
    return result.group() if result else ''


# Tests.

import unittest

class TestDelUnpairedBrackets(unittest.TestCase):

    def setUp(self):
        self.strings = {
            '' : '',
            'a b c': 'a b c',
            '()()': '()()',
            ')()': ')()',
            '()(': '()',
            'qlqksq((ewwe)(pll': 'qlqksq((ewwe)',
            '(abc)(def)(((lsd) (be(fd(fd': '(abc)(def)(((lsd) ',
        }

    def test_del_unpaired_brackets(self):
        for input, result_need in self.strings.items():
            result_real = del_unpaired_brackets(input)
            self.assertEqual(result_need, result_real,
                    'Failed on {0} Need: {1} Return: {2}'.format(input, result_need, result_real))

    def test_del_unpaired_brackets_re(self):
        for input, result_need in self.strings.items():
            result_real = del_unpaired_brackets(input)
            self.assertEqual(result_need, result_real,
                    'Failed on {0} Need: {1} Return: {2}'.format(input, result_need, result_real))


if __name__ == '__main__':
    unittest.main()
