from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from subprocess import call

from ...middleware import check


@check
def shutdownPc(self):
    self.bot.send_message(self.message.chat.id, '⌛️ After how many *seconds* to *shutdown* your PC?', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, shutdownPc_process, self)


def shutdownPc_process(message, self):
    if not message.text.isdigit():
        self.bot.send_message(self.message.chat.id, 'Time must be a number')
        return

    seconds = int(message.text)
    markupInlineCancelShutdown = InlineKeyboardMarkup()
    btnCancelShutdown = InlineKeyboardButton(text = 'Cancel', callback_data = 'cancelShutdown')
    markupInlineCancelShutdown.add(btnCancelShutdown)
    self.bot.send_message(self.message.chat.id, f'⚠️ Shutting down in *{seconds}s*', parse_mode = 'Markdown', reply_markup = markupInlineCancelShutdown)
    call(f'shutdown -s -t {seconds}', shell = True)   