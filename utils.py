import re
import xml.etree.ElementTree as ET


def clean_text(text: str) -> str:
    """Очищает текст от знаков препинания и цифр."""
    clean_text = re.sub('[^a-zA-Zа-яА-Я]+', '', text)
    return clean_text


def parse_xml(in_file: str, out_file: str) -> None:
    """Преобразует XML в текстовый файл."""
    in_file = open(in_file, encoding='utf-8')
    xml = '<root>' + in_file.read() + '</root>'
    in_file.close()
    root = ET.fromstring(xml)

    with open(out_file, 'w') as out_file:
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
