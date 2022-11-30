from ctypes import windll

from ...middleware import check


@check
def lockPc(self):
    windll.user32.LockWorkStation()
    self.bot.send_message(self.message.chat.id, '*🔒 Locked*', parse_mode = 'Markdown')