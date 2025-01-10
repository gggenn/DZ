# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NoteEditExist.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setStyleSheet("\n"
"    background-color: #EAEDFE;\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.boldButton = QtWidgets.QPushButton(self.widget)
        self.boldButton.setStyleSheet("QPushButton {\n"
"    background-color: #eebbc3;\n"
"    border-radius: 4px;\n"
"    width: 40px;\n"
"    height: 28px;\n"
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
        self.boldButton.setObjectName("boldButton")
        self.horizontalLayout.addWidget(self.boldButton)
        self.italicButton = QtWidgets.QPushButton(self.widget)
        self.italicButton.setStyleSheet("QPushButton {\n"
"    background-color: #eebbc3;\n"
"    border-radius: 4px;\n"
"    width: 40px;\n"
"    height: 28px;\n"
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
        self.italicButton.setObjectName("italicButton")
        self.horizontalLayout.addWidget(self.italicButton)
        self.colorButton = QtWidgets.QPushButton(self.widget)
        self.colorButton.setStyleSheet("QPushButton {\n"
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
        self.colorButton.setObjectName("colorButton")
        self.horizontalLayout.addWidget(self.colorButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("background-color: white;\n"
"border-radius: 4px;\n"
"color: #232946;\n"
"font-size: 14px;\n"
"border: 1px solid #ccc;\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tagLabel = QtWidgets.QLabel(self.widget)
        self.tagLabel.setText("")
        self.tagLabel.setObjectName("tagLabel")
        self.horizontalLayout_3.addWidget(self.tagLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.contentField = QtWidgets.QTextEdit(self.widget)
        self.contentField.setStyleSheet("background-color: white;\n"
"border-radius: 4px;\n"
"color: #232946;\n"
"font-size: 14px;\n"
"border: 1px solid #ccc;\n"
"")
        self.contentField.setObjectName("contentField")
        self.verticalLayout.addWidget(self.contentField)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.canelButton = QtWidgets.QPushButton(self.widget)
        self.canelButton.setStyleSheet("QPushButton {\n"
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
        self.canelButton.setObjectName("canelButton")
        self.horizontalLayout_2.addWidget(self.canelButton)
        self.saveButton = QtWidgets.QPushButton(self.widget)
        self.saveButton.setStyleSheet("QPushButton {\n"
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
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.boldButton.setText(_translate("Dialog", "B"))
        self.italicButton.setText(_translate("Dialog", "I"))
        self.colorButton.setText(_translate("Dialog", "Цвет"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.canelButton.setText(_translate("Dialog", "Отменить"))
        self.saveButton.setText(_translate("Dialog", "Сохранить"))
