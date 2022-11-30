from os import path as os_path
from ...middleware import check


@check
def downloadFile(self):
        self.bot.send_message(self.message.chat.id,'🛣️ Enter the file path')
        self.bot.register_next_step_handler(self.message, downloadFile_process, self)


def downloadFile_process(message, self):
    path = self.message.text
    self.bot.send_chat_action(self.message.chat.id, 'upload_document')

    if not os_path.exists(path):
        self.bot.send_message(self.message.chat.id, "⛔ The *path* is *incorrect* or the *file does not exist*", parse_mode = 'Markdown')
        return

    self.bot.send_message(self.message.chat.id, "⌛️ File is loading, please wait...")
    file = open(path, 'rb')
    self.bot.send_document(self.message.chat.id, file)
    file.close()
        