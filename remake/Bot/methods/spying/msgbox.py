from threading import Thread

from ...middleware import check


@check
def msgbox(self):
    self.bot.send_message(self.message.chat.id, '📝 Enter the text that should be displayed on the screen')
    self.bot.register_next_step_handler(self.message, msgbox_process, self)


def msgbox_process(message, self):
    self.bot.send_chat_action(self.message.chat.id, 'typing')
    th = Thread(target = msgbox_thread(self), args = (), daemon = True)
    th.start()
    self.bot.send_message(self.message.chat.id, f'📕 Messagebox was *closed*',parse_mode = 'Markdown')


def msgbox_thread(self):
    self.messageBox(None, self.message.text, 'PC Control Bot', 0)
