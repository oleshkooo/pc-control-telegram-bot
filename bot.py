# system
import os
import re
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
# webcam
import cv2
# batttery status
import psutil
# check ip 
import socket


# bot
#! my_id =  YOUR ID HERE !!!
#! TOKEN =  YOUR TOKEN HERE !!!

bot = telebot.TeleBot(TOKEN)

# volume
volDevices = AudioUtilities.GetSpeakers()
volInterface = volDevices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
vol = cast(volInterface, POINTER(IAudioEndpointVolume))

# sleep
flag = False


@bot.message_handler(commands=['start'])
def Start(message):
    bot.send_message(message.chat.id, 'Бот запущений')


@bot.message_handler(commands=['help'])
def Help(message):
    bot.send_message(message.chat.id, '''
*ℹ️  Information about bot:*\n
*🚀  /start* - Start bot\n
*ℹ️  /help* - Commands list\n
*🏞  /screenshot* - Take screenshot\n
*📸  /webcam* - Take webcam photo\n
*🔊  /volume* - Set volume to [value]\n
*☀️  /brightness* - Set brightness to [value]\n
*🔒  /lock* - Lock your PC\n
*🖱  /mouse* - Set mouse position\n
*⚠️  /shutdown* - Shutdown your PC\n
*🔄  /reboot* - Restart your PC\n
*💤  /sleep* - Hibernate your PC\n
*🔋  /battery* - Show battery status\n
*🛰️  /ip* - Show your IP\n
*🖥  /pc* - Show PC info\n

    ''', parse_mode='Markdown')


@bot.message_handler(commands=['screenshot', 'screen'])
def Screenshot(message):
    # if message.id != my_id:
    #     return InfoUser(message)
    bot.send_message(message.chat.id, '*Done ✅*', parse_mode='Markdown')
    bot.send_chat_action(message.chat.id, 'upload_photo')
    img = ImageGrab.grab()
    img.save('Screenshot.png')
    # bot.send_photo(message.chat.id, open('Screenshot.png', 'rb'))
    bot.send_document(message.chat.id, open('Screenshot.png', 'rb'))
    os.remove('Screenshot.png')


@bot.message_handler(commands=['webcam', 'cam'])
def Webcam(message):
    webcam = cv2.VideoCapture(0)
    result, image = webcam.read()
    if not result:
        return bot.send_message(message.chat.id, 'No image detected. Please try again')
    cv2.imwrite("Webcam.png", image)
    # bot.send_photo(message.chat.id, open('Webcam.png', 'rb'))
    bot.send_document(message.chat.id, open('Webcam.png', 'rb'))
    os.remove('Webcam.png')


@bot.message_handler(commands=['volume', 'vol'])
def Volume(message):
    # if message.id != my_id:
    #     return InfoUser(message)
    currentVolume = getCurrentVolume()
    emoji = getVolumeEmoji(currentVolume)
    bot.send_message(
        message.chat.id, f'{emoji} Current volume is *{currentVolume}%*', parse_mode='Markdown')
    bot.send_message(message.chat.id, 'Enter new volume:')
    bot.register_next_step_handler(message, Volume_process)


def Volume_process(message):
    volume = message.text
    if not volume.isdigit():
        return bot.send_message(message.chat.id, 'Volume must be a number')
    volumeInt = int(volume)
    if volumeInt < 0 or volumeInt > 100:
        return bot.send_message(message.chat.id, 'Volume must be *> 0* and *< 100*', parse_mode='Markdown')
    emoji = getVolumeEmoji(volumeInt)
    scalarVolume = volumeInt / 100
    vol.SetMasterVolumeLevelScalar(scalarVolume, None)
    bot.send_message(
        message.chat.id, f'{emoji} Volume set to *{message.text}%*', parse_mode='Markdown')


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


@bot.message_handler(commands=['brightness', 'bright'])
def Brightness(message):
    # if message.id != my_id:
    #     return InfoUser(message)
    currentBrightness = getCurrentBrightness()
    emoji = getBrightnessEmoji(currentBrightness)
    bot.send_message(
        message.chat.id, f'{emoji} Current brightness is *{currentBrightness}%*', parse_mode='Markdown')
    bot.send_message(message.chat.id, 'Enter new brightness:')
    bot.register_next_step_handler(message, Brightness_process)


def Brightness_process(message):
    brightness = message.text
    if not brightness.isdigit():
        return bot.send_message(message.chat.id, 'Brightness must be a number')
    brightnessInt = int(brightness)
    if brightnessInt < 0 or brightnessInt > 100:
        return bot.send_message(message.chat.id, 'Brightness must be *> 0* and *< 100*', parse_mode='Markdown')
    emoji = getBrightnessEmoji(brightnessInt)
    sbc.set_brightness(brightnessInt)
    bot.send_message(
        message.chat.id, f'{emoji} Brightness set to *{message.text}%*', parse_mode='Markdown')


def getCurrentBrightness():
    return sbc.get_brightness()[0]


def getBrightnessEmoji(brightness):
    if brightness < 33:
        return '🔅'
    elif brightness < 66:
        return '🔆'
    else:
        return '☀️'


@bot.message_handler(commands=['lock'])
def Lock(message):
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode='Markdown')
    ctypes.windll.user32.LockWorkStation()
    bot.send_message(message.chat.id, '*Locked 🔒*', parse_mode='Markdown')


@bot.message_handler(commands=['info'])
def Info(message):
    bot.send_chat_action(message.chat.id, 'typing')
    text = f"Someone just used  *{message.text}*\n\n"
    text += f"Username:  *@{message.from_user.username}*\n"
    text += f"First Name:  *{message.from_user.first_name}*\n"
    if message.from_user.last_name != None:
        text += f"Last Name:  *{message.from_user.last_name}*\n"
    text += f"User Id:  *{message.from_user.id}*\n"
    bot.send_message(my_id, f'{text}', parse_mode='Markdown')


# TODO mouse
# @bot.message_handler(commands = ['mouse'])
# def changeMouse(message):


@bot.message_handler(commands=['shutdown', 'sd'])
def Shutdown(message):
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode='Markdown')
    bot.send_message(
        message.chat.id, 'How many *seconds* to turn off the PC?', parse_mode='Markdown')
    bot.register_next_step_handler(message, Shutdown_process)


def Shutdown_process(message):
    if not message.text.isdigit():
        return bot.send_message(message.chat.id, 'Time must be a number')
    seconds = int(message.text)
    markupInlineCancelShutdown = types.InlineKeyboardMarkup()
    btnCancelShutdown = types.InlineKeyboardButton(
        text='Cancel', callback_data='cancelShutdown')
    markupInlineCancelShutdown.add(btnCancelShutdown)
    bot.send_message(message.chat.id, f'⚠️  Shutting down in *{seconds}s*',
                     parse_mode='Markdown', reply_markup=markupInlineCancelShutdown)
    os.system(f'shutdown -s -t {seconds}')


@bot.message_handler(commands=['reboot', 'rb'])
def Reeboot(message):
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode='Markdown')
    bot.send_message(
        message.chat.id, 'How many *seconds* to restart the PC?', parse_mode='Markdown')
    bot.register_next_step_handler(message, Reboot_process)


def Reboot_process(message):
    if not message.text.isdigit():
        return bot.send_message(message.chat.id, 'Time must be a number')
    seconds = int(message.text)
    markupInlineCancelReboot = types.InlineKeyboardMarkup()
    btnCancelReboot = types.InlineKeyboardButton(
        text='Cancel', callback_data='cancelReboot')
    markupInlineCancelReboot.add(btnCancelReboot)
    bot.send_message(message.chat.id, f'🔄  Reboot in *{seconds}s*',
                     parse_mode='Markdown', reply_markup=markupInlineCancelReboot)
    os.system(f'shutdown -r -t {seconds}')


@bot.message_handler(commands=['sleep'])
def Sleep(message):
    global flag
    flag = False
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode='Markdown')
    bot.send_message(
        message.chat.id, 'How many *seconds* to sleep?', parse_mode='Markdown')
    bot.register_next_step_handler(message, Sleep_process)


def Sleep_process(message):
    global flag
    if not message.text.isdigit():
        return bot.send_message(message.chat.id, 'Time must be a number')
    seconds = int(message.text)
    markupInlineCancelSleep = types.InlineKeyboardMarkup()
    btnCancelSleep = types.InlineKeyboardButton(
        text='Cancel', callback_data='cancelSleep')
    markupInlineCancelSleep.add(btnCancelSleep)
    bot.send_message(message.chat.id, f'💤  Sleeping in *{seconds}s*',
                     parse_mode='Markdown', reply_markup=markupInlineCancelSleep)
    for i in range(seconds):
        time.sleep(1)
        if flag == True:
            flag = False
            return
    os.system('shutdown /h')


# ! callback handler
@bot.callback_query_handler(func=lambda call: True)
def ShutdownCancel(call):
    if call.data == 'cancelShutdown':
        os.system('shutdown /a')
        bot.send_message(call.message.chat.id,
                         '🛑  Shutdown *canceled*', parse_mode='Markdown')
    elif call.data == 'cancelReboot':
        os.system('shutdown /a')
        bot.send_message(call.message.chat.id,
                         '🛑  Reboot *canceled*', parse_mode='Markdown')
    elif call.data == 'cancelSleep':
        global flag
        flag = True
        bot.send_message(call.message.chat.id,
                         '🛑  Sleep *canceled*', parse_mode='Markdown')


#! ADD
#*7/14/2022 BLVX
@bot.message_handler(commands=['battery', 'bc'])
def SendCharge(message):
    percent = GetCharge()
    bot.send_message(message.chat.id,f'{GetBatteryEmoji(percent)} Battery level is *{percent}*%', parse_mode = 'Markdown')
def GetCharge():
    return psutil.sensors_battery().percent
def GetBatteryEmoji(percent):
    if percent <= 33: return '🪫'
    return '🔋'
    
@bot.message_handler(commands = ['ip'])
def SendIP(message):
    bot.send_message(message.chat.id, f'🛰️ Your *IP* is *{GetIP()}*', parse_mode = 'Markdown')
def GetIP():
    return socket.gethostbyname(socket.gethostname())

@bot.message_handler(commands=['pc', 'pc_info'])
def PcInfo(message): 
    curBattery = GetCharge()
    curBrightness = getCurrentBrightness()
    curVolume = getCurrentVolume()
    
    msg = '🖥️ *Info about your PC*\n'
    msg += f' *Name:* {platform.node()}\n'
    msg += f' *OS:* {platform.system()} {platform.release()}\n'   
    msg += f' *IP*: {GetIP()} 🛰️\n'
    msg += f' *Battery level*: {curBattery}% {GetBatteryEmoji(curBattery)}\n'
    msg += f' *Brightness:* {curBrightness}% {getBrightnessEmoji(curBrightness)}\n'
    msg += f' *Volume:* {curVolume}% {getVolumeEmoji(curVolume)}\n'
    bot.send_message(message.chat.id, msg, parse_mode = "markdown")

#                                                                                                                                                             *

bot.polling(none_stop=True)


# TODO:
#* check battery
#* full info about pc
#* ip info
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
