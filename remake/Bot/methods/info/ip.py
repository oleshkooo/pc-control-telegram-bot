from socket import gethostbyname, gethostname

from ...middleware import check


@check
def ip(self):
    self.bot.send_message(self.message.chat.id, f'🛰️ Your *IP* is *{getIP()}*', parse_mode = 'Markdown')


def getIP():
    return gethostbyname(gethostname())