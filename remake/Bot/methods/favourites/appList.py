from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from ...middleware import check


@check
def appList(self):
    if len(self.data.apps) == 0:
        self.bot.send_message(self.message.chat.id, '🫙 The app list is *empty*', parse_mode = 'Markdown')
        return

    markupInline = InlineKeyboardMarkup()

    for key in self.data.apps:
        callback = key
        btn = InlineKeyboardButton(text = f'{key}',callback_data = callback)
        markupInline.add(btn)

    self.bot.send_message(self.message.chat.id,'📃 Favourite apps list:', parse_mode = 'Markdown', reply_markup = markupInline)
