# system
import os
import time
import ctypes
import platform
# bot
import telebot
from telebot import types
# screenshot
import pyscreenshot as ImageGrab
# volume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
# brightness
import screen_brightness_control as sbc
# mouse
import mouse
# batttery status
import psutil
# ip
import socket


# bot
#! my_id = 
#! TOKEN = ''
bot = telebot.TeleBot(TOKEN)


# volume
volDevices = AudioUtilities.GetSpeakers()
volInterface = volDevices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
vol = cast(volInterface, POINTER(IAudioEndpointVolume))


# sleep
flag = False


@bot.message_handler(commands = ['start'])
def Start(message):
    bot.send_message(message.chat.id, 'Бот запущений')
    


@bot.message_handler(commands = ['help'])
def Help(message):
    bot.send_message(message.chat.id, '''
*ℹ️  Information about bot:*\n
*🚀  /start* - Start bot\n
*ℹ️  /help* - Commands list\n
*🔊  /volume* - Set volume to [value]\n
*☀️  /brightness* - Set brightness to [value]\n
*🔒  /lock* - Lock your PC\n
*🖱  /mouse* - Set mouse position\n
*⚠️  /shutdown* - Shutdown your PC\n
*🔄  /reboot* - Restart your PC\n
*💤  /sleep* - Hibernate your PC\n
*🔋  /battery* - Show battery status\n
*🛰️  /ip* - Show your IP\n
*🪪  /get_id * - Get your telegram ID\n
*⚙️  /info* - Show PC info\n
*🖥️  /status* - Show PC status\n
    ''', parse_mode = 'Markdown')


#! * 🏞  /screenshot* - Take screenshot\n
#! *📸  /webcam* - Take webcam photo\n


@bot.message_handler(commands = ['volume', 'vol'])
def Volume(message):
    # if message.id != my_id:
    #     return Warn(message)
    currentVolume = getCurrentVolume()
    emoji = getVolumeEmoji(currentVolume)
    bot.send_message(message.chat.id, f'{emoji} Current volume is *{currentVolume}%*', parse_mode = 'Markdown')
    bot.send_message(message.chat.id, 'Enter new volume:')
    bot.register_next_step_handler(message, Volume_process)



def Volume_process(message):
    # if message.id != my_id:
    #     return Warn(message)
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



@bot.message_handler(commands = ['brightness', 'bright'])
def Brightness(message):
    # if message.id != my_id:
    #     return Warn(message)
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



@bot.message_handler(commands = ['lock'])
def Lock(message):
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode = 'Markdown')
    ctypes.windll.user32.LockWorkStation()
    bot.send_message(message.chat.id, '*Locked 🔒*', parse_mode = 'Markdown')



# TODO mouse
# @bot.message_handler(commands = ['mouse'])
# def changeMouse(message):



@bot.message_handler(commands = ['shutdown', 'sd'])
def Shutdown(message):
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



@bot.message_handler(commands = ['reboot', 'rb'])
def Reeboot(message):
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



@bot.message_handler(commands = ['sleep'])
def Sleep(message):
    global flag
    flag = False
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode = 'Markdown')
    bot.send_message(
        message.chat.id, 'How many *seconds* to sleep?', parse_mode = 'Markdown')
    bot.register_next_step_handler(message, Sleep_process)
def Sleep_process(message):
    global flag
    if not message.text.isdigit():
        return bot.send_message(message.chat.id, 'Time must be a number')
    seconds = int(message.text)
    markupInlineCancelSleep = types.InlineKeyboardMarkup()
    btnCancelSleep = types.InlineKeyboardButton(text = 'Cancel', callback_data = 'cancelSleep')
    markupInlineCancelSleep.add(btnCancelSleep)
    bot.send_message(message.chat.id, f'💤  Sleeping in *{seconds}s*', parse_mode = 'Markdown', reply_markup = markupInlineCancelSleep)
    for i in range(seconds):
        time.sleep(1)
        if flag:
            flag = False
            return
    os.system('shutdown /h')
    
    
    
# ! callback handler
@bot.callback_query_handler(func=lambda call: True)
def ShutdownCancel(call):
    if call.data == 'cancelShutdown':
        os.system('shutdown /a')
        bot.send_message(call.message.chat.id, '🛑  Shutdown *canceled*', parse_mode = 'Markdown')
    elif call.data == 'cancelReboot':
        os.system('shutdown /a')
        bot.send_message(call.message.chat.id, '🛑  Reboot *canceled*', parse_mode = 'Markdown')
    elif call.data == 'cancelSleep':
        global flag
        flag = True
        bot.send_message(call.message.chat.id, '🛑  Sleep *canceled*', parse_mode = 'Markdown')



@bot.message_handler(commands = ['battery'])
def Battery(message):
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



@bot.message_handler(commands = ['ip'])
def IP(message):
    ip = getIP()
    bot.send_message(message.chat.id, f'🛰️ Your *IP* is *{ip}*', parse_mode = 'Markdown')
def getIP():
    return socket.gethostbyname(socket.gethostname())



@bot.message_handler(commands = ['info', 'pc', 'pc_info'])
def PcInfo(message):
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



@bot.message_handler(commands = ['status', 'pc_status'])
def PcStatus(message):
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



# ! warning
def Warn(message):
    bot.send_chat_action(message.chat.id, 'typing')
    msg = f"Someone just used  *{message.text}*\n\n"
    msg += f"Username:  *@{message.from_user.username}*\n"
    msg += f"First Name:  *{message.from_user.first_name}*\n"
    if message.from_user.last_name != None:
        msg += f"Last Name:  *{message.from_user.last_name}*\n"
    msg += f"User Id:  *{message.from_user.id}*\n"
    bot.send_message(my_id, f'{msg}', parse_mode = 'Markdown')


@bot.message_handler(commands = ['get_id', 'id'])
def GetId(message):
    bot.send_message(message.from_user.id, f'🪪 Your *ID* is *{message.from_user.id}*', parse_mode = 'Markdown')

if __name__ == '__main__': # чтобы код выполнялся только при запуске в виде сценария, а не при импорте модуля
    try:
       bot.polling(none_stop = True) # запуск бота
    except Exception as e:
       print(e) # или import traceback; traceback.print_exc() для печати полной инфы
       time.sleep(15)



# TODO:
#* check battery
#* full info about pc
#* ip info
#? pc status
#  screen shot
# open browser
# open link
# open in youtube
# youtube fullscreen
# youtube pause
# youtube next video
# timer
#? webcam photo
# keylogger
# spotify control