from psutil import sensors_battery

from ...middleware import check


@check
def battery(self):
    battery = getBattery()
    status = isCharging()
    msg = f'{getBatteryEmoji(battery)}  Battery level is *{battery}*%\n'
    msg += f'{getChargingEmoji(status)}  Сharging:  *{status}*'
    self.bot.send_message(self.message.chat.id, msg, parse_mode = 'Markdown')


def getBattery():
    return sensors_battery().percent or 100


def isCharging():
    return sensors_battery().power_plugged


def getBatteryEmoji(battery):
    if battery <= 33:
        return '🪫'
    else:
        return '🔋'


def getChargingEmoji(isCharging):
    if isCharging:
        return '⚡️'
    else:
        return '🔌'