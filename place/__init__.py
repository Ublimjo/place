'''
    All thing you need for interaction with the terminal output
'''


from posix import get_terminal_size

columns = column = lambda: get_terminal_size()[0]
lines = line = lambda: get_terminal_size()[1]
