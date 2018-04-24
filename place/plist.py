'''
    Utility for column output
'''


from posix import get_terminal_size


def columns(): return get_terminal_size()[0]
def lines(): return get_terminal_size()[1]


def longest(iterable):
    counts = 0
    for i, line in enumerate(iterable):
        if len(line) > counts:
            counts = i
    return iterable[counts]


def columize(iterable, column=0):
    '''
        :param column: 0 for automatic
    '''
    if column == 0:
        pass
    if column == 1:
        return "\n".join(iterable)
    if column == 2:
        length = len(iterable)
        if (len(iterable) % 2) == 0:
            col1 = iterable[:(len(iterable) // 2)]
            col2 = iterable[(len(iterable) // 2):]
        else:
            col1 = iterable[:(len(iterable) // 2) + 1]
            col2 = iterable[(len(iterable) // 2) + 1:]
