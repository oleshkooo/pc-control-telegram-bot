from subprocess import call

from ...middleware import check


@check
def killProcess(self):
    self.bot.send_message(self.message.chat.id,'💀 Enter the *name* of the *process* you want to *kill*:', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, killProcess_process, self)


def killProcess_process(message, self):
    if not call("taskkill /IM " + self.message.text + " -F", shell = True):
        self.bot.send_message(self.message.chat.id,f'🔪 *{message.text}* process was *killed*', parse_mode = 'Markdown')
    else:
        self.bot.send_message(self.message.chat.id,'⛔ Process not found', parse_mode = 'Markdown')
