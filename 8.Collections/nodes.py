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