#!/usr/bin/env python3

"""
Imports nécessaires
"""

import ast
import json
from string import ascii_letters, digits
from itertools import chain
from random import choice
import pickle
import os

from Code import Code


"""
Fonctions utilisées
"""

def create_uid(n=9):
    '''Génère une chaîne de caractères alétoires de longueur n
   en évitant 0, O, I, l pour être sympa.'''
    chrs = [c for c in chain(ascii_letters, digits)
            if c not in '0OIl']
    return ''.join((choice(chrs) for i in range(n)))



"""
Sauvegarde du code dans un fichier
"""

def save_doc_as_file(code=Code()):
    '''Crée/Enregistre le document sous la forme d'un fichier
    data/uid. Return the file name.
    '''
    uid = code.uid
    if uid is None:
        code = Code()
    with open(f'data/{uid}', 'w') as fd:
        code = str(code)
        print(code)
        fd.write(code)
    return uid


"""
Récupération d'un code à partir d'un fichier
"""

def read_doc_as_file(uid):
    '''Lit le document data/uid'''
    try:
        with open(f'data/{uid}') as fd:
            code = ast.literal_eval(fd.read())
            code = Code(**code)
        return code
    except FileNotFoundError:
        return None

"""
Récupération des n derniers codes
"""

def get_last_entries_from_files(n=10, nlines=10):
    entries = os.scandir('data')
    d = []
    entries = sorted(list(entries),
                     key=(lambda e: e.stat().st_mtime),
                     reverse=True)
    for i, e in enumerate(entries):
        if i >= n:
            break
        if e.name.startswith('.'):
            continue
        code = read_doc_as_file(e.name)
        d.append(code)
    return d
