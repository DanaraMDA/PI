# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Универ\Программная инженерия\Интерфейс\authorizationwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_authorization_window(object):
    def setupUi(self, authorization_window):
        authorization_window.setObjectName("authorization_window")
        authorization_window.resize(481, 271)
        authorization_window.setAutoFillBackground(False)
        authorization_window.setStyleSheet("background-color: rgb(51, 102, 204);")
        self.centralwidget = QtWidgets.QWidget(authorization_window)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 100, 221, 24))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 103, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 143, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 140, 221, 24))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(175, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(102, 102, 102);\n"
"border: 2px solid rgb(102, 102, 102);\n"
"border-radius: 6px;")
        self.pushButton.setObjectName("pushButton")
        authorization_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(authorization_window)
        QtCore.QMetaObject.connectSlotsByName(authorization_window)

    def retranslateUi(self, authorization_window):
        _translate = QtCore.QCoreApplication.translate
        authorization_window.setWindowTitle(_translate("authorization_window", "MainWindow"))
        self.label.setText(_translate("authorization_window", "Логин"))
        self.label_2.setText(_translate("authorization_window", "Пароль"))
        self.label_3.setText(_translate("authorization_window", "Авторизируйтесь в системе"))
        self.pushButton.setText(_translate("authorization_window", "Войти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    authorization_window = QtWidgets.QMainWindow()
    ui = Ui_authorization_window()
    ui.setupUi(authorization_window)
    authorization_window.show()
    sys.exit(app.exec_())

