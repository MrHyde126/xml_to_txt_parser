import re
import xml.etree.ElementTree as ET


def clean_text(text):
    clean_text = re.sub('[^a-zA-Zа-яА-Я]+', '', text)
    return clean_text


in_file = open('data/13/output.xml', encoding='utf-8')
xml = '<root>' + in_file.read() + '</root>'
in_file.close()
root = ET.fromstring(xml)

with open('output.txt', 'w') as out_file:
    data = []
    for node in root.iter('node'):
        if node.attrib.get('type') == 'RIL_TEXTLINE':
            line = ''
            for child_none in node:
                if child_none.attrib.get('type') == 'RIL_WORD':
                    text = clean_text(child_none.text)
                    if text:
                        line += f' {text}'
            if line:
                data.append(line.lstrip())
    out_file.write('\n'.join(data))
