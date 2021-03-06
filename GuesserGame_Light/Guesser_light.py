# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuessGame.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


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
        
        #ADDITION LINES TO PROVIDE TRANSLUCENCY AND FRAMELESS TEXTURE
        
        #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.round_label = QtWidgets.QLabel(self.centralwidget)
        self.round_label.setGeometry(QtCore.QRect(60, 20, 100, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.round_label.setFont(font)
        self.round_label.setAlignment(QtCore.Qt.AlignCenter)
        self.round_label.setObjectName("round_label")
        self.highscore_label = QtWidgets.QLabel(self.centralwidget)
        self.highscore_label.setGeometry(QtCore.QRect(260, 20, 125, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.highscore_label.setFont(font)
        self.highscore_label.setAlignment(QtCore.Qt.AlignCenter)
        self.highscore_label.setObjectName("highscore_label")
        self.round_count_label = QtWidgets.QLabel(self.centralwidget)
        self.round_count_label.setGeometry(QtCore.QRect(60, 50, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.round_count_label.setFont(font)
        self.round_count_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.round_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.round_count_label.setObjectName("round_count_label")
        self.highscore_count_label = QtWidgets.QLabel(self.centralwidget)
        self.highscore_count_label.setGeometry(QtCore.QRect(260, 50, 110, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.highscore_count_label.setFont(font)
        self.highscore_count_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.highscore_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.highscore_count_label.setObjectName("highscore_count_label")
        self.guess_info = QtWidgets.QLabel(self.centralwidget)
        self.guess_info.setGeometry(QtCore.QRect(60, 170, 300, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.guess_info.setFont(font)
        self.guess_info.setAlignment(QtCore.Qt.AlignCenter)
        self.guess_info.setObjectName("guess_info")
        self.entry_box = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_box.setGeometry(QtCore.QRect(60, 230, 300, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.entry_box.setFont(font)
        self.entry_box.setObjectName("entry_box")
        self.hint = QtWidgets.QLabel(self.centralwidget)
        self.hint.setGeometry(QtCore.QRect(60, 300, 300, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.hint.setFont(font)
        self.hint.setAlignment(QtCore.Qt.AlignCenter)
        self.hint.setObjectName("hint")
        self.guess_button = QtWidgets.QPushButton(self.centralwidget)
        self.guess_button.setGeometry(QtCore.QRect(60, 260, 75, 23))
        self.guess_button.setObjectName("guess_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 21))
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
