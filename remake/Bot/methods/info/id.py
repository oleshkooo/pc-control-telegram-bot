from socket import gethostbyname, gethostname

from ...middleware import check


@check
def id(self):
    self.bot.send_message(self.message.from_user.id, f'🆔  Your *ID* is *{getID(self)}*', parse_mode = 'Markdown')


def getID(self):
    return self.message.from_user.id