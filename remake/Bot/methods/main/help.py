from ...middleware import check

@check
def help(self):
    self.bot.send_message(self.message.chat.id,
'''
*ℹ️  Information about bot:*\n\n
*🚀  /start* - Start bot\n
*⛔  /stop* - Stop bot\n
*ℹ️   /help* - Commands list\n
*🏃‍♀️  /autorun_on* - Run the bot after turning on the PC\n
*🚫  /autorun_off* - Disable bot autorun\n

*☀️  /brightness* - Set brightness to [value]\n
*🔊  /volume* - Set volume to [value]\n
*🏞  /screenshot* - Take a screenshot\n

*🔋  /battery* - Show battery status\n
*🛰️  /ip* - Get your IP\n
*🆔  /id * - Get your telegram ID\n
*⚙️  /info* - Show PC info\n
*🖥️  /status* - Show PC status\n

*⌨️  /keylogger* - Turn on keylogger\n
*🗨️ /write* - Enter the text like from keyboard\n
*🗳️  /msgbox* - Displays a message on the PC screen\n
*🖱  /mouse* - Set mouse position\n
*👨‍💻  /cmd* - Run command\n
*💀  /kill* - Kill process\n

*⏪  /prev* - Previous track\n
*⏩  /next* - Next track\n
*⏯  /playpause* - Play/Pause track\n
*📗  /collapse* - Collapse the program\n
*📖  /show* - Show the program\n
*❌  /close* - Close current program\n
*📕  /close_tab* - Close current tab\n
*📺  /fullscreen* - Fullscreenf for program\n
*📺  /fullmedia* - Fullscreen for movie\n

*👟  /app* - Open application\n
*📃  /apps* - Favourite applications\n
*➕  /add_app* - Add application to favourites\n
*➖  /remove_app* - Remove application from favourites\n

*🌐  /browser* - Open URL in browser\n
*🔍  /search* - Search in browser\n
*▶️  /youtube* - Search in youtube\n

*🔒  /lock* - Lock your PC\n
*⚠️  /shutdown* - Shutdown your PC\n
*🔄  /reboot* - Restart your PC\n
*💤  /hibernate* - Hibernate your PC\n

*⬇️  /download* - Download file from PC\n
*⬆️  /upload* - Upload file to PC\n
*🕸️  /upload_url* - Upload file from URL\n
''',
    parse_mode = 'Markdown')