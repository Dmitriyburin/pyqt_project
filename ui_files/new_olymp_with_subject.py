# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_olymp_with_subject.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class NewOlympSubject(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 563)
        self.linkEdit = QtWidgets.QLineEdit(Form)
        self.linkEdit.setGeometry(QtCore.QRect(22, 280, 271, 20))
        self.linkEdit.setStyleSheet("border: 1px solid rgb(0, 132, 255);\n"
                                    "border-radius: 10px;")
        self.linkEdit.setObjectName("linkEdit")
        self.titleEdit = QtWidgets.QLineEdit(Form)
        self.titleEdit.setGeometry(QtCore.QRect(22, 90, 191, 20))
        self.titleEdit.setStyleSheet("border: 1px solid rgb(0, 132, 255);\n"
                                     "border-radius: 10px;")
        self.titleEdit.setObjectName("titleEdit")
        self.classEdit = QtWidgets.QSpinBox(Form)
        self.classEdit.setGeometry(QtCore.QRect(20, 150, 61, 21))
        self.classEdit.setStyleSheet("QSpinBox{\n"
                                     "    border: 1px solid rgb(0, 132, 255);\n"
                                     "    border-radius: 8px;\n"
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
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setGeometry(QtCore.QRect(20, 510, 361, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(0, 132, 255);\n"
                                      "    border-radius: 7px;\n"
                                      "    color: #fff;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(0, 166, 255);\n"
                                      "}\n"
                                      "")
        self.saveButton.setObjectName("saveButton")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(20, 210, 110, 22))
        self.dateEdit.setStyleSheet("QDateEdit{\n"
                                    "    border-radius: 10px;\n"
                                    "    border: 1px solid rgb(0, 132, 255);\n"
                                    "}\n"
                                    "\n"
                                    "QDateEdit::up-button {\n"
                                    "    border: 1px solid rgb(0, 132, 255);\n"
                                    "     border-radius: 0 1px 1px 0;\n"
                                    "}\n"
                                    "QDateEdit::down-button {\n"
                                    "     border: 1px solid rgb(0, 132, 255);\n"
                                    "     border-radius: 0 1px 1px 0;\n"
                                    "}")
        self.dateEdit.setObjectName("dateEdit")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 340, 361, 131))
        self.frame.setStyleSheet("background-color: rgb(0, 132, 255);\n"
                                 "border-radius: 30px;\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.descrPlainEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.descrPlainEdit.setStyleSheet("color: #fff;")
        self.descrPlainEdit.setPlainText("")
        self.descrPlainEdit.setObjectName("descrPlainEdit")
        self.gridLayout.addWidget(self.descrPlainEdit, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #fff;")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #fff;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.durPlainEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.durPlainEdit.setStyleSheet("color: #fff;")
        self.durPlainEdit.setObjectName("durPlainEdit")
        self.gridLayout.addWidget(self.durPlainEdit, 1, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(169, 340, 31, 131))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(20, 190, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #565656;")
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 130, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #565656;")
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 271, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #565656;")
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #565656;")
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 389, 361, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.subjectEdit = QtWidgets.QLineEdit(Form)
        self.subjectEdit.setGeometry(QtCore.QRect(22, 30, 191, 20))
        self.subjectEdit.setStyleSheet("border: 1px solid rgb(0, 132, 255);\n"
                                       "border-radius: 10px;")
        self.subjectEdit.setObjectName("subjectEdit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #565656;")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.saveButton.setText(_translate("Form", "Сохранить"))
        self.label_7.setText(_translate("Form", "  Описание"))
        self.label_5.setText(_translate("Form", "  Продолжительность "))
        self.label_9.setText(_translate("Form", "Дата проведения"))
        self.label_8.setText(_translate("Form", "Класс"))
        self.label_3.setText(_translate("Form", "Ссылка на официальный сайт олимпиады"))
        self.label_2.setText(_translate("Form", "Название"))
        self.label_4.setText(_translate("Form", "Предмет"))
