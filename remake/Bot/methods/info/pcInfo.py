from platform import uname
from psutil import cpu_count, virtual_memory

from .ip import getIP
from ...utils import getSize
from ...middleware import check


@check
def pcInfo(self):
    platformUname = uname()

    msg = '⚙️  *Info about your PC*\n\n'
    # OS
    msg += f'OS:  *{platformUname.system} {platformUname.release} {platformUname.version}*\n'
    msg += f'Name:  *{platformUname.node}*\n'
    # CPU
    msg += f'Processor:  *{platformUname.processor}*'
    msg += f'Core:  *{cpu_count(logical = True)}*\n'
    # RAM
    msg += f'📊  RAM: *{getSize(virtual_memory().total)}*\n'
    # IP
    msg += f'🛰️  IP: *{getIP()}*'
    self.bot.send_message(self.message.chat.id, msg, parse_mode = 'Markdown')
