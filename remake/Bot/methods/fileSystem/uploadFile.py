from os import path as os_path
from ...middleware import check


@check
def uploadFile(self):
    self.bot.send_message(self.message.chat.id,'💾 Send *file* a file to *upload*', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, uploadFile_process, self)


def uploadFile_process(message, self): 
    self.bot.send_chat_action(self.message.chat.id, 'upload_document')
    file_info = self.bot.get_file(self.message.document.file_id)
    downloaded_file = self.bot.download_file(file_info.file_path)
    src = os_path.expanduser('~') + '\\Desktop\\' + self.message.document.file_name        
    
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)

    self.bot.send_message(self.message.chat.id, '✅ *File* was successfully *uploaded*', parse_mode = 'Markdown')