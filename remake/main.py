from os import path as os_path, system as os_system
from sys import argv as sys_argv, exit
from ctypes import windll
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSystemTrayIcon, QAction, QMenu, qApp, QMainWindow, QGraphicsDropShadowEffect
from psutil import process_iter
from threading import Thread
from subprocess import call
from pathlib import Path as pathlibPath
import psycopg2
from wmi import WMI
from pickle import load as pickle_load, dump as pickle_dump
from resource import resources

from Bot import utils


# TODO check @ in username
# PC CONTROL BOT SERTVER
# pccb_server


class UI(QMainWindow):
    def init(self):
        self.tray_icon = None
        self.botFlag = False
        self.MessageBox = windll.user32.MessageBoxW
        # self.processName = 'server.exe'
        self.processName = 'server.py'
        self.data = utils.Data()


    def initialUI(self, MainWindow):
        self.init()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/menuIcons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.HomeWindow.setGeometry(QtCore.QRect(0, 0, 1100, 805))
        self.HomeWindow.setTitle("")
        self.HomeWindow.setObjectName("HomeWindow")
        self.botIcon = QtWidgets.QFrame(self.HomeWindow)
        self.botIcon.setGeometry(QtCore.QRect(417, 128, 266, 266))
        self.botIcon.setStyleSheet("background-image: url(:/backgrounds/ImageBot.png);")
        self.botIcon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botIcon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botIcon.setObjectName("imageBot")

        effect = QGraphicsDropShadowEffect()
        effect.setOffset(5, 5)
        effect.setBlurRadius(50)
        self.botIcon.setGraphicsEffect(effect)

        self.btnTurn = QtWidgets.QPushButton(self.HomeWindow)
        self.btnTurn.setGeometry(QtCore.QRect(388, 576, 320, 64))
        self.btnTurn.setStyleSheet("QPushButton\n"
                                   "{\n"
                                   "    border: none;\n"
                                   "    border-radius: 10px;\n"
                                   "    background-image: url(:/btnBackgrounds/btnTurnON.png)\n"
                                   "}\n"
                                   "QPushButton:hover\n"
                                   "{\n"
                                   "    background-image: url(:/btnSelectedback/btnTurnONSelected.png)\n"
                                   "}\n"
                                   "QPushButton:pressed\n"
                                   "{\n"
                                   "    border-radius: 17px;\n"
                                   "}")
        self.btnTurn.setText("")
        self.btnTurn.setObjectName("btnTurn")
        self.msgStatusBot = QtWidgets.QFrame(self.HomeWindow)
        self.msgStatusBot.setGeometry(QtCore.QRect(388, 476, 320, 88))
        self.msgStatusBot.setStyleSheet("border-radius: 16px;\n"
                                        "background-image: url(:/msgBackgrounds/msgBotIsOFF.png);")
        self.msgStatusBot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgStatusBot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgStatusBot.setObjectName("msgStatusBot")
        self.ChangeDataWindow = QtWidgets.QGroupBox(self.MainWindows)
        self.ChangeDataWindow.setGeometry(QtCore.QRect(0, 0, 1100, 805))
        self.ChangeDataWindow.setTitle("")
        self.ChangeDataWindow.setObjectName("ChangeDataWindow")
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
                                              "color: #858D98;")
        self.lineChangeUsername.setText("")
        self.lineChangeUsername.setMaxLength(10)
        self.lineChangeUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.lineChangeUsername.setDragEnabled(False)
        self.lineChangeUsername.setReadOnly(False)
        self.lineChangeUsername.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineChangeUsername.setObjectName("lineEditUsername")
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
                                           "color: #858D98;")
        self.lineChangeToken.setText("")
        self.lineChangeToken.setMaxLength(70)
        self.lineChangeToken.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineChangeToken.setAlignment(QtCore.Qt.AlignCenter)
        self.lineChangeToken.setObjectName("lineEditToken")
        self.btnChangeUsername = QtWidgets.QPushButton(self.ChangeDataWindow)
        self.btnChangeUsername.setGeometry(QtCore.QRect(136, 438, 320, 64))
        self.btnChangeUsername.setStyleSheet("QPushButton\n"
                                             "{\n"
                                             "    border: none;\n"
                                             "    border-radius: 10px;\n"
                                             "    background-image: url(:/btnBackgrounds/btnChangeUsername.png);\n"
                                             "}\n"
                                             "QPushButton:hover\n"
                                             "{\n"
                                             "    background-image: url(:/btnSelectedback/btnChangeUsernameSelected.png);\n"
                                             "}\n"
                                             "QPushButton:pressed\n"
                                             "{\n"
                                             "    border-radius: 17px;\n"
                                             "}")
        self.btnChangeUsername.setText("")
        self.btnChangeUsername.setObjectName("btnChangeUsername")
        self.btnChangeToken = QtWidgets.QPushButton(self.ChangeDataWindow)
        self.btnChangeToken.setGeometry(QtCore.QRect(616, 438, 320, 64))
        self.btnChangeToken.setStyleSheet("QPushButton\n"
                                          "{\n"
                                          "    border: none;\n"
                                          "    border-radius: 10px;\n"
                                          "    background-image: url(:/btnBackgrounds/btnChangeToken.png);\n"
                                          "}\n"
                                          "QPushButton:hover\n"
                                          "{\n"
                                          "    background-image: url(:/btnSelectedback/btnChangeTokenSelected.png);\n"
                                          "}\n"
                                          "QPushButton:pressed\n"
                                          "{\n"
                                          "    border-radius: 17px;\n"
                                          "}")
        self.btnChangeToken.setText("")
        self.btnChangeToken.setObjectName("btnChangeToken")
        self.msgEnterNewToken = QtWidgets.QFrame(self.ChangeDataWindow)
        self.msgEnterNewToken.setGeometry(QtCore.QRect(616, 296, 220, 60))
        self.msgEnterNewToken.setStyleSheet("background-image: url(:/msgBackgrounds/msgEnterNewToken.png);\n"
                                            "")
        self.msgEnterNewToken.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgEnterNewToken.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgEnterNewToken.setObjectName("msgEnterNewToken")
        self.msgEnterNewUsername = QtWidgets.QFrame(self.ChangeDataWindow)
        self.msgEnterNewUsername.setGeometry(QtCore.QRect(136, 296, 261, 60))
        self.msgEnterNewUsername.setStyleSheet("background-image: url(:/msgBackgrounds/msgEnterNewUsername.png);\n"
                                               "")
        self.msgEnterNewUsername.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgEnterNewUsername.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgEnterNewUsername.setObjectName("msgEnterNewUsername")
        self.InfoWindow = QtWidgets.QGroupBox(self.MainWindows)
        self.InfoWindow.setGeometry(QtCore.QRect(0, 0, 1100, 805))
        self.InfoWindow.setTitle("")
        self.InfoWindow.setObjectName("InfoWindow")

        effect = QGraphicsDropShadowEffect()
        effect.setOffset(5, 5)
        effect.setBlurRadius(50)

        self.imageOleshko = QtWidgets.QFrame(self.InfoWindow)
        self.imageOleshko.setGeometry(QtCore.QRect(206, 260, 266, 265))
        self.imageOleshko.setStyleSheet("background-image: url(:/developers/imageOleshko.png);")
        self.imageOleshko.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageOleshko.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageOleshko.setObjectName("imageOleshko")
        self.imageOleshko.setGraphicsEffect(effect)

        effect = QGraphicsDropShadowEffect()
        effect.setOffset(5, 5)
        effect.setBlurRadius(50)

        self.imageBLVX = QtWidgets.QFrame(self.InfoWindow)
        self.imageBLVX.setGeometry(QtCore.QRect(630, 260, 266, 265))
        self.imageBLVX.setStyleSheet("background-image: url(:/developers/imageBLVX.png);")
        self.imageBLVX.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageBLVX.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageBLVX.setObjectName("imageBLVX")
        self.imageBLVX.setGraphicsEffect(effect)

        self.msgDevelopedBy = QtWidgets.QFrame(self.InfoWindow)
        self.msgDevelopedBy.setGeometry(QtCore.QRect(455, 137, 187, 60))
        self.msgDevelopedBy.setStyleSheet("background-image: url(:/developers/msgDevelopedBy.png);")
        self.msgDevelopedBy.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgDevelopedBy.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgDevelopedBy.setObjectName("msgDevelopedBy")
        self.msgOleshko = QtWidgets.QFrame(self.InfoWindow)
        self.msgOleshko.setGeometry(QtCore.QRect(256, 546, 166, 61))
        self.msgOleshko.setStyleSheet("background-image: url(:/developers/msgOleshko.png);")
        self.msgOleshko.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgOleshko.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgOleshko.setObjectName("msgOleshko")
        self.msgBLVX = QtWidgets.QFrame(self.InfoWindow)
        self.msgBLVX.setGeometry(QtCore.QRect(704, 546, 119, 61))
        self.msgBLVX.setStyleSheet("background-image: url(:/developers/msgBLVX.png);")
        self.msgBLVX.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgBLVX.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgBLVX.setObjectName("msgBLVX")
        self.InfoWindow.raise_()
        self.ChangeDataWindow.raise_()
        self.HomeWindow.raise_()
        self.menu = QtWidgets.QGroupBox(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(0, 0, 104, 805))
        self.menu.setStyleSheet("QGroupBox\n"
                                "{\n"
                                "    background-color: #E3F0E6;\n"
                                "    border: none;\n"
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
                                   "    background-image:url(:/menuIcons/iconHomeSelected.png)\n"
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
                                         "    background-image: url(:/menuIcons/iconSettings.png);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover\n"
                                         "{\n"
                                         "    \n"
                                         "    background-image:url(:/menuIcons/iconSettingsSelected.png);\n"
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

        self.MainWindows.raise_()
        self.menu.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateMainWindows(MainWindow)


    def setupUI(self):
        self.arrayMainWindows = [self.HomeWindow, self.ChangeDataWindow, self.InfoWindow]
        self.iconNames = ['Home', 'Settings', 'Info']
        self.arrayBtn = [self.btnHome, self.btnChangeData, self.btnInfo]
        self._translate = QtCore.QCoreApplication.translate


    def runUI(self):

        if self.isFirstTime():
            self.createLoginWindows()
            self.MainWindows.hide()
            self.welcomeWin()


        self.setupUI()


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
        
        self.btnTurn.clicked.connect(lambda: self.changeTurn())
        
        self.btnHome.clicked.connect(lambda: self.changeWindow(self.HomeWindow)) 
        self.btnChangeData.clicked.connect(lambda: self.changeWindow(self.ChangeDataWindow))
        self.btnInfo.clicked.connect(lambda: self.changeWindow(self.InfoWindow))
        
        self.btnChangeToken.clicked.connect(lambda: self.changeToken())
        self.btnChangeUsername.clicked.connect(lambda: self.changeUsername())


    def isFirstTime(self):
        PATH = os_path.expanduser('~') + '\\AppData\\Local\\PC_Control_Bot\\data.bin'
        return False if os_path.exists(PATH) else True


    def createLoginWindows(self):
        self.AuthorizedWindows = QtWidgets.QGroupBox(self.centralwidget)
        self.AuthorizedWindows.setGeometry(QtCore.QRect(-2, -2, 1205, 805))
        self.AuthorizedWindows.setStyleSheet("QGroupBox\n"
                                             "{\n"
                                             "    \n"
                                             "    background-image: url(:/backgrounds/background.png);\n"
                                             "}\n"
                                             "")
        self.AuthorizedWindows.setTitle("")
        self.AuthorizedWindows.setObjectName("AuthorizedWindows")
        effect = QGraphicsDropShadowEffect()
        effect.setOffset(5, 5)
        effect.setBlurRadius(50)
        self.botIcon = QtWidgets.QFrame(self.AuthorizedWindows)
        self.botIcon.setGeometry(QtCore.QRect(467, 90, 267, 267))
        self.botIcon.setStyleSheet("background-image: url(:/backgrounds/ImageBot.png);")
        self.botIcon.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botIcon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botIcon.setObjectName("botIcon")
        self.botIcon.setGraphicsEffect(effect)

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
        self.btnNextPg1 = QtWidgets.QPushButton(self.WelcomeWindow)
        self.btnNextPg1.setGeometry(QtCore.QRect(395, 600, 411, 64))
        self.btnNextPg1.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "    border: none;\n"
                                      "    border-radius: 10px;\n"
                                      "    background-image: url(:/btnBackgrounds/btnNextPg1.png);\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "    background-image: url(:/btnSelectedback/btnNextPg1Selected.png);\n"
                                      "}\n"
                                      "QPushButton:pressed\n"
                                      "{\n"
                                      "    border-radius: 17px;\n"
                                      "}")
        self.btnNextPg1.setText("")
        self.btnNextPg1.setObjectName("btnNextPg1")
        self.TermWindow = QtWidgets.QGroupBox(self.AuthorizedWindows)
        self.TermWindow.setGeometry(QtCore.QRect(0, 0, 1205, 805))
        self.TermWindow.setTitle("")
        self.TermWindow.setObjectName("TermWindow")
        self.msgTerms = QtWidgets.QFrame(self.TermWindow)
        self.msgTerms.setGeometry(QtCore.QRect(304, 435, 592, 199))
        self.msgTerms.setStyleSheet("border-radius: 16px;\n"
                                    "background-image: url(:/msgBackgrounds/msgTerms.png);")
        self.msgTerms.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgTerms.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgTerms.setObjectName("msgTerms")
        self.btnNextPg2 = QtWidgets.QPushButton(self.TermWindow)
        self.btnNextPg2.setGeometry(QtCore.QRect(304, 646, 592, 64))
        self.btnNextPg2.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "    border: none;\n"
                                      "    border-radius: 10px;\n"
                                      "    background-image: url(:/btnBackgrounds/btnNextPg2.png);\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "    background-image: url(:/btnSelectedback/btnNextPg2Selected.png);\n"
                                      "}\n"
                                      "QPushButton:pressed\n"
                                      "{\n"
                                      "    border-radius: 17px;\n"
                                      "}")
        self.btnNextPg2.setText("")
        self.btnNextPg2.setObjectName("btnNextPg2")
        self.EnterUsernameWindow = QtWidgets.QGroupBox(self.AuthorizedWindows)
        self.EnterUsernameWindow.setGeometry(QtCore.QRect(0, 0, 1205, 805))
        self.EnterUsernameWindow.setStyleSheet("QLabel{\n"
                                               "    background-color: #FF0000;\n"
                                               "}")
        self.EnterUsernameWindow.setTitle("")
        self.EnterUsernameWindow.setObjectName("EnterUsernameWindow")
        self.msgEnterUsername = QtWidgets.QFrame(self.EnterUsernameWindow)
        self.msgEnterUsername.setGeometry(QtCore.QRect(282, 415, 636, 91))
        self.msgEnterUsername.setStyleSheet("border-radius: 16px;\n"
                                            "background-image: url(:/msgBackgrounds/msgEnterUsername.png);")
        self.msgEnterUsername.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgEnterUsername.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgEnterUsername.setObjectName("msgEnterUsername")
        self.btnNextPg5 = QtWidgets.QPushButton(self.EnterUsernameWindow)
        self.btnNextPg5.setGeometry(QtCore.QRect(606, 518, 312, 64))
        self.btnNextPg5.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "    border: none;\n"
                                      "    border-radius: 10px;\n"
                                      "    background-image: url(:/btnBackgrounds/btnNextPg5.png);\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "    background-image: url(:/btnSelectedback/btnNextPg5Selected.png);\n"
                                      "}\n"
                                      "QPushButton:pressed\n"
                                      "{\n"
                                      "    border-radius: 17px;\n"
                                      "}")
        self.btnNextPg5.setText("")
        self.btnNextPg5.setObjectName("btnNextPg5")
        self.lineEditEnterUsername = QtWidgets.QLineEdit(self.EnterUsernameWindow)
        self.lineEditEnterUsername.setGeometry(QtCore.QRect(282, 518, 312, 63))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditEnterUsername.setFont(font)
        self.lineEditEnterUsername.setAutoFillBackground(False)
        self.lineEditEnterUsername.setStyleSheet("border: none;\n"
                                                 "border-radius: 15px;\n"
                                                 "background-color: rgb(231, 253, 204);\n"
                                                 "color: #858D98;")
        self.lineEditEnterUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditEnterUsername.setObjectName("lineEditEnterUsername")
        self.EnterKeyWindow = QtWidgets.QGroupBox(self.AuthorizedWindows)
        self.EnterKeyWindow.setGeometry(QtCore.QRect(0, 0, 1205, 805))
        self.EnterKeyWindow.setTitle("")
        self.EnterKeyWindow.setObjectName("EnterKeyWindow")
        self.msgGetKey = QtWidgets.QFrame(self.EnterKeyWindow)
        self.msgGetKey.setGeometry(QtCore.QRect(355, 405, 490, 172))
        self.msgGetKey.setStyleSheet("border-radius: 15px;\n"
                                     "background-image: url(:/msgBackgrounds/msgGetKey.png);")
        self.msgGetKey.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.msgGetKey.setFrameShadow(QtWidgets.QFrame.Raised)
        self.msgGetKey.setObjectName("msgGetKey")
        self.btnNextPg3 = QtWidgets.QPushButton(self.EnterKeyWindow)
        self.btnNextPg3.setGeometry(QtCore.QRect(355, 665, 490, 64))
        self.btnNextPg3.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "    border: none;\n"
                                      "    border-radius: 10px;\n"
                                      "    background-image: url(:/btnBackgrounds/btnNextPg3.png);\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "    background-image: url(:/btnSelectedback/btnNextPg3Selected.png);\n"
                                      "}\n"
                                      "QPushButton:pressed\n"
                                      "{\n"
                                      "    border-radius: 17px;\n"
                                      "}")
        self.btnNextPg3.setText("")
        self.btnNextPg3.setObjectName("btnNextPg3")
        self.lineEditEnterKey = QtWidgets.QLineEdit(self.EnterKeyWindow)
        self.lineEditEnterKey.setGeometry(QtCore.QRect(355, 589, 490, 64))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditEnterKey.setFont(font)
        self.lineEditEnterKey.setAutoFillBackground(False)
        self.lineEditEnterKey.setStyleSheet("border: none;\n"
                                            "border-radius: 16px;\n"
                                            "background-color: rgb(231, 253, 204);\n"
                                            "color: #858D98;")
        self.lineEditEnterKey.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditEnterKey.setObjectName("lineEditEnterKey")
        self.EnterTokenWindow = QtWidgets.QGroupBox(self.AuthorizedWindows)
        self.EnterTokenWindow.setGeometry(QtCore.QRect(0, 0, 1205, 805))
        self.EnterTokenWindow.setTitle("")
        self.EnterTokenWindow.setObjectName("EnterTokenWindow")
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
        self.btnNextPg4.setStyleSheet("QPushButton\n"
                                      "{\n"
                                      "    border: none;\n"
                                      "    border-radius: 10px;\n"
                                      "    background-image: url(:/btnBackgrounds/btnNextPg4.png);\n"
                                      "}\n"
                                      "QPushButton:hover\n"
                                      "{\n"
                                      "    background-image: url(:/btnSelectedback/btnNextPg4Selected.png);\n"
                                      "}\n"
                                      "QPushButton:pressed\n"
                                      "{\n"
                                      "    border-radius: 17px;\n"
                                      "}")
        self.btnNextPg4.setText("")
        self.btnNextPg4.setObjectName("btnNextPg4")
        self.lineEditEnterToken = QtWidgets.QLineEdit(self.EnterTokenWindow)
        self.lineEditEnterToken.setGeometry(QtCore.QRect(155, 626, 630, 64))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditEnterToken.setFont(font)
        self.lineEditEnterToken.setAutoFillBackground(False)
        self.lineEditEnterToken.setStyleSheet("border: none;\n"
                                              "border-radius: 16px;\n"
                                              "background-color: rgb(231, 253, 204);\n"
                                              "color: #858D98;")
        self.lineEditEnterToken.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditEnterToken.setObjectName("lineEditEnterToken")
        self.EnterUsernameWindow.raise_()
        self.EnterTokenWindow.raise_()
        self.EnterKeyWindow.raise_()
        self.TermWindow.raise_()
        self.WelcomeWindow.raise_()
        self.botIcon.raise_()
        self.retranslateAuthorizedWindows(self.AuthorizedWindows)


    def welcomeWin(self):
        self.AuthorizedWindows.show()
        self.WelcomeWindow.show()
        self.btnNextPg1.clicked.connect(lambda: self.termWin())


    def termWin(self):
        self.WelcomeWindow.hide()
        self.TermWindow.show()
        self.btnNextPg2.clicked.connect(lambda: self.enterTokenWin())


    def enterTokenWin(self):
        self.EnterKeyWindow.hide()
        self.TermWindow.hide()
        self.EnterTokenWindow.show()
        self.btnNextPg4.clicked.connect(lambda: checkToken())

        def checkToken():
            TOKEN = self.lineEditEnterToken.text()
            self.lineEditEnterToken.clear()

            if len(TOKEN) != 46:
                _translate = QtCore.QCoreApplication.translate
                self.lineEditEnterToken.setPlaceholderText(_translate("MainWindow", "Incorrect TOKEN"))
                return

            self.data.TOKEN = TOKEN
            utils.writeToFile(self.data)
            self.enterUsernameWin()


    def enterUsernameWin(self):
        self.EnterTokenWindow.hide()
        self.EnterUsernameWindow.show()
        self.btnNextPg5.clicked.connect(lambda: checkUsername())

        def checkUsername():
            USERNAME = self.lineEditEnterUsername.text()
            self.lineEditEnterUsername.clear()

            if len(USERNAME) < 5:
                _translate = QtCore.QCoreApplication.translate
                self.lineEditEnterUsername.setPlaceholderText(_translate("MainWindow", "Incorrect USERNAME"))
                return

            self.AuthorizedWindows.hide()
            self.MainWindows.show()
            self.menu.show()

            self.data.USERNAME = USERNAME
            utils.writeToFile(self.data)
            self.EnterUsernameWindow.hide()
            self.AuthorizedWindows.hide()


    def runServer(self):
        # os_system(command)
        # call(f'cd output && cd server && {self.processName}', shell=True)
        call(f'python {self.processName}', shell=True)


    def checkProcess(self):
        for proc in process_iter():
            if proc.name() == self.processName:
                return True
        return False


    def changeTurn(self):
        flag = self.checkProcess()

        if not flag:
            self.msgStatusBot.setStyleSheet("border-radius: 16px;\n"
                                            f"background-image: url(:/msgBackgrounds/msgBotStarting.png);")
            th = Thread(target=self.runServer, args=(), daemon=True)
            th.start()
            return

        self.msgStatusBot.setStyleSheet("border-radius: 16px;\n"
                                        f"background-image: url(:/msgBackgrounds/msgBotStopping.png);")
        call(f'taskkill /f /im {self.processName}', shell=True)


    def changeToken(self):
        TOKEN = self.lineChangeToken.text()
        self.lineChangeToken.setText('')

        if len(TOKEN) != 46:
            self.lineChangeToken.setPlaceholderText(self._translate("MainWindow", "Incorrect TOKEN"))
            return

        self.data.TOKEN = TOKEN
        writeToFile(TOKEN, None)
        self.lineChangeToken.setPlaceholderText(self._translate("MainWindow", "success"))


    def changeUsername(self):
        USERNAME = self.lineChangeUsername.text()
        self.lineChangeUsername.setText('')

        if len(USERNAME) < 5:
            self.lineChangeUsername.setPlaceholderText(self._translate("MainWindow", "Incorrect USERNAME"))
            return

        self.data.username = USERNAME
        writeToFile(self.data)
        self.lineChangeUsername.setPlaceholderText(self._translate("MainWindow", "success"))


    def changeWindow(self, window):
        def setStyles(name):
            i = 0
            for el in self.iconNames:
                if el != name:
                    style = getStyle(self, el, False)
                else:
                    style = getStyle(self, el, True)
                self.arrayBtn[i].setStyleSheet(style)
                i += 1

        def getStyle(self, defaultName, flag):
            selectedName = defaultName + 'Selected'
            if flag:
                defaultName += 'Blue'
            return ("QPushButton\n{\nbackground-image: url(:/menuIcons/"
                    f"icon{defaultName}.png);\n"
                    "}\nQPushButton:hover{\nbackground-image:url(:/menuIcons/"
                    f"icon{selectedName}.png);\n"
                    "}")

        for el in self.arrayMainWindows:
            if el != window:
                el.hide()
        window.show()

        if window == self.HomeWindow:
            name = 'Home'
        elif window == self.ChangeDataWindow:
            name = 'Settings'
        else:
            name = 'Info'

        setStyles(name)


    def retranslateMainWindows(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PC Control Bot"))
        self.lineChangeUsername.setPlaceholderText(_translate("MainWindow", "Your Username"))
        self.lineChangeToken.setPlaceholderText(_translate("MainWindow", "Your TOKEN"))
        self.lineChangeUsername.setMaxLength(100)


    def retranslateAuthorizedWindows(self, AuthorizedWindows):
        _translate = QtCore.QCoreApplication.translate
        self.lineEditEnterUsername.setPlaceholderText(_translate("MainWindow", "Your USERNAME"))
        self.lineEditEnterKey.setPlaceholderText(_translate("MainWindow", "Your KEY"))
        self.lineEditEnterToken.setPlaceholderText(_translate("MainWindow", "Your TOKEN"))


    def checkBotStatus(self):
        prev = False

        while True:
            self.botFlag = self.checkProcess()

            if prev != self.botFlag:
                if self.botFlag:
                    btnStatus = 'OFF'
                    botStatus = 'ON'
                    prev = True
                    self.botFlag = True
                else:
                    btnStatus = 'ON'
                    botStatus = 'OFF'
                    prev = False
                    self.botFlag = False

                self.msgStatusBot.setStyleSheet("border-radius: 16px;\n"
                                                f"background-image: url(:/msgBackgrounds/msgBotIs{botStatus}.png);")
                self.btnTurn.setStyleSheet("QPushButton\n"
                                           "{\n"
                                           "    border: none;\n"
                                           "    border-radius: 10px;\n"
                                           f"    background-image: url(:/btnBackgrounds/btnTurn{btnStatus}.png)\n"
                                           "}\n"
                                           "QPushButton:hover\n"
                                           "{\n"
                                           f"    background-image: url(:/btnSelectedback/btnTurn{btnStatus}Selected.png)\n"
                                           "}\n"
                                           "QPushButton:pressed\n"
                                           "{\n"
                                           "    border-radius: 17px;\n"
                                           "}")
            sleep(5)


    # hide window to tray
    def closeEvent(self, event):
        event.ignore()
        self.hide()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys_argv)
    MainWindow = UI()
    MainWindow.initialUI(MainWindow)
    MainWindow.show()
    MainWindow.runUI()

    th = Thread(target=MainWindow.checkBotStatus, args=(), daemon=True)
    th.start()

    exit(app.exec_())
