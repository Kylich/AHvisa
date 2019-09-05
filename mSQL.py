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

    cursor.execute("""INSERT INTO albums
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                    client)
    
    # Сохраняем изменения
    conn.commit()

    # Не забываем закрыть соединение с базой данных
    conn.close()
    print('new client added to db')