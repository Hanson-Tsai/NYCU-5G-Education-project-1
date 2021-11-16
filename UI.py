# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Connect = QtWidgets.QPushButton(self.centralwidget)
        self.Connect.setGeometry(QtCore.QRect(0, 0, 801, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.Connect.setFont(font)
        self.Connect.setObjectName("Connect")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 70, 801, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.SongButtomList = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.SongButtomList.setContentsMargins(0, 0, 0, 0)
        self.SongButtomList.setObjectName("SongButtomList")
        self.PlaySong1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.PlaySong1.setFont(font)
        self.PlaySong1.setObjectName("PlaySong1")
        self.SongButtomList.addWidget(self.PlaySong1)
        self.PlaySong2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.PlaySong2.setFont(font)
        self.PlaySong2.setObjectName("PlaySong2")
        self.SongButtomList.addWidget(self.PlaySong2)
        self.PlaySong3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.PlaySong3.setFont(font)
        self.PlaySong3.setObjectName("PlaySong3")
        self.SongButtomList.addWidget(self.PlaySong3)
        self.LyricDisplay = QtWidgets.QLabel(self.centralwidget)
        self.LyricDisplay.setGeometry(QtCore.QRect(10, 290, 781, 121))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.LyricDisplay.setFont(font)
        self.LyricDisplay.setObjectName("LyricDisplay")
        self.LyricDisplay.setStyleSheet("background-color: yellow; border: 1px solid black;")
        self.LyricDisplay.setAlignment(QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Connect.setText(_translate("MainWindow", "Connect"))
        self.PlaySong1.setText(_translate("MainWindow", "Song 1"))
        self.PlaySong2.setText(_translate("MainWindow", "Song 2"))
        self.PlaySong3.setText(_translate("MainWindow", "Song 3"))
        self.LyricDisplay.setText(_translate("MainWindow", "Let\'s pick a song to play"))

