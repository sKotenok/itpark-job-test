#!/usr/bin/env python3
"""
Имеется следующая выборка из БД.
id | node_id | node_name | type | name | min | max | title_label
...

Необходимо сформировать объект:

{
  "21":[
    {
      "node_name":"ZP3111-5 4-in-1",
      "type":"sensor",
      "name":"Luminance"
    },
    {
      "node_name":"ZP3111-5 4-in-1",
      "type":"sensor",
      "name":"Relative Humidity"
    },
    {
      "node_name":"ZP3111-5 4-in-1",
      "type":"sensor",
      "name":"Temperature"
    }
  ],
  "23":[
    {
      "node_name":"ZP3111-5 4-in-1",
      "type":"sensor",
      "name":"Luminance"
    },
    {
      "node_name":"ZP3111-5 4-in-1",
      "type":"sensor",
      "name":"Relative Humidity"
    },
    {
      "node_name":"ZP3111-5 4-in-1",
      "type":"sensor",
      "name":"Temperature"
    }
  ]
}

Продолжите/измените код:

for row in query:
    node_id = row.node_id
    node_name = row.node_name
    type = row.type

"""

class Row:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value

query = [
    Row(id=5, node_id=21, node_name='ZP3111-5 4-in-1', name='Luminance', type='sensor'),
    Row(id=3, node_id=21, node_name='ZP3111-5 4-in-1', name='Relative Humidity', type='sensor'),
    Row(id=1, node_id=23, node_name='ZP3111-5 4-in-1', name='Luminance', type='sensor'),
]

output = {}


for row in query:
    node_id = row.node_id

    if node_id not in output:
        output[node_id] = []

    output[node_id].append({
        'node_name': row.node_name,
        'name': row.name,
        'type': row.type
    })


from pprint import pprint
pprint(output)
