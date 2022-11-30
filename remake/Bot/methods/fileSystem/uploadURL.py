from os import path as os_path
from ...middleware import check


@check
def uploadURL(message):
    self.bot.send_message(self.message.chat.id,'🔗 Enter *URL*', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, uploadURL_process, self)


def uploadURL_process(message, self):
    url = self.message.text
    self.bot.send_chat_action(self.self.message.chat.id, 'upload_document')
    path = os_path.expanduser('~') + '\\Desktop\\'
    obj = SmartDL(url, path, progress_bar = False)
    self.bot.send_message(self.message.chat.id, '⌛️ File is loading, please wait...')
    obj.start()
    self.bot.send_message(self.message.chat.id, f'✅ Successfully downloaded')    