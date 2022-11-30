from ...middleware import check


@check
def volume(self):
    currentVolume = getVolume(self)
    emoji = getVolumeEmoji(currentVolume)
    self.bot.send_message(self.message.chat.id, f'{emoji} Current volume is *{currentVolume}%*', parse_mode = 'Markdown')
    self.bot.send_message(self.message.chat.id, 'Enter new volume:')
    self.bot.register_next_step_handler(self.message, volume_process, self)


def volume_process(message, self):
    volume = self.message.text
    volumeInt = int(volume)

    if volumeInt < 0 or volumeInt > 100:
        self.bot.send_message(self.message.chat.id, 'Volume must be *> 0* and *< 100*', parse_mode = 'Markdown')
        return

    emoji = getVolumeEmoji(volumeInt)
    scalarVolume = volumeInt / 100
    self.vol.SetMasterVolumeLevelScalar(scalarVolume, None)
    self.bot.send_message(self.message.chat.id, f'{emoji} Volume set to *{self.message.text}%*', parse_mode = 'Markdown')


def getVolume(self):
    return int(round(self.vol.GetMasterVolumeLevelScalar() * 100))


def getVolumeEmoji(volume):
    if volume == 0: return '🔇'
    elif volume <= 33: return '🔈'
    elif volume <= 66: return '🔉'
    else: return '🔊'