from os import getpid
from subprocess import call

from ...middleware import check


@check
def stopBot(self):
    self.bot.send_message(self.message.chat.id, '*⛔  Bot stopped*', parse_mode = 'Markdown')
    call('taskkill /f /im host.exe', shell = True)
    pid = str(getpid())
    call(f'taskkill /PID {pid} /F', shell = True)