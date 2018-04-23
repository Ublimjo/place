'''
    All thing you need for interaction with the terminal output
'''


from posix import get_terminal_size

columns = column = lambda: get_terminal_size()[0]
lines = line = lambda: get_terminal_size()[1]


class Tri:
    def __init__(self, now=''):
        self.now = now

    def __str__(self):
        return self.now

    def put(self, text, parag='-__'):
        length = len(text)
        if parag == '-__':
            if self.now == '':
                self.now = text
            else:
                self.now = text + self.now[length:]

        if parag == '_-_':
            centered = text.center(columns())
            start = (columns() - length) // 2
            if self.now == '':
                self.now = centered
            else:
                self.now = self.now[:start] + \
                    text + self.now[start + length:]

        if parag == '__-':
            if self.now == '':
                self.now = text.rjust(columns())
            else:
                start = (columns() - length)
                self.now = self.now[:start] + text

    def show(self):
        print(self.now)
