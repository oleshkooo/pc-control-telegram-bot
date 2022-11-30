from os import path as os_path

from ...utils import writeToFile
from ...middleware import check


@check
def removeApp(self):
    if len(self.data.apps) == 0:
        self.bot.send_message(self.message.chat.id, '🫙 The app list is *empty*', parse_mode = 'Markdown')
        return

    self.bot.send_message(self.message.chat.id,'📝 Enter *app name* to *remove*', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, removeApp_process, self)


def removeApp_process(message, self):
    name = self.message.text

    if name not in self.data.apps:
        self.bot.send_message(self.message.chat.id, f'⛔ *{name}* is *not in the list*', parse_mode = 'Markdown')
        return

    del self.data.apps[name]
    writeToFile(self.data)
    self.bot.send_message(self.message.chat.id, f'✅ *{name}* was removed successfully', parse_mode = 'Markdown')