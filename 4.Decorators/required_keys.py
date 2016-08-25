#!/usr/bin/env python3

"""
Имеется функция:

def foo(data):
    return json.dumps(data)

Напишите декоратор к функции который проверит что объект dataявляется dict.

Декоратор должен иметь параметр объект list, где указывается ключи, которые должен обязательно иметь объект data.

В противной случае, функция должна возвращать None.

Пример:

@required_keys(['phone', 'token'])
def foo(data):
    return json.dumps(data)

"""

