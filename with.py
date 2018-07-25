import numpy as np
import os, sys

# case 1
# with
with open("hello.txt", 'w') as f:
    f.write('hello, woeld')
# Just like
f =open('hello.txt', 'w')
try:
    f.write('trytrytry')
finally:
    f.close()



# case 2
class ManageFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManageFile('hello.txt') as f:
    f.write('ff')
    f.write('gg')


# Case 3
from contextlib import contextmanager
@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()
# Try
with managed_file('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now!')


# Case 4: Indenter()
class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)


with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')
