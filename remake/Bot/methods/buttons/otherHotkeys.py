from pyautogui import hotkey, press

from ...middleware import check


@check
def closeTab(self):
    hotkey('ctrl', 'w')
    self.bot.send_message(self.message.chat.id, '❌ *Tab closed*', parse_mode = 'Markdown')


@check
def fullscreen(self):
    press('f11')
    self.bot.send_message(self.message.chat.id, '📺  *Program* is *fullscreen* now', parse_mode = 'Markdown')


@check
def fullscreenMedia(self):
    press('f')
    self.bot.send_message(self.message.chat.id, '📺  *Movie* is *fullscreen* now', parse_mode = 'Markdown')
