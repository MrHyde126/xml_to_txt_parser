**Постановка задачи**:
Представим, что есть директория, в которой хранятся xml файлы (в директории может быть сколько угодно поддиректорий, в каждой из которых также могут быть вложенные директории, то есть уровень вложенности не ограничен, а также могут быть и другие типы файлов помимо xml). Каждый xml файл состоит из тегов node с полем type. Поле type может принимать значения:

1. RIL_TEXTLINE – текстовое поле
2. RIL_WORD – слово

Вам необходимо создать директорию с той же структурой, что и исходная и сохраняя именование файлов (то есть, если вы обрабатываете файл 1.xml, то выходной файл называть 1.txt, он должен лежать в том же месте директории, где и соответствующий xml) для каждого xml файла в директории склеить все, что находится в рамках одного текстового поля через пробел, а также убрать все знаки препинания и цифры. Текстовые поля между собой склеивать символом новой строки.

**Пример**:
Имеется директория data со структурой:

- doc1.xml
- subfolder1
  - image.png
- subfolder2
  - doc1.xml
  - script1.py
  - subfolder1
    - doc1.xml
    - doc2.xml
    - image.png

Вам нужно получить директорию с такой структурой:

- doc1.txt
- subfolder1
- subfolder2
  - doc1.txt
  - subfolder1
    - doc1.txt
    - doc2.txt

В каждом txt лежит требуемое содержимое в соответствии с xml файлом