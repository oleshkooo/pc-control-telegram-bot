from os import path as os_path
from subprocess import call

from ...middleware import check


@check
def openApp(self):
    if len(self.data.apps) == 0:
        self.bot.send_message(self.message.chat.id, '🫙 The app list is *empty*', parse_mode = 'Markdown')
        return
    
    self.bot.send_message(self.message.chat.id, '📝 Enter the app name:', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, openApp_process, self)


def openApp_process(message, self):
    name = self.message.text

    if name not in self.data.apps:
        self.bot.send_message(self.message.chat.id, f'⛔ *{name}* is *not in the list*', parse_mode = 'Markdown')
        return
    
    path = self.data.apps[name]

    if not os_path.exists(path):
        self.bot.send_message(self.message.chat.id, "⛔ App name is *incorrect* or the *app does not exist*", parse_mode = 'Markdown')
        return

    call(f"\"{path}\"", shell = True)   
    self.bot.send_message(self.message.chat.id, f'✅ Opening *{name}*', parse_mode = 'Markdown')