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
import json


def required_keys(list=None):
    def wrapper(fn):
        def wrapped(data, *args, **kwargs):
            if type(data) is not dict:
                return None
            if list:
                for key in list:
                    if not key in data:
                        return None
            return fn(data, *args, **kwargs)
        return wrapped
    return wrapper



@required_keys(['phone', 'token'])
def foo(data):
    return json.dumps(data)



if __name__ == '__main__':
    data_correct = {
        "phone": "898989",
        "token": "123123123",
        "bob": "Eva"
    }
    data_bad1 = {
        "bob": "Eva",
        "token": "123123123",
    }
    data_bad2 = ['898989', '123123123', 'Eva']

    for d in data_correct, data_bad1, data_bad2:
        print('Data:', d)
        print('Result:', foo(d))

