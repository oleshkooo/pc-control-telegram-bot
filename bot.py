# system
import os
import time
import ctypes
import platform
# telegram bot
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



# telegram bot
my_id = 673723655
TOKEN = '5428408141:AAFpzz6uw7VmMyVyqsKiOm5VhZehDFFRGOk'
bot = telebot.TeleBot(TOKEN)



# volume
volDevices = AudioUtilities.GetSpeakers()
volInterface = volDevices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
vol = cast(volInterface, POINTER(IAudioEndpointVolume))



@bot.message_handler(commands = ['start'])
def Start(message):
    bot.send_message(message.chat.id,'Бот запущений')



@bot.message_handler(commands=['help'])
def Help(message):
    bot.send_message(message.chat.id, '''
*ℹ️ Information about bot:*\n
*🚀  /start* - start bot\n
*ℹ️  /help* - help\n
*🏞  /screenshot* - take screenshot\n
*🔊  /volume* - set volume\n
*☀️  /brightness* - set brightness\n
*🔒  /lock* - lock your PC\n
*🖱  /mouse* - set mouse position\n
*💤  /shutdown* - shutdown your PC
*🛑  /shutdown_cancel* - cancel shutdown\n
*🔄  /reboot* - restart your PC
*🛑  /reboot_cancel* - cancel restart PC\n
    ''', parse_mode = 'Markdown')



@bot.message_handler(commands = ['screenshot'])
def Screenshot(message):
    # if message.id != my_id:
    #     return InfoUser(message)
    bot.send_message(message.chat.id, '*Done ✅*', parse_mode = 'Markdown')
    bot.send_chat_action(message.chat.id, 'upload_photo')
    img = ImageGrab.grab()
    img.save('screenshot.png')
    bot.send_photo(message.chat.id, open('screenshot.png', 'rb'))
    os.remove('screenshot.png')



@bot.message_handler(commands = ['volume'])
def Volume(message):
    # if message.id != my_id:
    #     return InfoUser(message)
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
        return bot.send_message(message.chat.id, 'Volume must be > 0 and < 100')
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



@bot.message_handler(commands = ['brightness'])
def Brightness(message):
    # if message.id != my_id:
    #     return InfoUser(message)
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
        return bot.send_message(message.chat.id, 'Brightness must be > 0 and < 100')
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



@bot.message_handler(commands = ['info'])
def Info(message):
    bot.send_chat_action(message.chat.id, 'typing')
    text = f"Someone just used  *{message.text}*\n\n"
    text += f"Username:  *@{message.from_user.username}*\n"
    text += f"First Name:  *{message.from_user.first_name}*\n"
    if message.from_user.last_name != None:
        text += f"Last Name:  *{message.from_user.last_name}*\n"
    text += f"User Id:  *{message.from_user.id}*\n"
    bot.send_message(my_id, f'{text}', parse_mode = 'Markdown')



# TODO mouse
# @bot.message_handler(commands = ['mouse'])
# def changeMouse(message):



@bot.message_handler(commands = ['shutdown'])
def Shutdown(message):
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode = 'Markdown')
    bot.send_message(message.chat.id, 'How many *seconds* to turn off the PC?', parse_mode = 'Markdown')
    bot.register_next_step_handler(message, Shutdown_process)
def Shutdown_process(message):
    # TODO inline button
    if not message.text.isdigit():
        return bot.send_message(message.chat.id, 'Time must be a number')
    seconds = int(message.text)
    bot.send_message(message.chat.id, f'💤  Shutting down in *{seconds}s*', parse_mode = 'Markdown')
    os.system(f'shutdown -s -t {seconds}')



@bot.message_handler(commands = ['reboot'])
def Reeboot(message):
    if platform.system() != "Windows":
        return bot.send_message(message.chat.id, 'This feature is currently working only on *Windows*', parse_mode = 'Markdown')
    bot.send_message(message.chat.id, 'How many *seconds* to restart the PC?',parse_mode = 'Markdown')
    bot.register_next_step_handler(message, Reboot_process)
def Reboot_process(message):
    # TODO inline button
    if not message.text.isdigit():
        return bot.send_message(message.chat.id, 'Time must be a number')
    seconds = int(message.text)
    bot.send_message(message.chat.id, f'🔄  Reboot in *{seconds}s*', parse_mode = 'Markdown')
    os.system(f'shutdown -r -t {seconds}')



@bot.message_handler(commands = ['shutdown_cancel', 'reboot_cancel'])
def ShutdownCancel(message):
    os.system('shutdown /a')
    bot.send_message(message.chat.id, '🛑  Shutdown or Reboot *canceled*', parse_mode = 'Markdown')



bot.polling(none_stop = True)