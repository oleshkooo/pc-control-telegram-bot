from ...utils import openInBrowser
from ...middleware import check


@check
def browserURL(self):
    self.bot.send_message(self.message.chat.id, '🌐 Enter URL:', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, browserURL_process, self)


def browserURL_process(message, self):
    url = self.message.text
    openInBrowser(f'https://{url}')