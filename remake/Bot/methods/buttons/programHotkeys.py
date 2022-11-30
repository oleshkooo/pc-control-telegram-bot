from pyautogui import hotkey

from ...middleware import check


@check
def collapseProgram(self):        
    hotkey('win', 'm')
    self.bot.send_message(self.message.chat.id, '✅ Program *collapsed*', parse_mode = 'Markdown')


@check
def showProgram(self):
    hotkey('win', 'shiftleft', 'm')
    self.bot.send_message(self.message.chat.id, '✅ Program *showed*', parse_mode = 'Markdown')


@check
def closeProgram(self):
    self.bot.send_message(self.message.chat.id, '❌ Program *closed*', parse_mode = 'Markdown')
    hotkey('altleft', 'f4')