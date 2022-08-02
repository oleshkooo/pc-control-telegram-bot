from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon,QAction,QMenu,qApp,QMainWindow
from resource import resource
import psutil
import time
from threading import Thread
import subprocess
import pymysql
import wmi
import os
import pickle



class Ui_MainWindow(QMainWindow):
    tray_icon = None
    
    def setupUi(self, MainWindow):
        QMainWindow.__init__(self)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWindows = QtWidgets.QGroupBox(self.centralwidget)
        self.MainWindows.setGeometry(QtCore.QRect(104, -2, 1100, 805))
        self.MainWindows.setStyleSheet("\n"
"QGroupBox\n"
"{\n"
"    \n"
"    background-image: url(:/backgrounds/background.png);\n"
"}\n"
"")
        self.MainWindows.setTitle("")
        self.MainWindows.setObjectName("MainWindows")
        self.HomeWindow = QtWidgets.QGroupBox(self.MainWindows)
        self.HomeWindow.setGeometry(QtCore.QRect(0, 0, 1100, 802))
        self.HomeWindow.setTitle("")
        self.HomeWindow.setObjectName("HomeWindow")
        self.HomeWindow.show()
        self.imageBot = QtWidgets.QFrame(self.HomeWindow)
        self.imageBot.setGeometry(QtCore.QRect(417, 128, 266, 266))
        self.imageBot.setStyleSheet("background-image: url(:/backgrounds/ImageBot.png);")
        self.imageBot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageBot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageBot.setObjectName("imageBot")
        
        
        
        ##############################################################################################################*
        self.msgStatusBot = QtWidgets.QFrame(self.HomeWindow)
        self.msgStatusBot.setGeometry(QtCore.QRect(388, 476, 320, 88))
        self.msgStatusBot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgStatusBot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgStatusBot.setObjectName("msgStatusBot")
        

        self.btnTurn = QtWidgets.QPushButton(self.HomeWindow)
        self.btnTurn.setGeometry(QtCore.QRect(388, 576, 320, 64))   
        self.btnTurn.setText("")
        self.btnTurn.setIconSize(QtCore.QSize(320, 64))
        self.btnTurn.setObjectName("btnTurn")
         
        
       


        
        self.SettingsWindow = QtWidgets.QGroupBox(self.MainWindows)
        self.SettingsWindow.setGeometry(QtCore.QRect(0, 0, 1100, 805))
        self.SettingsWindow.setTitle("")
        self.SettingsWindow.setObjectName("SettingsWindow")
        self.ChangeDataWindow = QtWidgets.QGroupBox(self.MainWindows)
        self.ChangeDataWindow.setGeometry(QtCore.QRect(0, 0, 1100, 805))
        self.ChangeDataWindow.setTitle("")
        self.ChangeDataWindow.setObjectName("ChangeData")
        self.labelEnterID = QtWidgets.QLabel(self.ChangeDataWindow)
        self.labelEnterID.setGeometry(QtCore.QRect(136, 303, 181, 58))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.labelEnterID.setFont(font)
        self.labelEnterID.setStyleSheet("border-radius: 29px;\n"
"background-color:#E3F0E6 ;")
        self.labelEnterID.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEnterID.setObjectName("labelEnterID")
        self.labelEnterToken = QtWidgets.QLabel(self.ChangeDataWindow)
        self.labelEnterToken.setGeometry(QtCore.QRect(616, 303, 218, 58))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        self.labelEnterToken.setFont(font)
        self.labelEnterToken.setStyleSheet("border-radius: 29px;\n"
"background-color:#E3F0E6 ;")
        self.labelEnterToken.setAlignment(QtCore.Qt.AlignCenter)
        self.labelEnterToken.setObjectName("labelEnterToken")
        self.lineChangeUsername = QtWidgets.QLineEdit(self.ChangeDataWindow)
        self.lineChangeUsername.setGeometry(QtCore.QRect(215, 368, 241, 58))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineChangeUsername.setFont(font)
        self.lineChangeUsername.setAutoFillBackground(False)
        self.lineChangeUsername.setStyleSheet("border-radius: 29px;\n"
"background-color: #E7FDCC;\n"
"color: #858D98;\n"
"")
        self.lineChangeUsername.setText("")
        self.lineChangeUsername.setMaxLength(10)
        self.lineChangeUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.lineChangeUsername.setDragEnabled(False)
        self.lineChangeUsername.setReadOnly(False)
        self.lineChangeUsername.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineChangeUsername.setObjectName("lineChangeUsername")
        self.lineChangeToken = QtWidgets.QLineEdit(self.ChangeDataWindow)
        self.lineChangeToken.setGeometry(QtCore.QRect(695, 368, 241, 58))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineChangeToken.setFont(font)
        self.lineChangeToken.setMouseTracking(True)
        self.lineChangeToken.setStyleSheet("border-radius: 29px;\n"
"background-color: #E7FDCC;\n"
"color: #858D98;\n"
"")
        self.lineChangeToken.setText("")
        self.lineChangeToken.setMaxLength(70)
        self.lineChangeToken.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineChangeToken.setAlignment(QtCore.Qt.AlignCenter)
        self.lineChangeToken.setObjectName("lineChangeToken")
        self.btnChangeUsername = QtWidgets.QPushButton(self.ChangeDataWindow)
        self.btnChangeUsername.setGeometry(QtCore.QRect(136, 438, 320, 64))
        self.btnChangeUsername.setStyleSheet("QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-image: url(:/btnBackgrounds/btnChangeID.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 15px;    \n"
"}    \n"
"")
        self.btnChangeUsername.setText("")
        self.btnChangeUsername.setObjectName("btnChangeUsername")
        
        
        self.btnChangeToken = QtWidgets.QPushButton(self.ChangeDataWindow)
        self.btnChangeToken.setGeometry(QtCore.QRect(616, 438, 320, 64))
        
        self.btnChangeToken.setStyleSheet("QPushButton\n"
"{\n"
"    border-radius: 10px;\n"
"    background-image: url(:/btnBackgrounds/btnChangeToken.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius: 15px;    \n"
"}    \n"
"")
        self.btnChangeToken.setText("")
        self.btnChangeToken.setObjectName("btnChangeToken")
        self.InfoWindow = QtWidgets.QGroupBox(self.MainWindows)
        self.InfoWindow.setGeometry(QtCore.QRect(0, 0, 1100, 805))
        self.InfoWindow.setTitle("")
        self.InfoWindow.setObjectName("InfoWindow")
        self.imageOleshko = QtWidgets.QFrame(self.InfoWindow)
        self.imageOleshko.setGeometry(QtCore.QRect(206, 260, 266, 265))
        self.imageOleshko.setStyleSheet("background-image: url(:/developers/imageOleshko.png);")
        self.imageOleshko.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageOleshko.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageOleshko.setObjectName("imageOleshko")
        self.imageBLVX = QtWidgets.QFrame(self.InfoWindow)
        self.imageBLVX.setGeometry(QtCore.QRect(630, 260, 266, 265))
        self.imageBLVX.setStyleSheet("background-image: url(:/developers/imageBLVX.png);")
        self.imageBLVX.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageBLVX.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageBLVX.setObjectName("imageBLVX")
        self.msgDevelopedBy = QtWidgets.QLabel(self.InfoWindow)
        self.msgDevelopedBy.setGeometry(QtCore.QRect(459, 138, 185, 58))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.msgDevelopedBy.setFont(font)
        self.msgDevelopedBy.setStyleSheet("border-radius: 29px;\n"
"background-color: rgb(227, 240, 230);")
        self.msgDevelopedBy.setAlignment(QtCore.Qt.AlignCenter)
        self.msgDevelopedBy.setObjectName("msgDevelopedBy")
        self.msgOleshko = QtWidgets.QLabel(self.InfoWindow)
        self.msgOleshko.setGeometry(QtCore.QRect(258, 546, 163, 58))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.msgOleshko.setFont(font)
        self.msgOleshko.setStyleSheet("border-radius: 29px;\n"
"background-color: rgb(227, 240, 230);")
        self.msgOleshko.setAlignment(QtCore.Qt.AlignCenter)
        self.msgOleshko.setObjectName("msgOleshko")
        self.msgBLVX = QtWidgets.QLabel(self.InfoWindow)
        self.msgBLVX.setGeometry(QtCore.QRect(705, 546, 116, 58))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.msgBLVX.setFont(font)
        self.msgBLVX.setStyleSheet("border-radius: 29px;\n"
"background-color: rgb(227, 240, 230);")
        self.msgBLVX.setAlignment(QtCore.Qt.AlignCenter)
        self.msgBLVX.setObjectName("msgBLVX")
        self.SettingsWindow.raise_()
        self.InfoWindow.raise_()
        self.ChangeDataWindow.raise_()
        self.HomeWindow.raise_()
        self.menu = QtWidgets.QGroupBox(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 0, 104, 805))
        self.menu.setStyleSheet("QGroupBox\n"
"{\n"
"    background-color: #E3F0E6;\n"
"}\n"
"QPushButton\n"
"{\n"
"    border: none;\n"
"}\n"
"")
        self.menu.setTitle("")
        self.menu.setObjectName("menu")
        self.btnHome = QtWidgets.QPushButton(self.menu)
        self.btnHome.setGeometry(QtCore.QRect(31, 40, 40, 40))
        self.btnHome.setStyleSheet("QPushButton\n"
"{\n"
"    background-image: url(:/menuIcons/iconHomeBlue.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    background-image: url(:/menuIcons/iconHomeSelected.png);\n"
"}")
        self.btnHome.setInputMethodHints(QtCore.Qt.ImhExclusiveInputMask)
        self.btnHome.setText("")
        self.btnHome.setIconSize(QtCore.QSize(40, 40))
        self.btnHome.setCheckable(True)
        self.btnHome.setChecked(True)
        self.btnHome.setObjectName("btnHome")
        self.btnChangeData = QtWidgets.QPushButton(self.menu)
        self.btnChangeData.setGeometry(QtCore.QRect(31, 120, 40, 40))
        self.btnChangeData.setStyleSheet("QPushButton\n"
"{\n"
"    background-image: url(:/menuIcons/iconKey.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    background-image:url(:/menuIcons/iconKeySelected.png);\n"
"}")
        self.btnChangeData.setText("")
        self.btnChangeData.setIconSize(QtCore.QSize(40, 40))
        self.btnChangeData.setObjectName("btnChangeData")
        self.btnInfo = QtWidgets.QPushButton(self.menu)
        self.btnInfo.setGeometry(QtCore.QRect(31, 200, 40, 40))
        self.btnInfo.setStyleSheet("QPushButton\n"
"{\n"
"    background-image: url(:/menuIcons/iconInfo.png);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    \n"
"    background-image:url(:/menuIcons/iconInfoSelected.png)\n"
"}")
        self.btnInfo.setText("")
        self.btnInfo.setIconSize(QtCore.QSize(40, 40))
        self.btnInfo.setObjectName("btnInfo")
        self.AuthorizedWindows = QtWidgets.QGroupBox(self.centralwidget)
        self.AuthorizedWindows.setGeometry(QtCore.QRect(-2, -2, 1205, 805))
        self.AuthorizedWindows.setStyleSheet("background-image: url(:/backgrounds/background.png);\n"
"")
        self.AuthorizedWindows.setTitle("")
        self.AuthorizedWindows.setObjectName("AuthorizedWindows")
        self.WelcomeWindow = QtWidgets.QGroupBox(self.AuthorizedWindows)
        self.WelcomeWindow.setGeometry(QtCore.QRect(0, 0, 1205, 805))
        self.WelcomeWindow.setTitle("")
        self.WelcomeWindow.setObjectName("WelcomeWindow")
        self.msgHi = QtWidgets.QFrame(self.WelcomeWindow)
        self.msgHi.setGeometry(QtCore.QRect(395, 470, 410, 118))
        self.msgHi.setStyleSheet("border-radius: 16px;\n"
"background-image: url(:/msgBackgrounds/msgHi.png);")
        self.msgHi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgHi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgHi.setObjectName("msgHi")
        self.botIconPg1 = QtWidgets.QFrame(self.WelcomeWindow)
        self.botIconPg1.setGeometry(QtCore.QRect(467, 90, 267, 267))
        self.botIconPg1.setStyleSheet("background-image: url(:/backgrounds/ImageBot.png);")
        self.botIconPg1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botIconPg1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botIconPg1.setObjectName("botIconPg1")
        self.btnNextPg1 = QtWidgets.QPushButton(self.WelcomeWindow)
        self.btnNextPg1.setGeometry(QtCore.QRect(395, 600, 411, 64))
        self.btnNextPg1.setStyleSheet("border: none;\n"
"border-radius: 10px;\n"
"background-image: url(:/btnBackgrounds/btnNextPg1.png);")
        self.btnNextPg1.setText("")
        self.btnNextPg1.setObjectName("btnNextPg1")
        self.EnterKeyWindow = QtWidgets.QGroupBox(self.AuthorizedWindows)
        self.EnterKeyWindow.setGeometry(QtCore.QRect(0, 0, 1205, 805))
        self.EnterKeyWindow.setTitle("")
        self.EnterKeyWindow.setObjectName("EnterKeyWindow")
        self.botIconPg3 = QtWidgets.QFrame(self.EnterKeyWindow)
        self.botIconPg3.setGeometry(QtCore.QRect(467, 90, 267, 267))
        self.botIconPg3.setStyleSheet("background-image: url(:/backgrounds/ImageBot.png);")
        self.botIconPg3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botIconPg3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botIconPg3.setObjectName("botIconPg3")
        self.msgGetKey = QtWidgets.QFrame(self.EnterKeyWindow)
        self.msgGetKey.setGeometry(QtCore.QRect(355, 405, 490, 172))
        self.msgGetKey.setStyleSheet("border-radius: 15px;\n"
"background-image: url(:/msgBackgrounds/msgGetKey.png);")
        self.msgGetKey.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgGetKey.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgGetKey.setObjectName("msgGetKey")
        self.btnNextPg3 = QtWidgets.QPushButton(self.EnterKeyWindow)
        self.btnNextPg3.setGeometry(QtCore.QRect(355, 665, 490, 64))
        self.btnNextPg3.setStyleSheet("border: none;\n"
"border-radius: 10px;\n"
"background-image: url(:/btnBackgrounds/btnNextPg3.png);")
        self.btnNextPg3.setText("")
        self.btnNextPg3.setObjectName("btnNextPg3")
        self.lineEditEnterKey = QtWidgets.QLineEdit(self.EnterKeyWindow)
        self.lineEditEnterKey.setGeometry(QtCore.QRect(355, 589, 490, 64))
        palette = QtGui.QPalette()
        self.lineEditEnterKey.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditEnterKey.setFont(font)
        self.lineEditEnterKey.setAutoFillBackground(False)
        self.lineEditEnterKey.setStyleSheet("border: none;\n"
"border-radius: 15px;\n"
"background-image: url(:/lineEdit/lineEditKey.png);")
        self.lineEditEnterKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditEnterKey.setObjectName("lineEditEnterKey")
        self.EnterTokenWindow = QtWidgets.QGroupBox(self.AuthorizedWindows)
        self.EnterTokenWindow.setGeometry(QtCore.QRect(0, 0, 1205, 805))
        self.EnterTokenWindow.setTitle("")
        self.EnterTokenWindow.setObjectName("EnterTokenWindow")
        self.botIconPg4 = QtWidgets.QFrame(self.EnterTokenWindow)
        self.botIconPg4.setGeometry(QtCore.QRect(467, 90, 267, 267))
        self.botIconPg4.setStyleSheet("background-image: url(:/backgrounds/ImageBot.png);")
        self.botIconPg4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botIconPg4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botIconPg4.setObjectName("botIconPg4")
        self.msgGetToken = QtWidgets.QFrame(self.EnterTokenWindow)
        self.msgGetToken.setGeometry(QtCore.QRect(155, 415, 891, 199))
        self.msgGetToken.setStyleSheet("border-radius: 16px;\n"
"background-image: url(:/msgBackgrounds/msgEnterToken.png);\n"
"")
        self.msgGetToken.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgGetToken.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgGetToken.setObjectName("msgGetToken")
        self.btnNextPg4 = QtWidgets.QPushButton(self.EnterTokenWindow)
        self.btnNextPg4.setGeometry(QtCore.QRect(797, 626, 249, 64))
        self.btnNextPg4.setStyleSheet("border: none;\n"
"border-radius: 16px;\n"
"background-image: url(:/btnBackgrounds/btnNextPg4.png);")
        self.btnNextPg4.setText("")
        self.btnNextPg4.setObjectName("btnNextPg4")
        self.lineEditEnterToken = QtWidgets.QLineEdit(self.EnterTokenWindow)
        self.lineEditEnterToken.setGeometry(QtCore.QRect(155, 626, 630, 64))
        palette = QtGui.QPalette()
        self.lineEditEnterToken.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditEnterToken.setFont(font)
        self.lineEditEnterToken.setAutoFillBackground(False)
        self.lineEditEnterToken.setStyleSheet("border: none;\n"
"border-radius: 15px;\n"
"background-image: url(:/lineEdit/lineEditToken.png);")
        self.lineEditEnterToken.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditEnterToken.setObjectName("lineEditEnterToken")
        self.EnterUsernameWindow = QtWidgets.QGroupBox(self.AuthorizedWindows)
        self.EnterUsernameWindow.setGeometry(QtCore.QRect(0, 0, 1205, 805))
        self.EnterUsernameWindow.setStyleSheet("QLabel{\n"
"    background-color: #FF0000;\n"
"}")
        self.EnterUsernameWindow.setTitle("")
        self.EnterUsernameWindow.setObjectName("EnterIDWindow")
        self.botIconPg5 = QtWidgets.QFrame(self.EnterUsernameWindow)
        self.botIconPg5.setGeometry(QtCore.QRect(467, 90, 267, 267))
        self.botIconPg5.setStyleSheet("background-image: url(:/backgrounds/ImageBot.png);")
        self.botIconPg5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botIconPg5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botIconPg5.setObjectName("botIconPg5")
        self.msgEnterUsername = QtWidgets.QFrame(self.EnterUsernameWindow)
        self.msgEnterUsername.setGeometry(QtCore.QRect(282, 415, 636, 91))
        self.msgEnterUsername.setStyleSheet("border-radius: 16px;\n"
"background-image: url(:/msgBackgrounds/msgEnterUsername.png);")
        self.msgEnterUsername.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgEnterUsername.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgEnterUsername.setObjectName("msgEnterUsername")
        self.btnNextPg5 = QtWidgets.QPushButton(self.EnterUsernameWindow)
        self.btnNextPg5.setGeometry(QtCore.QRect(606, 518, 312, 64))
        self.btnNextPg5.setStyleSheet("border: none;\n"
"background-image: url(:/btnBackgrounds/btnNextPg5.png);\n"
"border-radius: 16px;\n"
"")
        self.btnNextPg5.setText("")
        self.btnNextPg5.setObjectName("btnNextPg5")
        self.lineEditEnterUsername = QtWidgets.QLineEdit(self.EnterUsernameWindow)
        self.lineEditEnterUsername.setGeometry(QtCore.QRect(282, 518, 312, 63))
        palette = QtGui.QPalette()
        self.lineEditEnterUsername.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditEnterUsername.setFont(font)
        self.lineEditEnterUsername.setAutoFillBackground(False)
        self.lineEditEnterUsername.setStyleSheet("border: none;\n"
"border-radius: 15px;\n"
"background-image: url(:/lineEdit/lineEditUsername.png);")
        self.lineEditEnterUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditEnterUsername.setObjectName("lineEditEnterUsername")
        self.TermWindow = QtWidgets.QGroupBox(self.AuthorizedWindows)
        self.TermWindow.setGeometry(QtCore.QRect(0, 0, 1205, 805))
        self.TermWindow.setTitle("")
        self.TermWindow.setObjectName("TermWindow")
        self.botIconPg2 = QtWidgets.QFrame(self.TermWindow)
        self.botIconPg2.setGeometry(QtCore.QRect(467, 90, 267, 267))
        self.botIconPg2.setStyleSheet("background-image: url(:/backgrounds/ImageBot.png);")
        self.botIconPg2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botIconPg2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botIconPg2.setObjectName("botIconPg2")
        self.msgTerms = QtWidgets.QFrame(self.TermWindow)
        self.msgTerms.setGeometry(QtCore.QRect(304, 435, 592, 199))
        self.msgTerms.setStyleSheet("border-radius: 16px;\n"
"background-image: url(:/msgBackgrounds/msgTerms.png);")
        self.msgTerms.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgTerms.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgTerms.setObjectName("msgTerms")
        self.btnNextPg2 = QtWidgets.QPushButton(self.TermWindow)
        self.btnNextPg2.setGeometry(QtCore.QRect(304, 646, 592, 64))
        self.btnNextPg2.setStyleSheet("border: none;\n"
"border-radius: 10px;\n"
"background-image: url(:/btnBackgrounds/btnNextPg2.png);")
        self.btnNextPg2.setText("")
        self.btnNextPg2.setObjectName("btnNextPg2")
        self.TermWindow.raise_()
        self.EnterKeyWindow.raise_()
        self.EnterTokenWindow.raise_()
        self.EnterUsernameWindow.raise_()
        self.WelcomeWindow.raise_()
        self.AuthorizedWindows.raise_()
        self.MainWindows.raise_()
        self.menu.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelEnterID.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#222222;\">Change </span><span style=\" font-size:12pt; font-weight:600; color:#3478f7;\">ID</span></p></body></html>"))
        self.labelEnterToken.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#222222;\">Change </span><span style=\" font-size:12pt; font-weight:600; color:#3478f7;\">Token</span></p></body></html>"))
        self.lineChangeUsername.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Open Sans\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#858d98;\">Your ID</span></p></body></html>"))
        self.lineChangeUsername.setPlaceholderText(_translate("MainWindow", "Your ID"))
        self.lineChangeToken.setPlaceholderText(_translate("MainWindow", "Your TOKEN"))
        self.msgDevelopedBy.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#222222;\">Developed by:</span></p></body></html>"))
        self.msgOleshko.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#222222;\">@oleshko_o</span></p></body></html>"))
        self.msgBLVX.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#222222;\">@BLVX</span></p></body></html>"))
        self.lineEditEnterKey.setPlaceholderText(_translate("MainWindow", "Your KEY"))
        self.lineEditEnterToken.setPlaceholderText(_translate("MainWindow", "Your TOKEN"))
        self.lineEditEnterUsername.setPlaceholderText(_translate("MainWindow", "Your USERNAME"))
        
       
        
        #########################################################################################################################################################################*
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menuIcons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(icon)
        
        
      
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(qApp.quit)
        hide_action.triggered.connect(self.hide)
        
        tray_menu = QMenu()
        
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
        arrayWindows = [self.HomeWindow,self.ChangeDataWindow,self.InfoWindow,self.EnterKeyWindow,self.EnterTokenWindow,self.EnterUsernameWindow,self.WelcomeWindow,self.TermWindow]
        iconNames = ['Home','Key','Info']
        arrayBtn = [self.btnHome,self.btnChangeData,self.btnInfo]

        def ChangeWindow(self,window):
            for el in arrayWindows:
                if el != window:
                    el.hide()    
            window.show()
            
            if window == self.HomeWindow:
                name = 'Home'
            elif window == self.ChangeDataWindow:
                name = 'Key'
            else:
                name = 'Info'

            setStyles(name)
            
        def setStyles(name):
            i = 0
            for el in iconNames:
                if el != name:
                    style = getStyle(self,el,False)
                else:
                    style = getStyle(self,el,True)
                arrayBtn[i].setStyleSheet(style)    
                i += 1
        
        def getStyle(self,defaultName,flag):
            
            selectedName = defaultName
            
            if flag:
                defaultName += 'Blue'   
                
            return ("QPushButton\n{\nbackground-image: url(:/menuIcons/"
                     f"icon{defaultName}.png);\n"
                    "}\nQPushButton:hover{\nbackground-image:url(:/menuIcons/"
                    f"icon{selectedName}Selected.png);\n"
                    "}") 
                    
     
       
        
        
        self.btnTurn.clicked.connect(lambda: self.ChangeTurn())
        
        self.btnHome.clicked.connect(lambda: ChangeWindow(self,self.HomeWindow)) 
        self.btnChangeData.clicked.connect(lambda: ChangeWindow(self,self.ChangeDataWindow))
        self.btnInfo.clicked.connect(lambda: ChangeWindow(self,self.InfoWindow))
        
        self.btnChangeToken.clicked.connect(lambda: self.ChangeToken_process())
        self.btnChangeUsername.clicked.connect(lambda: self.ChangeUsername_process())

        self.MainWindows.hide()
        self.menu.hide()    
            
        for el in arrayWindows:
            el.hide()


        id = wmi.WMI().Win32_BaseBoard()[0].SerialNumber.strip()
        
        try:        
            connection = pymysql.connect(
                host = "sql11.freesqldatabase.com",
                port = 3306,
                user = "sql11509414",
                password = "alNPD6NZjz",
                database = "sql11509414",
                cursorclass = pymysql.cursors.DictCursor
            )
            with connection.cursor() as cursor:
                select_query = f'SELECT * FROM `data` WHERE `id` = "{id}"'
                cursor.execute(select_query)
                result = cursor.fetchall()
                if not result:
                    self.verificationUser()
                else:
                    self.menu.show()
                    self.MainWindows.show()
                    self.AuthorizedWindows.hide()
                    self.HomeWindow.show()
        except:
            print("error")

    def ChangeToken_process(self):
        TOKEN = self.lineChangeToken.text()
        _translate = QtCore.QCoreApplication.translate
        self.lineChangeToken.setText('')    
        if len(TOKEN) != 46:
            self.lineChangeToken.setPlaceholderText(_translate("MainWindow", "incorrect TOKEN"))
        else:
            self.lineChangeToken.setPlaceholderText(_translate("MainWindow", "success"))
            WriteToFile(TOKEN,None)

    def ChangeUsername_process(self):
        USERNAME = self.lineChangeUsername.text()
        _translate = QtCore.QCoreApplication.translate
        self.lineChangeUsername.setText('')    
        if len(USERNAME) < 5:
            self.lineChangeUsername.setPlaceholderText(_translate("MainWindow", "incorrect USERNAME"))
        else:
            self.lineChangeUsername.setPlaceholderText(_translate("MainWindow", "success"))
            WriteToFile(None,USERNAME)
    
    
    def StartBot(self):
            subprocess.call('cd .. && cd host && host.exe', shell = True)    
            
    def ChangeTurn(self):
        flag = False
        for proc in psutil.process_iter():
            if proc.name() == "host.exe":
                flag = True
                break
        
        if not flag:
            self.msgStatusBot.setStyleSheet("border-radius: 16px;\n"
                f"background-image: url(:/msgBackgrounds/msgBotStarting.png);")
            
            th = Thread(target = self.StartBot, args = (), daemon = True)
            th.start()
        else:
            self.msgStatusBot.setStyleSheet("border-radius: 16px;\n"
                f"background-image: url(:/msgBackgrounds/msgBotStopping.png);")
            
            subprocess.call('taskkill /f /im host.exe', shell = True)    
            
    def verificationUser(self):
        def welcomeWin_process():
            self.WelcomeWindow.show()
            self.btnNextPg1.clicked.connect(lambda: termsWin_process())
        
        def termsWin_process():
            self.WelcomeWindow.hide()
            self.TermWindow.show()
            
            self.btnNextPg2.clicked.connect(lambda: enterKeyWin_process())
        
            def enterKeyWin_process():
                self.TermWindow.hide()
                self.EnterKeyWindow.show()
                
                self.btnNextPg3.clicked.connect(lambda: checkKey())
                def checkKey():
                    try:        
                        connection = connectToDB()
                        
                        with connection.cursor() as cursor:
                            key = self.lineEditEnterKey.text()
                            select_query = f'SELECT * FROM `data` WHERE `_key` = "{key}"'
                            cursor.execute(select_query)
                            result = cursor.fetchall()
                            
                            _translate = QtCore.QCoreApplication.translate
                            self.lineEditEnterKey.clear()
                            if not result:
                                self.lineEditEnterKey.setPlaceholderText(_translate("MainWindow", "incorrect KEY"))
                            else:
                                id = wmi.WMI().Win32_BaseBoard()[0].SerialNumber.strip()
                                try:        
                                    connection = connectToDB()
                                    with connection.cursor() as cursor:
                                        insert_query = f'UPDATE `data` SET `id`= "{id}" WHERE `_key` = "{key}";'    
                                        cursor.execute(insert_query)
                                        connection.commit()
                                    enterTokenWin_process()

                                except:
                                    print("error")
                            
                    except Exception as e:
                        print(Exception, e)
                
        def enterTokenWin_process():
            self.EnterKeyWindow.hide()
            self.EnterTokenWindow.show()
            
            self.btnNextPg4.clicked.connect(lambda: checkToken())
            
            def checkToken():
                TOKEN = self.lineEditEnterToken.text()
                self.lineEditEnterToken.clear()
                if len(TOKEN) != 46:
                    _translate = QtCore.QCoreApplication.translate
                    self.lineEditEnterToken.setPlaceholderText(_translate("MainWindow", "incorrect TOKEN"))
                else:
                    enterUsernameWin_process(TOKEN)
                
        def enterUsernameWin_process(TOKEN):
            
            self.EnterTokenWindow.hide()
            self.EnterUsernameWindow.show()
            
            self.btnNextPg5.clicked.connect(lambda: checkUsername())
            def checkUsername():
                USERNAME = self.lineEditEnterUsername.text()
                self.lineEditEnterUsername.clear()
                if len(USERNAME) < 5:
                    _translate = QtCore.QCoreApplication.translate
                    self.lineEditEnterUsername.setPlaceholderText(_translate("MainWindow", "incorrect USERNAME"))
                else:
                    show_MainWindows()
                    WriteToFile(TOKEN,USERNAME)
                    
         
        def show_MainWindows():
            self.AuthorizedWindows.hide()
            self.MainWindows.show()
            self.menu.show()
            self.HomeWindow.show()
        
        
        welcomeWin_process()
    
        
        
                      
    def CheckBotStatus(self): 
        while True:
            flag = False
            for proc in psutil.process_iter():
                if proc.name() == "host.exe":
                    flag = True
                    break
            if flag:
                btnStatus = 'OFF'
                botStatus = 'ON'
            else:
                btnStatus = 'ON'
                botStatus = 'OFF'     
        
            self.msgStatusBot.setStyleSheet("border-radius: 16px;\n"
                f"background-image: url(:/msgBackgrounds/msgBotIs{botStatus}.png);")
            self.btnTurn.setStyleSheet("QPushButton\n"
                "{\n"
                "    border-radius: 10px;\n"
                f"    background-image: url(:/btnBackgrounds/btnTurn{btnStatus}.png);\n"
                "}\n"
                "QPushButton:hover\n"
                "{\n"
                "    border-radius: 15px;\n"
                "}")           
            time.sleep(5)
            
            
            
            
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        
 
class Data:
    def __init__(self,TOKEN,USERNAME):
        self.USER = USERNAME
        self.TOKEN = TOKEN
        self.dict = {}

def WriteToFile(TOKEN,USERNAME):
    PATH = os.path.abspath('../')  ###########################################!
    if not os.path.exists(PATH + '\\data'):
        subprocess.call(f'cd {PATH} && mkdir data', shell = True)
    PATH += '\\data\\data.bin'
    
    if os.path.exists(PATH):
        file = open(PATH, 'rb')
        data = pickle.load(file)
        file.close()
        
        if TOKEN != None:
            data.TOKEN = TOKEN
        elif USERNAME != None:
            data.USER = USERNAME
    else:        
        data = Data(TOKEN,USERNAME)
    
    file = open(PATH, 'wb')
    pickle.dump(data, file)
    file.close()

def connectToDB():
    connection = pymysql.connect(
        host = "sql11.freesqldatabase.com",
        port = 3306,
        user = "sql11509414",
        password = "alNPD6NZjz",
        database = "sql11509414",
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection

if __name__ == "__main__":
    import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Ui_MainWindow()
    MainWindow.setupUi(MainWindow)
    MainWindow.show()
    
    th = Thread(target = MainWindow.CheckBotStatus, args = (), daemon = True)
    th.start()
    
    sys.exit(app.exec_())