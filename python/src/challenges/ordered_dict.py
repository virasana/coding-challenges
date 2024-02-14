from collections import OrderedDict


def get_prices(N, data):
    dictionary = OrderedDict()

    for datum in data:
        item, price = datum.rsplit(maxsplit=1)
        dictionary[item] = dictionary.get(item, 0) + int(price)
    
    return dictionary


input = """\
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30\
"""

N, data = input[0], input[1:].strip().split('\n')
dictionary = get_prices(N, data)
for item in dictionary.items():
        print(*item)