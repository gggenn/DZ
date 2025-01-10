# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 595)
        MainWindow.setStyleSheet("QWidget#MainWindow {\n"
"    background-color: #EAEDFE;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addTagButton = QtWidgets.QPushButton(self.centralwidget)
        self.addTagButton.setStyleSheet("QPushButton {\n"
"    background-color: #eebbc3;\n"
"    border-radius: 4px;\n"
"    padding-top: 6px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 10px;\n"
"    color: #232946;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E6B4BC; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFC9D2;\n"
"}")
        self.addTagButton.setObjectName("addTagButton")
        self.horizontalLayout.addWidget(self.addTagButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tagComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.tagComboBox.setStyleSheet("    background-color: #eebbc3;\n"
"    border-radius: 4px;\n"
"    padding-top: 6px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 10px;\n"
"    color: #232946;\n"
"    font-size: 14px;\n"
"\n"
"")
        self.tagComboBox.setObjectName("tagComboBox")
        self.tagComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.tagComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.sortComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.sortComboBox.setStyleSheet("QComboBox {\n"
"    background-color: #eebbc3;\n"
"    border-radius: 4px;\n"
"    padding-top: 6px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 10px;\n"
"    color: #232946;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.sortComboBox.setObjectName("sortComboBox")
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.verticalLayout_2.addWidget(self.sortComboBox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setStyleSheet("QPushButton {\n"
"    background-color: #eebbc3;\n"
"    border-radius: 4px;\n"
"    padding-top: 6px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 10px;\n"
"    color: #232946;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E6B4BC; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFC9D2;\n"
"}")
        self.createButton.setObjectName("createButton")
        self.horizontalLayout_2.addWidget(self.createButton)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setStyleSheet("QPushButton {\n"
"    background-color: #eebbc3;\n"
"    border-radius: 4px;\n"
"    padding-top: 6px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 10px;\n"
"    color: #232946;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E6B4BC; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFC9D2;\n"
"}")
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_2.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setStyleSheet("QPushButton {\n"
"    background-color: #eebbc3;\n"
"    border-radius: 4px;\n"
"    padding-top: 6px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 6px;\n"
"    padding-left: 10px;\n"
"    color: #232946;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E6B4BC; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #FFC9D2;\n"
"}")
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_2.addWidget(self.deleteButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.listNotes = QtWidgets.QListWidget(self.centralwidget)
        self.listNotes.setStyleSheet("background-color: white;\n"
"border-radius: 4px;\n"
"color: #232946;\n"
"font-size: 14px;\n"
"border: 1px solid #ccc;")
        self.listNotes.setObjectName("listNotes")
        self.verticalLayout_5.addWidget(self.listNotes)
        self.verticalLayout_5.setStretch(0, 10)
        self.verticalLayout_5.setStretch(1, 90)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addTagButton.setText(_translate("MainWindow", "Добавить тег"))
        self.tagComboBox.setItemText(0, _translate("MainWindow", "Ничего"))
        self.sortComboBox.setItemText(0, _translate("MainWindow", "По названию"))
        self.sortComboBox.setItemText(1, _translate("MainWindow", "По дате"))
        self.createButton.setText(_translate("MainWindow", "Создать"))
        self.editButton.setText(_translate("MainWindow", "Редактировать"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
