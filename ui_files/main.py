# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Main(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 532)
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setGeometry(QtCore.QRect(20, 270, 131, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(0, 132, 255);\n"
                                        "    border-radius: 7px;\n"
                                        "    color: #fff;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(0, 166, 255);\n"
                                        "}\n"
                                        "")
        self.searchButton.setObjectName("searchButton")
        self.titleEdit = QtWidgets.QLineEdit(Form)
        self.titleEdit.setGeometry(QtCore.QRect(20, 90, 131, 20))
        self.titleEdit.setStyleSheet("border: 1px solid rgb(0, 132, 255);\n"
                                     "border-radius: 10px;")
        self.titleEdit.setObjectName("titleEdit")
        self.subjectEdit = QtWidgets.QLineEdit(Form)
        self.subjectEdit.setGeometry(QtCore.QRect(20, 160, 131, 20))
        self.subjectEdit.setStyleSheet("border: 1px solid rgb(0, 132, 255);\n"
                                       "border-radius: 10px;")
        self.subjectEdit.setObjectName("subjectEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #565656;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #565656;")
        self.label_3.setObjectName("label_3")
        self.classEdit = QtWidgets.QSpinBox(Form)
        self.classEdit.setGeometry(QtCore.QRect(20, 220, 41, 16))
        self.classEdit.setStyleSheet("QSpinBox{\n"
                                     "    border: 1px solid rgb(0, 132, 255);\n"
                                     "    border-radius: 7px;\n"
                                     "}\n"
                                     "QSpinBox::up-button {\n"
                                     "    border: 1px solid rgb(0, 132, 255);\n"
                                     "     border-radius: 0 1px 1px 0;\n"
                                     "}\n"
                                     "QSpinBox::down-button {\n"
                                     "     border: 1px solid rgb(0, 132, 255);\n"
                                     "     border-radius: 0 1px 1px 0;\n"
                                     "}")
        self.classEdit.setObjectName("classEdit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #565656;")
        self.label_4.setObjectName("label_4")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(230, 60, 601, 471))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 50, 231, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(620, 0, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(770, 70, 31, 33))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("QPushButton {\n"
                                     "    background-color: rgb(0, 132, 255);\n"
                                     "    border-radius: 7px;\n"
                                     "    color: #fff;\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(0, 166, 255);\n"
                                     "}\n"
                                     "")
        self.addButton.setObjectName("addButton")
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setGeometry(QtCore.QRect(540, 12, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("QPushButton{\n"
                                       "    border: none;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "    color: rgb(0, 132, 255);\n"
                                       "}")
        self.loginButton.setObjectName("loginButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(638, 20, 131, 22))
        self.comboBox.setStyleSheet("QComboBox{\n"
                                    "    border: 1px solid rgb(0, 132, 255);\n"
                                    "    border-radius: 7px;\n"
                                    "}\n"
                                    "QComboBox::drop-down {\n"
                                    "    border: 1px solid rgb(0, 132, 255);\n"
                                    "    border-radius: 0 1px 1px 0;\n"
                                    "}\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.confirmSettingsButton = QtWidgets.QPushButton(Form)
        self.confirmSettingsButton.setGeometry(QtCore.QRect(780, 20, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.confirmSettingsButton.setFont(font)
        self.confirmSettingsButton.setStyleSheet("QPushButton {\n"
                                                 "    background-color: rgb(0, 132, 255);\n"
                                                 "    border-radius: 7px;\n"
                                                 "    color: #fff;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "    background-color: rgb(0, 166, 255);\n"
                                                 "}\n"
                                                 "")
        self.confirmSettingsButton.setObjectName("confirmSettingsButton")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(20, 10, 41, 41))
        self.logo.setText("")
        self.logo.setObjectName("logo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.searchButton.setText(_translate("Form", "Искать"))
        self.label_2.setText(_translate("Form", "Название"))
        self.label_3.setText(_translate("Form", "Предмет"))
        self.label_4.setText(_translate("Form", "Класс"))
        self.addButton.setText(_translate("Form", "+"))
        self.loginButton.setText(_translate("Form", "Войти"))
        self.comboBox.setItemText(0, _translate("Form", "..."))
        self.comboBox.setItemText(1, _translate("Form", "Избранные олимпиады"))
        self.comboBox.setItemText(2, _translate("Form", "Выйти"))
        self.comboBox.setItemText(3, _translate("Form", "Удалить аккаунт"))
        self.confirmSettingsButton.setText(_translate("Form", "✔"))