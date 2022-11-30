from os import path as os_path

from ...utils import writeToFile
from ...middleware import check


@check
def addApp(self):
    self.bot.send_message(self.message.chat.id,f'📝 Enter the application *path*', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, addApp_process_1, self)


def addApp_process_1(message, self):
    self.appPath = self.message.text

    if not os_path.exists(self.appPath):
        self.bot.send_message(self.message.chat.id, "⛔ The *path* is *incorrect* or the *file does not exist*", parse_mode = 'Markdown')
        return

    for key, value in self.data.apps.items():
        if value == self.appPath:
            self.bot.send_message(self.message.chat.id, f"⛔ *{key}* is already in the list", parse_mode = 'Markdown')
            return

    self.bot.send_message(self.message.chat.id,f'📝 Enter the *name* of the application', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, addApp_process_2, self)


def addApp_process_2(message, self):
    name = self.message.text
    newApp = {
        name: self.appPath
    }

    self.data.apps = {**self.data.apps, **newApp}
    writeToFile(self.data)
    self.bot.send_message(self.message.chat.id,f'✅ *{name}* has been successfully added to the list', parse_mode = 'Markdown')