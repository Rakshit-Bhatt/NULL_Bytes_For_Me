# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuessGame_dark.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):
    low_number = 1
    high_number = 10
    guess_left = 5
    hidden_number = random.randint(low_number, high_number)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 396)
        MainWindow.setStyleSheet("background-color: rgb(15, 15, 15);\n"
"color: rgb(255, 255, 255);")

        
        #ADDITION LINES TO PROVIDE TRANSLUCENCY AND FRAMELESS TEXTURE
        
        #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.round_label = QtWidgets.QLabel(self.centralwidget)
        self.round_label.setGeometry(QtCore.QRect(60, 1, 100, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.round_label.setFont(font)
        self.round_label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\"")
        self.round_label.setAlignment(QtCore.Qt.AlignCenter)
        self.round_label.setObjectName("round_label")
        self.highscore_label = QtWidgets.QLabel(self.centralwidget)
        self.highscore_label.setGeometry(QtCore.QRect(211, 1, 201, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.highscore_label.setFont(font)
        self.highscore_label.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\"")
        self.highscore_label.setAlignment(QtCore.Qt.AlignCenter)
        self.highscore_label.setObjectName("highscore_label")
        self.round_count_label = QtWidgets.QLabel(self.centralwidget)
        self.round_count_label.setGeometry(QtCore.QRect(60, 50, 100, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.round_count_label.setFont(font)
        self.round_count_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.round_count_label.setStyleSheet("color:rgb(255, 255, 0);\n"
"font: 75 25pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.round_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.round_count_label.setObjectName("round_count_label")
        self.highscore_count_label = QtWidgets.QLabel(self.centralwidget)
        self.highscore_count_label.setGeometry(QtCore.QRect(260, 50, 100, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.highscore_count_label.setFont(font)
        self.highscore_count_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.highscore_count_label.setStyleSheet("color:rgb(255, 255, 0);\n"
"font: 75 25pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.highscore_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.highscore_count_label.setObjectName("highscore_count_label")
        self.guess_info = QtWidgets.QLabel(self.centralwidget)
        self.guess_info.setGeometry(QtCore.QRect(10, 140, 401, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.guess_info.setFont(font)
        self.guess_info.setAlignment(QtCore.Qt.AlignCenter)
        self.guess_info.setObjectName("guess_info")
        self.entry_box = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_box.setGeometry(QtCore.QRect(60, 210, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.entry_box.setFont(font)
        self.entry_box.setObjectName("entry_box")
        self.hint = QtWidgets.QLabel(self.centralwidget)
        self.hint.setGeometry(QtCore.QRect(60, 280, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.hint.setFont(font)
        self.hint.setStyleSheet("")
        self.hint.setAlignment(QtCore.Qt.AlignLeft)
        self.hint.setObjectName("hint")
        self.guess_button = QtWidgets.QPushButton(self.centralwidget)
        self.guess_button.setGeometry(QtCore.QRect(60, 240, 90, 26))
        self.guess_button.setStyleSheet("QPushButton {\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.guess_button.setObjectName("guess_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # linked buttons
        self.guess_button.clicked.connect(self.guess_number)
        self.entry_box.returnPressed.connect(self.guess_number)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.round_label.setText(_translate("MainWindow", "Round"))
        self.highscore_label.setText(_translate("MainWindow", "High Score"))
        self.round_count_label.setText(_translate("MainWindow", "1"))
        self.highscore_count_label.setText(_translate("MainWindow", "1"))
        self.guess_info.setText(_translate("MainWindow", f"Guess a number between {self.low_number} and {self.high_number}.\n"
f"{self.guess_left} Guesses Left"))

        self.hint.setText(_translate("MainWindow", ""))
        self.guess_button.setText(_translate("MainWindow", "Guess"))

    def guess_number(self):
        guess = self.entry_box.text()
        try:
            guess = int(guess)
            if guess == self.hidden_number:
                self.high_number = self.high_number * 2
                new_round = int(self.round_count_label.text()) + 1
                self.round_count_label.setText(str(new_round))
                self.guess_left = 5
                self.hidden_number = random.randint(self.low_number, self.high_number)
                self.guess_info.setText(f"Guess a number between {self.low_number} and {self.high_number}.\n{self.guess_left} Guesses Left")
                self.entry_box.setText("")
                self.hint.setText(f"Nice! Now Try {self.low_number} - {self.high_number}")
            elif self.guess_left > 1:
                if guess < self.hidden_number:
                    self.hint.setText(f"{guess} is low dude.....")
                else:
                    self.hint.setText(f"{guess} is high dude.....")
                self.guess_left -= 1
                self.entry_box.setText("")
                self.guess_info.setText(f"Guess a number between {self.low_number} and {self.high_number}.\n{self.guess_left} Guesses Left")
            else:
                self.low_number = 1
                self.high_number = 10
                self.guess_left = 5
                self.hidden_number = random.randint(self.low_number, self.high_number)
                self.guess_info.setText(f"Guess a number between {self.low_number} and {self.high_number}.\n{self.guess_left} Guesses Left")
                self.entry_box.setText("")
                self.hint.setText(f"YOU LOSE! The number is {self.hidden_number}\nTrying to make this easy for you again.")

                new_score = int(self.round_count_label.text())
                high_score = int(self.highscore_count_label.text())
                self.round_count_label.setText("1")
                if new_score > high_score:
                    self.highscore_count_label.setText(str(new_score))

        except ValueError:
            self.hint.setText("What? Hey you typed non-integer type!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
