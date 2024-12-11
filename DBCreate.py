import sqlite3
from datetime import datetime

# Подключение к базе данных (или создание новой базы данных)
conn = sqlite3.connect('NoteDB.db')
cursor = conn.cursor()

# Создание таблицы Notes
create_table_query = '''
CREATE TABLE IF NOT EXISTS Notes (
    Name TEXT PRIMARY KEY,
    Content TEXT,
    Creation_date DATE,
    Edit_date DATE
);
'''
cursor.execute(create_table_query)

create_table_query = '''
CREATE TABLE IF NOT EXISTS Tags (
    Name TEXT PRIMARY KEY
);
'''
cursor.execute(create_table_query)

create_table_query = '''
CREATE TABLE IF NOT EXISTS Tag_note (
    Note TEXT,
    Tag TEXT,
    FOREIGN KEY (Note) REFERENCES Notes(Name) ON DELETE CASCADE,
    FOREIGN KEY (Tag) REFERENCES Tags(Name) ON DELETE CASCADE
);
'''
cursor.execute(create_table_query)

# Получение текущей даты
# current_date = datetime.now().strftime('%Y-%m-%d')

# Добавление записи
# insert_data_query = """
# INSERT INTO Notes (Name, Content, Creation_date, Edit_date)
# VALUES ('Первая заметка', 'содержание', ?, ?);
# """
# cursor.execute(insert_data_query, (current_date, current_date))

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()