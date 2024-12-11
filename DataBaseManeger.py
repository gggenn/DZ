import sys
import os

import sqlite3


class ManegerDB:
    def __init__(self, path):
        self.path = path

    def get_notes_by_tag(self, tag):
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute(f"SELECT Note FROM Tag_note WHERE Tag = ?", (tag,))
        notes = [{'Note': row[0]} for row in cursor.fetchall()]
        connector.close()
        return notes

    def get_notes_by_name(self, name):
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute(f"SELECT Name FROM Notes WHERE Name = ?", (name,))
        notes = [{'Note': row[0]} for row in cursor.fetchall()]
        connector.close()
        return notes

    def load_tags_from_db(self):
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        # Выполняем запрос для получения всех названий тегов
        cursor.execute("SELECT Name FROM Tags ORDER BY Name ASC")
        # Получаем все строки результата
        rows = cursor.fetchall()
        # Закрываем соединение с базой данных
        connector.close()

        return rows

    def load_notes_from_db(self):
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        # Выполняем запрос для получения всех названий тегов
        cursor.execute("SELECT Name FROM Notes ORDER BY Name ASC")
        # Получаем все строки результата
        rows = cursor.fetchall()
        # Закрываем соединение с базой данных
        connector.close()

        return rows

    def add_tag_to_db(self, new_tag):
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        # Проверяем наличие тега с таким же именем
        cursor.execute("SELECT COUNT(*) FROM Tags WHERE Name = ?", (new_tag,))
        count = cursor.fetchone()[0]
        if count > 0:
            return False
        else:
            # Выполняем запрос для вставки нового тега
            cursor.execute("INSERT INTO Tags (Name) VALUES (?)", (new_tag,))
        connector.commit()
        connector.close()
        return True

    def add_note_to_db(self, new_note):
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        path_note = f"./static/notesstorage/{new_note}"
        # Проверяем наличие заметки с таким же именем
        cursor.execute("SELECT COUNT(*) FROM Notes WHERE Name = ?", (new_note,))
        count = cursor.fetchone()[0]
        if count > 0:
            return False
        else:
            # Выполняем запрос для вставки новой заметки
            cursor.execute("INSERT INTO Notes (Name, Content) VALUES (?, ?)", (new_note, path_note))
        connector.commit()
        connector.close()
        return True

    def add_elem_to_tag_note(self, note, tag):
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute("SELECT COUNT(*) FROM Tag_note WHERE Note = ? AND Tag = ?", (note, tag))
        count = cursor.fetchone()[0]
        if count > 0:
            return False
        else:
            cursor.execute("INSERT INTO Tag_note (Note, Tag) VALUES (?, ?)", (note, tag))
        connector.commit()
        connector.close()
        return True

    def load_note_from_db(self, note_name):
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute(f"SELECT Name, Content FROM Notes WHERE Name = ?", (note_name,))
        note = cursor.fetchone()
        if note is None:
            print("Запись не найдена.")
        connector.close()
        return note

    def get_tags_by_note(self, note):
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute(f"SELECT Tag FROM Tag_note WHERE Note = ?", (note,))
        tag = cursor.fetchone()
        connector.close()
        return tag

    def delete_note_by_name(self, note):
        connector = sqlite3.connect(self.path)
        cursor = connector.cursor()
        cursor.execute(f'DELETE FROM Notes WHERE Name = ?', (note,))

        cursor.execute(f'DELETE FROM Tag_note WHERE Note = ?', (note,))
        connector.commit()
        connector.close()

        path_note = f'static/notesstorage/{note}.txt'
        # Проверяем существование файла перед удалением
        if os.path.exists(path_note):
            # Удаляем файл
            os.remove(path_note)
        return True