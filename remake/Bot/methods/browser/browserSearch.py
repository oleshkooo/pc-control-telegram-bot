from ...utils import openInBrowser
from ...middleware import check


@check
def browserSearch(self):
    self.bot.send_message(self.message.chat.id, '🔍 Enter search query:', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, browserSearch_process, self)


def browserSearch_process(message, self):
    query = self.message.text
    self.bot.send_message(self.message.chat.id, f'🔍 Searching *{query}*', parse_mode = 'Markdown')
    openInBrowser(f'https://www.google.com/search?q={query}')