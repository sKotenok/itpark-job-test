#!/usr/bin/env python3

"""
В директории /opt/data содержатся N количество файлов. example1.xml example12.xml .... exampleN.xml.

Необходимо запустить количество thread-ов соответсвующее количеству файлов в директории.

Пример файла файл

Каждый thread должен распарсить файл и сформировать объект следующей структуры:

{
  "gateway_id": "A8F7E0128EDE",
  "node":[
    {
     "node_id": 36,
     "Temperature": 27.88,
     "Luminance": 100.00,
     "Relative Humidity": 48.49
    }
    ]
}

Ключи и значения объекта массива node (кромер node_id ) формируются из тега value, имеющиего атрибут genre="user".

Каждый thread должен выполнить POST запрос на https://swfdev.com/ с передачей данного объекта.
"""

