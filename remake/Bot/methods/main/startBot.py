from ...middleware import check


@check
def startBot(self):
    self.bot.send_message(self.message.chat.id, '🚀 Bot launched')
    self.bot.send_message(self.message.chat.id, 'Use  */help*  for more info', parse_mode = 'Markdown')