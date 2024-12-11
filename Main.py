import sys

from PyQt5.QtWidgets import QApplication

from InterfaceManeger import ListNoteWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ListNoteWindow()
    form.show()
    sys.exit(app.exec())