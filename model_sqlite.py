import sqlite3

def createTables():
    connection = sqlite3.connect('database/sharecode-plus.db')
    cursor = connection.cursor()

    with open('database/migrations/create_codes_table.sql') as file:
        cursor.executescript(file.read())

    connection.commit()

    with open('database/migrations/create_editions_table.sql') as file:
        cursor.executescript(file.read())

    connection.commit()
    connection.close()


def createCode():
    connection = sqlite3.connect('database/sharecode-plus.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO codes DEFAULT VALUES
    ''')

    uid = cursor.lastrowid

    connection.commit()
    connection.close()

    return uid


def getCode(uid):
    conn = sqlite3.connect('database/sharecode-plus.db')
    c = conn.cursor()

    c.execute('''
        SELECT
            content,
            language
        FROM codes
        WHERE uid = ?
    ''', uid)

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


def updateCode(uid, code, language):
    conn = sqlite3.connect('database/sharecode-plus.db')
    c = conn.cursor()

    result = c.execute('''
        UPDATE codes
        SET
            content= ?,
            language = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE uid = ?
    ''', (code, language, uid))

    conn.commit()
    conn.close()

    return result


def createEdition(ip, user_agent):
    conn = sqlite3.connect('database/sharecode-plus.db')
    c = conn.cursor()

    c.execute('''
        INSERT INTO editions
        VALUES(?,?)
    ''', (ip, user_agent))

    uid = c.lastrowid

    conn.commit()
    conn.close()

    return uid


def getEdition():
    conn = sqlite3.connect('database/sharecode-plus.db')
    c = conn.cursor()

    result = c.execute('''
        SELECT ip, user_agent, date
        FROM editions
        ORDER BY date DESC
    ''')

    conn.commit()
    conn.close()

    return result
