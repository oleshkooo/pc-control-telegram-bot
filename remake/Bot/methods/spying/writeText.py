from pyautogui import typewrite

from ...middleware import check


@check
def writeText(self):
    self.bot.send_message(self.message.chat.id, '💬  Enter text to *write*:', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, writeText_process, self)


def writeText_process(message, self):
    text = self.message.text
    self.bot.send_chat_action(self.message.chat.id, 'typing')
    self.bot.send_message(self.message.chat.id, f'*✏️  Writing text*  "{text}"', parse_mode = 'Markdown')
    typewrite(text, interval = 0.02)
