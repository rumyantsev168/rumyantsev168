import time

def text_art(string):
    for i in range(len(string) + 1):
        print('\b' * len(string), end='')
        print(string[:i], '_' * (len(string) - i), sep='', end='')
        time.sleep(0.25)
