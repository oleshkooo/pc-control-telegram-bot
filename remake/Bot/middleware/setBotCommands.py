from telebot.types import BotCommand


def setBotCommands(self):
    try:
        self.bot.set_my_commands([
            BotCommand('/start', 'Start Bot'),
            BotCommand('/stop', 'Stop bot'),
            BotCommand('/help', 'Commands list'),
            BotCommand('/autorun_on', 'Run the bot after turning on the PC'),
            BotCommand('/autorun_off', 'Disable bot autorun'),

            BotCommand('/brightness', 'Set brightness to [value]'),
            BotCommand('/volume', 'Set volume to [value]'),
            BotCommand('/screenshot', 'Take a screenshot'),

            BotCommand('/battery', 'Show battery status'),
            BotCommand('/ip', 'Get your IP'),
            BotCommand('/id', 'Get your telegram ID'),
            BotCommand('/info', 'Show PC info'),
            BotCommand('/status', 'Show PC status'),

            BotCommand('/keylogger', 'Turn on keylogger'),
            BotCommand('/write', 'Enter the text like from keyboard'),
            BotCommand('/text', 'Enter the text like from keyboard'),
            BotCommand('/msgbox', 'Displays a message on the PC screen'),
            BotCommand('/mouse', 'Set mouse position'),
            BotCommand('/cmd', 'Run command'),
            BotCommand('/kill', 'Kill process'),

            BotCommand('/previous', 'Previous track'),
            BotCommand('/next', 'Next track'),
            BotCommand('/skip', 'Next track'),
            BotCommand('/play', 'Play/Pause track'),
            BotCommand('/pause', 'Play/Pause track'),
            BotCommand('/collapse', 'Collapse the program'),
            BotCommand('/show', 'Show the program'),
            BotCommand('/close', 'Close current program'),
            BotCommand('/close_tab', 'Close current tab'),
            BotCommand('/fullscreen', 'Fullscreenf for program'),
            BotCommand('/fullmedia', 'Fullscreen for movie'),

            BotCommand('/app', 'Open application'),
            BotCommand('/apps', 'Favourite applications'),
            BotCommand('/add_app', 'Add application to favourites'),
            BotCommand('/remove_app', 'Remove application from favourites'),

            BotCommand('/browser', 'Open URL in browser'),
            BotCommand('/search', 'Search in browser'),
            BotCommand('/youtube', 'Search in youtube'),

            BotCommand('/lock', 'Lock your PC'),
            BotCommand('/shutdown', 'Shutdown your PC'),
            BotCommand('/reboot', 'Restart your PC'),
            BotCommand('/hibernate', 'Hibernate your PC'),
            BotCommand('/sleep', 'Hibernate your PC'),

            BotCommand('/download', 'Download file from PC'),
            BotCommand('/upload', 'Upload file to PC'),
            BotCommand('/upload_url', 'Upload file from URL'),
        ])

    except Exception as e:
        pass
