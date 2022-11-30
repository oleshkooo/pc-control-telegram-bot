from pyautogui import press

from ...middleware import check


@check
def previousTrack(self):
    press('prevtrack')
    self.bot.send_message(self.message.chat.id, '*⏪  Previous track*', parse_mode = 'Markdown')


@check
def nextTrack(self):
    press('nexttrack')
    self.bot.send_message(self.message.chat.id, '*⏩  Next track*', parse_mode = 'Markdown')


@check
def playPauseTrack(self):
    press('playpause')
    self.bot.send_message(self.message.chat.id, '*⏯  Play/Pause track*', parse_mode = 'Markdown')
