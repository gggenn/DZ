import os
from datetime import datetime

import sqlite3


class ManegerDB:
    def __init__(self, path):
        self.path = path

    def get_notes_by_tag(self, tag, sort_by_date=False):
        # Получить из базы данных заметки, содержащие указанный тэг.
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        if sort_by_date:
            query = '''
                    SELECT n.Name
                    FROM Notes n
                    JOIN Tag_note tn ON n.Name = tn.Note
                    WHERE tn.Tag = ?
                    ORDER BY n.Creation_date ASC
                '''
            cursor.execute(query, (tag,))
        else:
            query = '''
                    SELECT n.Name
                    FROM Notes n
                    JOIN Tag_note tn ON n.Name = tn.Note
                    WHERE tn.Tag = ?
                '''
            cursor.execute(query, (tag,))
        notes = [row[0] for row in cursor.fetchall()]
        connector.close()
        print(notes)
        return notes

    def get_notes_by_name(self, name):
        # Получить заметку из базы данных по указанному имени.
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute(f'SELECT Name FROM Notes WHERE Name = ?',
                       (name,))
        notes = [{'Note': row[0]} for row in cursor.fetchall()]
        connector.close()
        return notes

    def load_tags_from_db(self):
        # Загрузить все тэги из базы данных.
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute('SELECT Name FROM Tags ORDER BY Name ASC')
        rows = cursor.fetchall()
        connector.close()

        return rows

    def load_notes_from_db(self, sort_by_date=False):
        # Загрузить все заметки из базы данных.
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        if not sort_by_date:
            cursor.execute('SELECT Name FROM Notes ORDER BY Name ASC')
        else:
            cursor.execute('SELECT Name FROM Notes ORDER BY Creation_date ASC')
        rows = cursor.fetchall()
        connector.close()
        return rows

    def add_tag_to_db(self, new_tag):
        # Добавить тэг в базу данных.
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute('SELECT COUNT(*) FROM Tags WHERE Name = ?',
                       (new_tag,))
        count = cursor.fetchone()[0]
        if count > 0:
            return False
        else:
            cursor.execute('INSERT INTO Tags (Name) VALUES (?)',
                           (new_tag,))
        connector.commit()
        connector.close()
        return True

    def add_note_to_db(self, new_note):
        # Добавить заметку в базу данных.
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        path_note = f'./static/notesstorage/{new_note}'
        cursor.execute('SELECT COUNT(*) FROM Notes WHERE Name = ?',
                       (new_note,))
        count = cursor.fetchone()[0]
        if count > 0:
            return False
        else:
            current_date = datetime.now().date()
            cursor.execute('INSERT INTO Notes (Name, Content, Creation_date) VALUES (?, ?, ?)',
                           (new_note, path_note, current_date))
        connector.commit()
        connector.close()
        return True

    def add_elem_to_tag_note(self, note, tag):
        # Добавить в базу данных заметку и ее тэг.
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute('SELECT COUNT(*) FROM Tag_note WHERE Note = ? AND Tag = ?',
                       (note, tag))
        count = cursor.fetchone()[0]
        if count > 0:
            return False
        else:
            cursor.execute('INSERT INTO Tag_note (Note, Tag) VALUES (?, ?)',
                           (note, tag))
        connector.commit()
        connector.close()
        return True

    def load_note_from_db(self, note_name):
        # Загрузить заметку из базы данных по имени.
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute(f'SELECT Name, Content FROM Notes WHERE Name = ?',
                       (note_name,))
        note = cursor.fetchone()
        if note is None:
            print('Запись не найдена.')
        connector.close()
        return note

    def get_tags_by_note(self, note):
        # Получить тэг заметки по ее имени.
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute(f'SELECT Tag FROM Tag_note WHERE Note = ?',
                       (note,))
        tag = cursor.fetchone()
        connector.close()
        return tag

    def delete_note_by_name(self, note):
        # Удалить заметку с указанным имененем.
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute(f'DELETE FROM Notes WHERE Name = ?',
                       (note,))

        cursor.execute(f'DELETE FROM Tag_note WHERE Note = ?',
                       (note,))
        connector.commit()
        connector.close()
        path_note = f'static/notesstorage/{note}.txt'
        if os.path.exists(path_note):
            os.remove(path_note)
        return True