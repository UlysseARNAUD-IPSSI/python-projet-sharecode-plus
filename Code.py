#!/usr/bin/python3

class Code:

    def __init__(self, *, uid, code, langage):
        self.uid = uid
        self.code = code
        self.langage = langage

    def values (self):
        return self.__dict__.values()