import sqlite3

from itertools import chain
from random import choice
from string import ascii_letters, digits

def createTables():
    connection = sqlite3.connect('database/sharecode-plus.db')
    cursor = connection.cursor()

    with open('database/migrations/create_codes_table.sql') as file:
        cursor.executescript(file.read())

    connection.commit()

    with open('database/migrations/create_logs_table.sql') as file:
        cursor.executescript(file.read())

    connection.commit()
    connection.close()


def createCode():
    connection = sqlite3.connect('database/sharecode-plus.db')
    cursor = connection.cursor()

    uid = create_uid()

    cursor.execute('''
        INSERT INTO codes (uid) VALUES (?)
    ''', [uid])

    connection.commit()
    connection.close()

    return uid


def getCode(uid):
    conn = sqlite3.connect('database/sharecode-plus.db')
    c = conn.cursor()

    c.execute('''
        SELECT
            language,
            content
        FROM codes
        WHERE uid = ?
    ''', [uid])

    result = c.fetchone()

    conn.commit()
    conn.close()

    return result


def getAllCode():
    conn = sqlite3.connect('database/sharecode-plus.db')
    c = conn.cursor()

    c.execute('''
        SELECT
            uid,
            content,
            language
        FROM codes
        ORDER BY
            updated_at DESC,
            created_at DESC
    ''')

    result = c.fetchall()

    conn.commit()
    conn.close()

    return result


def updateCode(uid, content, language):
    conn = sqlite3.connect('database/sharecode-plus.db')
    c = conn.cursor()

    result = c.execute('''
        UPDATE codes
        SET
            content= ?,
            language = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE uid = ?
    ''', (content, language, uid))

    conn.commit()
    conn.close()

    return result


def createLog(ip, user_agent):
    conn = sqlite3.connect('database/sharecode-plus.db')
    c = conn.cursor()

    uid = create_uid()

    c.execute('''
        INSERT INTO logs (uid, address_ip, user_agent)
        VALUES(?,?,?)
    ''', [uid, ip, user_agent])

    conn.commit()
    conn.close()

    return uid


def getLog():
    conn = sqlite3.connect('database/sharecode-plus.db')
    c = conn.cursor()

    result = c.execute('''
        SELECT address_ip, user_agent, created_at
        FROM logs
        ORDER BY created_at DESC
    ''')

    conn.commit()
    conn.close()

    return result

def create_uid(n=9):
    '''Génère une chaîne de caractères alétoires de longueur n
   en évitant 0, O, I, l pour être sympa.'''
    chrs = [c for c in chain(ascii_letters, digits)
            if c not in '0OIl']
    return ''.join((choice(chrs) for i in range(n)))