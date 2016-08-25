#!/usr/bin/env python3

"""
Написать код с помощью регулярных выражений проверку пароля пользователя. Пароль должен быть длиной от 8 до 20 символов, содержать буквы в нижнем и вверхнем регистре, а также содержать цифры.

Т.е. пароль должен:
 - Иметь строго более 7 но менее 21 символа
 - Содержать хотя бы 1 символ в верхнем регистре
 - Содержать хотя бы 1 символ в нижнем регистре
 - Содержать хотя бы 1 цифровой символ
"""

def password_checker(passwd):
    pass
    return True

def password_checker_re(passwd):
    pass
    return True

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
                'A1aaaaa',                  # to low, need at least 8 symbols
                'A1aa aaaa aaaa aaaa a',    # > 20 symbols
                'Aaaaaaaaa',                # do not have numbers
                'a1aaaaaaa',                # do not have uppercase letters
                'A1AAAAAAA',                # do not have lowercase letters
            ]

    def test_correct_passwords(self):
        for p in self.correct_passwords:
            self.assertTrue(password_checker(p))

    def test_incorrect_passwords(self):
        for p in self.incorrect_passwords:
            self.assertFalse(password_checker(p))

    def test_correct_passwords_re(self):
        for p in self.correct_passwords:
            self.assertTrue(password_checker_re(p))

    def test_incorrect_passwords_re(self):
        for p in self.incorrect_passwords:
            self.assertFalse(password_checker_re(p))


if __name__ == '__main__':
    unittest.main()
