#!/usr/bin/python3
from itertools import chain
from random import choice
from string import ascii_letters, digits

from flask import jsonify


def create_uid(n=9):
    '''Génère une chaîne de caractères alétoires de longueur n
   en évitant 0, O, I, l pour être sympa.'''
    chrs = [c for c in chain(ascii_letters, digits)
            if c not in '0OIl']
    return ''.join((choice(chrs) for i in range(n)))


class Code:

    def __init__(self, uid=None, content=None, language=None):
        self.uid = uid or create_uid()
        self.content = content or '# Write your code here...'
        self.language = language or 'Plain text'

    def values(self):
        return dict(self.__dict__)

    def __str__(self):
        return str({
            "content": self.content,
            "language": self.language,
            "uid": self.uid,
        })
