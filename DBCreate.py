import sqlite3


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

# Создание таблицы Tags
create_table_query = '''
CREATE TABLE IF NOT EXISTS Tags (
    Name TEXT PRIMARY KEY
);
'''
cursor.execute(create_table_query)

# Создание таблицы Tag_note
create_table_query = '''
CREATE TABLE IF NOT EXISTS Tag_note (
    Note TEXT,
    Tag TEXT,
    FOREIGN KEY (Note) REFERENCES Notes(Name) ON DELETE CASCADE,
    FOREIGN KEY (Tag) REFERENCES Tags(Name) ON DELETE CASCADE
);
'''
cursor.execute(create_table_query)

conn.commit()

conn.close()