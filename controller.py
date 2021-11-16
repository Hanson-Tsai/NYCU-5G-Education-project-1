from pygame import mixer
from PyQt5 import QtWidgets, QtGui, QtCore, QtTest
from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        # in python3, super(Class, self).xxx = super().xxx
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        # TODO
        self.ui.PlaySong1.clicked.connect(self.playingSong1)
        self.ui.PlaySong2.clicked.connect(self.playingSong2)
        self.ui.PlaySong3.clicked.connect(self.playingSong3)
        
    def playingSong1(self):
        #read file
        f = open('./lyrics/happybirthday.txt', 'r')
        lines = f.read()
        f.close
        with open("./beats/happybirthday_beats.txt", "r") as f:
                beats = f.read()
                beats = [ int(x) for x in beats.split() ]
        #initialize
        index = 0
        tmp = []
        #play music
        mixer.init()
        mixer.music.load('C:/Users/User/project1/music/happybirthday.mp3')
        mixer.music.play()
        #show the lyric
        self.ui.LyricDisplay.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
        for line in lines:
            if (line != "\n"):
                tmp.append(line)
            else:
                string = ''.join(tmp)
                self.ui.LyricDisplay.setText(string)
                QtTest.QTest.qWait(int(beats[index])) # msec
                tmp = []
                index = index + 1
        self.ui.LyricDisplay.setStyleSheet("background-color: yellow; border: 1px solid black;")
        self.ui.LyricDisplay.setText("Let\'s pick a song to play")
        
    
    def playingSong2(self):
        #read file
        f = open('./lyrics/twotigger.txt', 'r')
        lines = f.read()
        f.close
        with open("./beats/twotigger_beats.txt", "r") as f:
                beats = f.read()
                beats = [ int(x) for x in beats.split() ]
        #initialize
        index = 0
        tmp = []
        #play music
        #mixer.init()
        #mixer.music.load('C:/Users/User/project1/happybirthday.mp3')
        #mixer.music.play()
        #show the lyric
        self.ui.LyricDisplay.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
        for line in lines:
            if (line != "\n"):
                tmp.append(line)
            else:
                string = ''.join(tmp)
                self.ui.LyricDisplay.setText(string)
                QtTest.QTest.qWait(int(beats[index])) # msec
                tmp = []
                index = index + 1
        self.ui.LyricDisplay.setStyleSheet("background-color: yellow; border: 1px solid black;")
        self.ui.LyricDisplay.setText("Let\'s pick a song to play")
        
    def playingSong3(self):
        #read file
        f = open('./lyrics/littlestar.txt', 'r')
        lines = f.read()
        f.close
        with open("./beats/littlestar_beats.txt", "r") as f:
                beats = f.read()
                beats = [ int(x) for x in beats.split() ]
        #initialize
        index = 0
        tmp = []
        #play music
        #mixer.init()
        #mixer.music.load('C:/Users/User/project1/happybirthday.mp3')
        #mixer.music.play()
        #show the lyric
        self.ui.LyricDisplay.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
        for line in lines:
            if (line != "\n"):
                tmp.append(line)
            else:
                string = ''.join(tmp)
                self.ui.LyricDisplay.setText(string)
                QtTest.QTest.qWait(int(beats[index])) # msec
                tmp = []
                index = index + 1
        self.ui.LyricDisplay.setStyleSheet("background-color: yellow; border: 1px solid black;")
        self.ui.LyricDisplay.setText("Let\'s pick a song to play")

    
    
    
    

