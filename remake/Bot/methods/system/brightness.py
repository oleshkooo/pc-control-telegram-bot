from screen_brightness_control import get_brightness, set_brightness

from ...middleware import check


@check
def brightness(self):
    currentBrightness = getBrightness()
    emoji = getBrightnessEmoji(currentBrightness)
    self.bot.send_message(self.message.chat.id, f'{emoji} Current brightness is *{currentBrightness}%*', parse_mode = 'Markdown')
    self.bot.send_message(self.message.chat.id, 'Enter new brightness:')
    self.bot.register_next_step_handler(self.message, brightness_process, self)


def brightness_process(message, self):
    brightness = self.message.text

    if not brightness.isdigit():
        self.bot.send_message(self.message.chat.id, 'Brightness must be a number')
        return

    brightnessInt = int(brightness)

    if brightnessInt < 0 or brightnessInt > 100:
        self.bot.send_message(self.message.chat.id, 'Brightness must be *> 0* and *< 100*', parse_mode = 'Markdown')
        return

    emoji = getBrightnessEmoji(brightnessInt)
    set_brightness(brightnessInt)
    self.bot.send_message(self.message.chat.id, f'{emoji} Brightness set to *{self.message.text}%*', parse_mode = 'Markdown')


def getBrightness():
    return get_brightness()[0]


def getBrightnessEmoji(brightness):
    if brightness < 33: return '🔅'
    elif brightness < 66: return '🔆'
    else: return '☀️'