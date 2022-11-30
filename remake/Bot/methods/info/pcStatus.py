from psutil import cpu_percent, virtual_memory

from ..system.brightness import getBrightness, getBrightnessEmoji
from ..system.volume import getVolume, getVolumeEmoji
from .battery import getBattery, getBatteryEmoji, isCharging, getChargingEmoji
from ...utils import getSize
from ...middleware import check


@check
def pcStatus(self):
    virtualMem = virtual_memory()
    battery = getBattery()
    chargingStatus = isCharging()
    brightness = getBrightness()
    volume = getVolume(self)

    msg = '🖥️  *Your PC Status*\n\n'
    msg += f'📊  Total CPU Usage:  *{cpu_percent()}%*\n'
    msg += f'🆓  RAM Available:  *{getSize(virtualMem.available)}* / {getSize(virtualMem.total)}\n'
    msg += f'📟  RAM Used:  *{getSize(virtualMem.used)}* / {getSize(virtualMem.total)}\n'
    msg += f'📊  RAM used percentage:  *{virtualMem.percent}%*\n\n'
    msg += f'{getBatteryEmoji(battery)}  Battery level:  *{battery}%*\n'
    msg += f'{getChargingEmoji(chargingStatus)}  Сharging:  *{chargingStatus}*\n'
    msg += f'{getBrightnessEmoji(brightness)}  Brightness:  *{brightness}%*\n'
    msg += f'{getVolumeEmoji(volume)}  Volume:  *{volume}%*\n'
    self.bot.send_message(self.message.chat.id, msg, parse_mode = "markdown")
