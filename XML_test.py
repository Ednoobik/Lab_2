import xml.dom.minidom as minidom


xml_file = open('books.xml', 'r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('book')
books_dict = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == 'author':
                if child.firstChild.nodeType == 3:
                    author = child.firstChild.data
            if child.tagName == 'title':
                if child.firstChild.nodeType == 3:
                    title = child.firstChild.data
    books_dict[title] = author

    print(node.getElementsByTagName('title')[0].firstChild.data)

# for key in books_dict.keys():
#     print(key, books_dict[key])

xml_file.close()