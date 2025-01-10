import os

from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox, QLabel, QColorDialog

from AddTag import Ui_addTage
from AddTagToNote import Ui_Dialog as Ui_addTagToNote
from DataBaseManeger import ManegerDB
from MainWindow import Ui_MainWindow
from NoteEdit import Ui_Dialog as Ui_noteEdit
from NoteEditExist import Ui_Dialog as Ui_noteEditExist


class ListNoteWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('./static/ui/MainWindow.ui', self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        icon = QIcon('./static/img/mainIcon.png')
        self.setWindowIcon(icon)
        self.load_tags()
        self.load_list_elem()
        self.setWindowTitle('Заметки')
        self.createButton.clicked.connect(self.open_edit_form)
        self.editButton.clicked.connect(self.open_edit_existing_form)
        self.addTagButton.clicked.connect(self.open_add_tag_form)
        self.deleteButton.clicked.connect(self.delete_note)
        self.tagComboBox.currentIndexChanged.connect(self.on_tag_selected)
        self.sortComboBox.currentIndexChanged.connect(self.on_tag_selected)

    def load_tags(self):
        # Загрузить тэги из базы данных в комбобокс.
        maneg_db = ManegerDB('./db/NoteDB.db')
        rows = maneg_db.load_tags_from_db()
        self.tagComboBox.clear()
        self.tagComboBox.addItem('Тег не выбран')
        for row in rows:
            self.tagComboBox.addItem(row[0])

    def load_list_elem(self, sort_by_date=False):
        # Загрузить названия заметок из базы данных в список.
        maneg_db = ManegerDB('./db/NoteDB.db')
        rows = maneg_db.load_notes_from_db(sort_by_date)
        self.listNotes.clear()
        for row in rows:
            self.listNotes.addItem(row[0])

    def on_tag_selected(self, index):
        # Оставить в списке только заметки, содержащие тэг, выбранный в комбобоксе.
        index_1 = self.tagComboBox.currentIndex()
        index_2 = self.sortComboBox.currentIndex()
        if index_1 == -1 or index_2 == -1:
            return
        tag = self.tagComboBox.itemText(index_1)
        sort = self.sortComboBox.itemText(index_2)
        f = False
        if sort == "По дате":
            f = True
        else:
            f = False
        if tag == "Тег не выбран":
            self.load_list_elem(f)
        else:
            maneg_db = ManegerDB('./db/NoteDB.db')
            notes = maneg_db.get_notes_by_tag(tag, f)
            self.listNotes.clear()
            for note in notes:
                self.listNotes.addItem(note)

    def open_edit_form(self):
        # Открыть окно для создания заметки.
        edit_form = EditNoteWindow(self)
        edit_form.exec_()

    def open_add_tag_form(self):
        # Открыть окно для добавления тега.
        add_tag_form = AddTagWindow(self)
        add_tag_form.exec_()

    def open_edit_existing_form(self):
        # Открыть окно для редактирования заметки.
        selected_items = self.listNotes.selectedItems()
        if len(selected_items) > 0:
            name_note = selected_items[0].text()
            edit_form = EditNoteExistWindow(self, name_note)
            edit_form.exec_()
        else:
            return

    def delete_note(self):
        # Удалить заметку, перед этим выведя сообщение для подтвержденя.
        selected_items = self.listNotes.selectedItems()
        if len(selected_items) > 0:
            note_name = selected_items[0].text()
            msg_box = QMessageBox.question(
                self,
                'Подтверждение',
                f'"Вы действительно хотите удалить заметку "{note_name}"?"',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if msg_box == QMessageBox.Yes:
                maneg_db = ManegerDB('./db/NoteDB.db')
                maneg_db.delete_note_by_name(note_name)
                self.load_list_elem()
        else:
            return


class EditNoteWindow(QDialog, Ui_noteEdit):
    def __init__(self, parent=None):
        super(EditNoteWindow, self).__init__(parent)
        # uic.loadUi('./static/ui/NoteEdit.ui', self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        icon = QIcon('./static/img/mainIcon.png')
        self.setWindowIcon(icon)
        self.setWindowTitle('Редактирование')
        self.addTagButton.clicked.connect(self.open_add_tag_to_note_form)
        self.boldButton.clicked.connect(self.make_text_bold)
        self.italicButton.clicked.connect(self.make_text_italic)
        self.saveButton.clicked.connect(self.save_note)
        self.canelButton.clicked.connect(self.canel_note)
        self.colorButton.clicked.connect(self.show_color_dialog)

    def show_color_dialog(self):
        # Открыть диалог для выбора цвета
        color = QColorDialog.getColor()
        if color.isValid():
            self.contentField.setTextColor(color)

    def canel_note(self):
        # Закрыть окно для редактированя заметки без сохранения изменений, перед этим выведя сообщение для подтверждения.
        msg_box = QMessageBox.question(
            self,
            'Подтверждение',
            'Вы действительно хотите закрыть заметку?\nИзменения не сохранятся.',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if msg_box == QMessageBox.Yes:
            self.done(0)

    def save_note(self):
        # Сохранить заметку и закрыть окно.
        title = self.nameField.text()
        path_save = './static/notesstorage/'
        tag = ""
        try:
            tag = self.tagLabel.text()
        except AttributeError as e:
            print(f'Ошибка: {e}')
        if not title:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText(f'Вы не указали название заметки')
            msg_box.exec_()
        else:
            html_content = self.contentField.toHtml()
            note_path = os.path.join(path_save, f'{title}.txt')
            if os.path.exists(note_path):
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(f'Заметка с именем "{title}" уже существует.')
                msg_box.exec_()
            else:
                maneg_db = ManegerDB('./db/NoteDB.db')
                success = maneg_db.add_note_to_db(title)
                if not success:
                    return
                with open(f'{path_save}{title}.txt', 'w') as file:
                    file.write(html_content)
                if tag != "":
                    maneg_db.add_elem_to_tag_note(title, tag)
            self.done(0)

    def make_text_bold(self):
        # Сделать выделенный текст жирным.
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
        # Сделать выделенный текст курсивом.
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
        # Открыть окно для добавления тэга.
        add_tag_to_note_form = AddTagToNoteWindow(self)
        add_tag_to_note_form.exec_()


class EditNoteExistWindow(QDialog, Ui_noteEditExist):
    def __init__(self, parent=None, note_name=None):
        super(EditNoteExistWindow, self).__init__(parent)
        self.note_name = note_name
        # uic.loadUi('./static/ui/NoteEditExist.ui', self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        icon = QIcon('./static/img/mainIcon.png')
        self.setWindowIcon(icon)
        self.add_content()
        self.setWindowTitle('Редактирование')
        self.boldButton.clicked.connect(self.make_text_bold)
        self.italicButton.clicked.connect(self.make_text_italic)
        self.saveButton.clicked.connect(self.save_note)
        self.canelButton.clicked.connect(self.canel_note)
        self.colorButton.clicked.connect(self.show_color_dialog)

    def show_color_dialog(self):
        # Открыть диалог для выбора цвета
        color = QColorDialog.getColor()
        if color.isValid():
            self.contentField.setTextColor(color)

    def canel_note(self):
        # Закрыть окно для редактированя заметки без сохранения изменений, перед этим выведя сообщение для подтверждения.
        msg_box = QMessageBox.question(
            self,
            'Подтверждение',
            'Вы действительно хотите закрыть заметку?\nИзменения не сохранятся.',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if msg_box == QMessageBox.Yes:
            self.done(0)

    def add_content(self):
        # Добавить в окно для редактирования содержание, название и тэг заметки.
        maneg_db = ManegerDB('./db/NoteDB.db')
        note_content = maneg_db.load_note_from_db(self.note_name)
        self.label.setText(note_content[0])
        with open(f'./static/notesstorage/{self.note_name}.txt', 'r') as file:
            text = file.read()
        self.contentField.setHtml(text)
        tag = maneg_db.get_tags_by_note(self.note_name)
        if tag is None:
            return
        else:
            self.tagLabel.setText(tag[0])
        return

    def save_note(self):
        # Сохранить заметку и закрыть окно.
        title = self.nameLabel.text()
        path_save = './static/notesstorage/'
        html_content = self.contentField.toHtml()
        with open(f'{path_save}{title}.txt', 'w') as file:
            file.write(html_content)
        pass
        self.done(0)

    def make_text_bold(self):
        # Сделать выделенный текст жирным.
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
        # Сделать выделенный текст курсивом.
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


class AddTagWindow(QDialog, Ui_addTage):
    def __init__(self, parent=None):
        super(AddTagWindow, self).__init__(parent)
        self.parent = parent
        # uic.loadUi('./static/ui/AddTag.ui', self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        icon = QIcon('./static/img/mainIcon.png')
        self.setWindowIcon(icon)
        self.setWindowTitle('Тэги')
        self.pixmap = QPixmap('static/img/tagIcon.png')
        self.image = QLabel(self)
        self.image.move(190, 20)
        self.image.resize(26, 29)
        self.image.setPixmap(self.pixmap)
        self.canelButton.clicked.connect(self.accept)
        self.addButton.clicked.connect(self.add_tag)

    def add_tag(self):
        # Добавить тэг, записанный в текстовое поле, в базу данных.
        new_tag = self.tagField.text().strip()
        if not new_tag:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText(f'Вы не указали название тега')
            msg_box.exec_()
        else:
            maneg_db = ManegerDB('./db/NoteDB.db')
            success = maneg_db.add_tag_to_db(new_tag)
            if not success:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setText(f'Такой тег уже существует')
                msg_box.exec_()
            else:
                self.parent.load_tags()
                self.tagField.clear()
                self.done(0)


class AddTagToNoteWindow(QDialog, Ui_addTagToNote):
    def __init__(self, parent=None):
        super(AddTagToNoteWindow, self).__init__(parent)
        self.parent = parent
        # uic.loadUi('./static/ui/AddTagToNote.ui', self)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pixmap = QPixmap('static/img/tagIcon.png')
        self.image = QLabel(self)
        self.image.move(120, 15)
        self.image.resize(26, 29)
        self.image.setPixmap(self.pixmap)
        icon = QIcon('./static/img/mainIcon.png')
        self.setWindowIcon(icon)
        self.load_tags()
        self.setWindowTitle('Добавить тэг')
        self.canelButton.clicked.connect(self.accept)
        self.addButton.clicked.connect(self.add_tag_to_note)

    def load_tags(self):
        # Загрузить тэги в комбобокс из базы данных.
        maneg_db = ManegerDB('./db/NoteDB.db')
        rows = maneg_db.load_tags_from_db()
        self.tagComboBox.clear()
        for row in rows:
            self.tagComboBox.addItem(row[0])

    def add_tag_to_note(self):
        # Добавить тэг из комбобокса к заметке в окне редактирования.
        tag = self.tagComboBox.currentText()
        self.parent.tagLabel.setText(tag)
        self.done(0)