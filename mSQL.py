import sqlite3
def newClient(client):
    conn = sqlite3.connect('SQLvisa.db')

    cursor = conn.cursor()

    try:
        cursor.execute("""INSERT INTO clients
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                        client)
        conn.commit()
        print('new client added to db')
    except sqlite3.Error as e:
        print("Database error: %s" % e)
    except Exception as e:
        print("Exception in _query: %s" % e)
    finally:
        conn.close()    