#!/usr/bin/env python3

"""
Написать код с помощью регулярных выражений проверку пароля пользователя. Пароль должен быть длиной от 8 до 20 символов, содержать буквы в нижнем и вверхнем регистре, а также содержать цифры.

Т.е. пароль должен:
 - Иметь строго более 7 но менее 21 символа
 - Содержать хотя бы 1 символ в верхнем регистре
 - Содержать хотя бы 1 символ в нижнем регистре
 - Содержать хотя бы 1 цифровой символ
"""
import re


def password_checker(passwd):
    if not (7 < len(passwd) < 21):
        return False

    UPPER = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    LOWER = set('abcdefghijklmnopqrstuvwxyz')
    DIGITS = set('1234567890')
    for test_set in UPPER, LOWER, DIGITS:
        for letter in passwd:
            if letter in test_set:
                break
        else:
            return False
    return True


def password_checker_re(passwd):
    passwd_re = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,20}$')
    return True if passwd_re.match(passwd) else False


# Tests

import unittest


class TestPasswordChecker(unittest.TestCase):

    def setUp(self):
        self.correct_passwords = [
                'Right Passw0rd',
                'Aa1aaaaa',                 # 8 symbols
                'aaaa aaaa aaaa aaA1a',     # 20 symbols
            ]
        self.incorrect_passwords = [
                'wrong password',
                'A1aaaaa',                  # to low, need at least 8 symbols
                'A1aa aaaa aaaa aaaa a',    # > 20 symbols
                'Aaaaaaaaa',                # do not have numbers
                'a1aaaaaaa',                # do not have uppercase letters
                'A1AAAAAAA',                # do not have lowercase letters
            ]

    def test_correct_passwords(self):
        for p in self.correct_passwords:
            self.assertTrue(password_checker(p), 'Failed on ' + p)

    def test_incorrect_passwords(self):
        for p in self.incorrect_passwords:
            self.assertFalse(password_checker(p), 'Failed on ' + p)

    def test_correct_passwords_re(self):
        for p in self.correct_passwords:
            self.assertTrue(password_checker_re(p), 'Failed on ' + p)

    def test_incorrect_passwords_re(self):
        for p in self.incorrect_passwords:
            self.assertFalse(password_checker_re(p), 'Failed on ' + p)


if __name__ == '__main__':
    unittest.main()
