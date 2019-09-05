# Импортируем библиотеку, соответствующую типу нашей базы данных 
import sqlite3
def newClient(client):
    # Создаем соединение с нашей базой данных
    # В нашем примере у нас это просто файл базы
    conn = sqlite3.connect('SQLvisa.db')

    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor = conn.cursor()

    # cursor.execute("""CREATE TABLE clients
    #                   (surname text, name text, sex text,
    #                    country text, Bcountry text, Byear text,
    #                    Bmonth text, Bday text, Pserial text, 
    #                    Pyear text, Pmonth text, Pday text)""")


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