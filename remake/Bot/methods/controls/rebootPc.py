from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from subprocess import call

from ...middleware import check


@check
def rebootPc(self):
    self.bot.send_message(self.message.chat.id, '⌛️ After how many *seconds* to *reboot* your PC?', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, rebootPc_process, self)


def rebootPc_process(message, self):
    if not self.message.text.isdigit():
        self.bot.send_message(self.message.chat.id, 'Time must be a number')
        return

    seconds = int(self.message.text)
    markupInlineCancelReboot = InlineKeyboardMarkup()
    btnCancelReboot = InlineKeyboardButton(text = 'Cancel', callback_data = 'cancelReboot')
    markupInlineCancelReboot.add(btnCancelReboot)
    call(f'shutdown -r -t {seconds}', shell = True)
    self.bot.send_message(self.message.chat.id, f'🔄 Reboot in *{seconds}s*', parse_mode = 'Markdown', reply_markup = markupInlineCancelReboot)