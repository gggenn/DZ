import sys
import sqlite3

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLabel, QListWidget, QTextEdit, QLineEdit
from PyQt5.QtGui import QFont

from DataBaseManeger import ManegerDB
from MainWindow import Ui_MainWindow
from NoteEdit import Ui_Dialog as Ui_noteEdit
from AddTag import Ui_addTage
from AddTagToNote import Ui_Dialog as Ui_addTagToNote


class ListNoteWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('./static/ui/MainWindow.ui', self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Загружаем теги из базы данных
        self.load_tags()
        self.load_list_elem()
        self.createButton.clicked.connect(self.open_edit_form)
        self.editButton.clicked.connect(self.open_edit_existing_form)
        self.addTagButton.clicked.connect(self.open_add_tag_form)
        self.deleteButton.clicked.connect(self.delete_note)
        self.tagComboBox.currentIndexChanged.connect(self.on_tag_selected)

    def load_tags(self):
        maneg_db = ManegerDB('./db/NoteDB.db')
        rows = maneg_db.load_tags_from_db()
        # Очищаем содержимое combo box перед добавлением новых элементов
        self.tagComboBox.clear()
        self.tagComboBox.addItem('Тег не выбран')
        # Добавляем каждый тег в combo box
        for row in rows:
            # Так как fetchall() возвращает кортежи, то берем первый элемент каждого кортежа
            self.tagComboBox.addItem(row[0])

    def load_list_elem(self):
        maneg_db = ManegerDB('./db/NoteDB.db')
        rows = maneg_db.load_notes_from_db()
        self.listNotes.clear()
        for row in rows:
            # item = QListWidgetItem(note['Note'])
            self.listNotes.addItem(row[0])

    def on_tag_selected(self, index):
        if index == -1:
            return
        tag = self.tagComboBox.itemText(index)
        if tag == "Тег не выбран":
            self.load_list_elem()
        else:
            maneg_db = ManegerDB('./db/NoteDB.db')
            notes = maneg_db.get_notes_by_tag(tag)
            # Очистка ListWidget перед добавлением новых элементов
            self.listNotes.clear()
            for note in notes:
                # item = QListWidgetItem(note['Note'])
                self.listNotes.addItem(note['Note'])

    def open_edit_form(self):
        edit_form = EditNoteWindow(self) # Создаем диалог с родителем
        edit_form.exec_() # Сделать диалог модальным

    def open_add_tag_form(self):
        add_tag_form = AddTagWindow(self) # Создаем диалог с родителем
        add_tag_form.exec_() # Сделать диалог модальным

    def open_edit_existing_form(self):
        selected_items = self.listNotes.selectedItems()
        if len(selected_items) > 0:
            name_note = selected_items[0].text()  # Получаем текст первого выделенного элемента
            edit_form = EditNoteWindow(self, name_note)  # Создаем диалог с родителем
            edit_form.exec_()  # Сделать диалог модальным
        else:
            return

    def delete_note(self):
        selected_items = self.listNotes.selectedItems()
        if len(selected_items) > 0:
            note = selected_items[0].text()  # Получаем текст первого выделенного элемента
            maneg_db = ManegerDB('./db/NoteDB.db')
            maneg_db.delete_note_by_name(note)
            self.load_list_elem()
        else:
            return


class EditNoteWindow(QDialog, Ui_noteEdit):
    def __init__(self, parent=None, note_name=None):
        super(EditNoteWindow, self).__init__(parent)
        self.note_name = note_name
        # uic.loadUi('./static/ui/NoteEdit.ui', self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.add_content()
        self.addTagButton.clicked.connect(self.open_add_tag_to_note_form)
        self.boldButton.clicked.connect(self.make_text_bold)
        self.italicButton.clicked.connect(self.make_text_italic)
        self.saveButton.clicked.connect(self.save_note)
        self.canelButton.clicked.connect(self.accept)  # Закрыть диалог по нажатию

    def add_content(self):
        if self.note_name is None:
            return
        maneg_db = ManegerDB('./db/NoteDB.db')
        note_content = maneg_db.load_note_from_db(self.note_name)
        self.nameField.setText(note_content[0])
        with open(f'./static/notesstorage//{self.note_name}.txt', 'r') as file:
            text = file.read()
        self.contentField.setHtml(text)
        tag = maneg_db.get_tags_by_note(self.note_name)
        if tag is None:
            return
        else:
            self.tagLabel.setText(tag[0])
        return

    def save_note(self):
        title = self.nameField.text()
        tag = ""
        try:
            tag = self.tagLabel.text()
        except AttributeError as e:
            print(f'Ошибка: {e}')
        if not title:
            return
        html_content = self.contentField.toHtml()
        if self.note_name is None:
            maneg_db = ManegerDB('./db/NoteDB.db')
            success = maneg_db.add_note_to_db(title)
            if not success:
                return
            with open(f'./static/notesstorage/{title}.txt', 'w') as file:
                file.write(html_content)
            if tag != "":
                maneg_db.add_elem_to_tag_note(title, tag)
        else:
            with open(f'./static/notesstorage/{title}.txt', 'w') as file:
                file.write(html_content)
            pass
        self.done(0)

    def make_text_bold(self):
            cursor = self.contentField.textCursor()
            if not cursor.hasSelection():
                return
            format = cursor.charFormat()
            font = format.font()
            weight = font.weight()
            if weight == QFont.Bold:
                font.setWeight(QFont.Normal)
            else:
                font.setWeight(QFont.Bold)
            format.setFont(font)
            cursor.mergeCharFormat(format)

    def make_text_italic(self):
            cursor = self.contentField.textCursor()
            if not cursor.hasSelection():
                return
            format = cursor.charFormat()
            font = format.font()
            weight = font.weight()
            if not font.italic():
                font.setItalic(True)
            else:
                font.setItalic(False)
            format.setFont(font)
            cursor.mergeCharFormat(format)

    def open_add_tag_to_note_form(self):
        add_tag_to_note_form = AddTagToNoteWindow(self) # Создаем диалог с родителем
        add_tag_to_note_form.exec_() # Сделать диалог модальным


class AddTagWindow(QDialog, Ui_addTage):
    def __init__(self, parent=None):
        super(AddTagWindow, self).__init__(parent)
        self.parent = parent
        # uic.loadUi('./static/ui/AddTag.ui', self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.canelButton.clicked.connect(self.accept)  # Закрыть диалог по нажатию
        self.addButton.clicked.connect(self.add_tag)

    def add_tag(self):
        # Получаем введенный текст из поля ввода
        new_tag = self.tagField.text().strip()
        if not new_tag:
            return
        maneg_db = ManegerDB('./db/NoteDB.db')
        success = maneg_db.add_tag_to_db(new_tag)
        if not success:
            return
        # Обновляем список тегов в ComboBox
        self.parent.load_tags()
        # Очищаем поле ввода
        self.tagField.clear()
        # Закрываем окно
        self.done(0)


class AddTagToNoteWindow(QDialog, Ui_addTagToNote):
    def __init__(self, parent=None):
        super(AddTagToNoteWindow, self).__init__(parent)
        self.parent = parent
        # uic.loadUi('./static/ui/AddTagToNote.ui', self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.load_tags()
        self.canelButton.clicked.connect(self.accept)  # Закрыть диалог по нажатию
        self.addButton.clicked.connect(self.add_tag_to_note)

    def load_tags(self):
        maneg_db = ManegerDB('./db/NoteDB.db')
        rows = maneg_db.load_tags_from_db()
        # Очищаем содержимое combo box перед добавлением новых элементов
        self.tagComboBox.clear()
        # Добавляем каждый тег в combo box
        for row in rows:
            # Так как fetchall() возвращает кортежи, то берем первый элемент каждого кортежа
            self.tagComboBox.addItem(row[0])

    def add_tag_to_note(self):
        tag = self.tagComboBox.currentText()
        self.parent.tagLabel.setText(tag)
        self.done(0)