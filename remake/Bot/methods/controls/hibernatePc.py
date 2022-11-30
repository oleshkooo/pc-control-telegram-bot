from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from subprocess import call
from time import sleep

from ...middleware import check

@check
def hibernatePc(self):
    self.hibernateFlag = False
    self.bot.send_message(self.message.chat.id, '⌛️ After how many *seconds* to *hibernate* your PC?', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, hibernatePc_process, self)


def hibernatePc_process(message, self):
    if not self.message.text.isdigit():
        return self.bot.send_message(self.message.chat.id, 'Time must be a number')

    seconds = int(self.message.text)    
    markupInlineCancelHibernate = InlineKeyboardMarkup()
    btnCancelHibernate = InlineKeyboardButton(text = 'Cancel', callback_data = 'cancelHibernate')
    markupInlineCancelHibernate.add(btnCancelHibernate)
    self.bot.send_message(self.message.chat.id, f'💤 Hibernating in *{seconds}s*', parse_mode = 'Markdown', reply_markup = markupInlineCancelHibernate)
    
    for i in range(seconds):
        sleep(1)
        if self.hibernateFlag:
            self.hibernateFlag = False
            return
        
    call('shutdown /h', shell = True)   