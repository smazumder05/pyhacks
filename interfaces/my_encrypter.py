import sys
from encrypter_if import CharReader, CharWriter, encrypter

class MyCharReader(CharReader):
    def __init__(self):
        def get_characters():
            data = input("Enter a line to encrypt:\n")
            for line in data:
                for char in line:
                    yield char

        self.iter = get_characters()

    def read_char(self):
        return next(self.iter)

class MyCharWriter(CharWriter):
    def write_char(self, char: str):
        print(char)


my_encrypter = encrypter(MyCharReader(),MyCharWriter())
my_encrypter()
