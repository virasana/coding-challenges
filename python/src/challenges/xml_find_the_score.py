import xml.etree.ElementTree as etree

xml = """\
<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>\
"""

def get_attr_number(node):
    # l = len(node.attrib)
    # c = sum(get_attr_number(child) for child in node)
    # # c = sum(map(get_attr_number, node))
    # result = l + c
    # return result
    score = 0
    for element in node.iter():
        score += len(element.attrib)
    return score


if __name__ == '__main__':
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


