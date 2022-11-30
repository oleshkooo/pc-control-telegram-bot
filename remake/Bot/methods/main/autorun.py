import os as os_path
from pathlib import Path

from ...utils import createShortcut
from ...middleware import check

@check
def autorunOn(self):
    pathToStartup = os_path.expanduser('~') + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\PC Control Bot Host.lnk'

    if not os_path.exists(pathToStartup):
        abs_file_name = os_path.abspath('.') + '\\host\\host.exe'
        pathToFile = Path(abs_file_name)
        createShortcut(
            fileName = pathToStartup,
            target = str(pathToFile),
            workDir = str(pathToFile.parent),
            args ='/cmd {%s} -new_console' % 'PС Control Bot Host',
        )
        self.bot.send_message(self.message.chat.id, '✅ bot is added to autorun')
        return

    self.bot.send_message(self.message.chat.id, '⛔ Bot is already in autorun')


@check
def autorunOff(self):
    PATH = os_path.expanduser('~') + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\PC Control Bot Host.lnk'

    if not os_path.exists(PATH):
        self.bot.send_message(self.message.chat.id, '⛔ *PC Control Bot Host* is not added to the *Start Menu*', parse_mode = 'Markdown')
        return

    os.remove(PATH)
    self.bot.send_message(self.message.chat.id, '✅ *PC Control Bot Host* is removed from the *Start Menu*', parse_mode = 'Markdown')
