#!/usr/bin/env python3

"""
В директории /opt/data содержатся N количество файлов. example1.xml example12.xml .... exampleN.xml.

Необходимо запустить количество thread-ов соответсвующее количеству файлов в директории.

Пример файла файл example.xml

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

#

PATH = 'files' # '/opt/data'
SERVER = 'http://127.0.0.1' # https://swfdev.com/


import os, sys
import json
import threading
import urllib
from xml.etree import ElementTree


if sys.version_info > (3, 0):
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen

    def get_xml_files(path):
        # Python3 version with scandir
        files = os.scandir(path)
        return [f.path for f in files if f.is_file() and f.name.lower().endswith('.xml')]

else:
    from urllib import urlencode
    from urllib2 import Request, urlopen

    def get_xml_files(path):
        # Python2 version
        files = os.listdir(path)
        result = []
        for f_name in files:
            f = os.path.join(path, f_name)
            if os.path.isfile(f) and os.path.splitext(f)[-1].lower() == '.xml':
                result.append(f)
        return result


def parse_gateway_nodes(xml_file, config):
    """Парсит xml-файл, возвращает словарь в заданном формате"""
    xml_obj = ElementTree.parse(xml_file)
    root = xml_obj.getroot()
    if root.tag != 'poll':
        return False
    result = {
        'gateway_id': root.get('gateway_id'),
        'node': [],
    }
    for node in root.findall('node'):
        node_dict = {}
        for value in node:
            node_dict['node_id'] = node.get('id')
            if value.tag == 'value' and value.get('genre') == 'user':
                node_dict[value.get('label')] = value.text
        result['node'].append(node_dict)
    return result


def send_gateway_nodes(serializable_data, config):
    """Отправляет данные на заданный URL"""
    uri = config['uri'] if 'uri' in config else 'http://127.0.0.1'

    ## Точно не знаю, JSON отправлять или обычный POST, поэтому можно задать в конфиге.
    content_type = config['content-type'] if 'content-type' in config else 'application/json'

    if content_type == 'application/json':
        data_str = json.dumps(serializable_data).encode('utf8')
    else:
        data_str = urlencode(serializable_data)

    req = Request(uri, data_str, headers={'content-type': content_type})
    urlopen(req)



class ParseThread(threading.Thread):
    def __init__(self, xml_file, parser_func, sender_func, config):
        super(ParseThread, self).__init__()
        self.xml_file = xml_file
        self.parser_func = parser_func
        self.sender_func = sender_func
        self.config = config

    def run(self):
        parsed_data = self.parser_func(self.xml_file, self.config)
        self.sender_func(parsed_data, self.config)



def main():
    xml_files = get_xml_files(PATH)
    config = {
        'uri': SERVER,
    }

    threads = []
    for f in xml_files:
        t = ParseThread(f, parse_gateway_nodes, send_gateway_nodes, config)
        t.start()
        threads.append(t)

    # wait all threads to complete
    for t in threads:
        t.join()
    print('All job is finished')


if __name__ == '__main__':
    main()
