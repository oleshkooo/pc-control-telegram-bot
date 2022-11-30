# ? buttons
# noneBtn types.InlineKeyboardMarkup()

# __menu
# menu_keyboadr = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = False)
# btnWatch = types.KeyboardButton('📺 Music or movie')

# menu_keyboadr.row(btnWatch)


# TODO mouse keyboard
# mouseButton
# mouse_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
# btnup = types.KeyboardButton('⬆️')
# btndown = types.KeyboardButton('⬇️')
# btnLeft = types.KeyboardButton('⬅️')
# btnRight = types.KeyboardButton('➡️')
# btnClick = types.KeyboardButton('🆗')
# btnCancel = types.KeyboardButton('⛔ Stop')
# btncurs = types.KeyboardButton('Specify the cursor range')
# mouse_keyboard.row(btnup)
# mouse_keyboard.row(btnLeft, btnClick, btnRight)
# mouse_keyboard.row(btndown)
# mouse_keyboard.row(btncurs, btnCancel)

# delButtons = types.ReplyKeyboardRemove()

# #homeButton

# home_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = False)


# pg = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = False)
# btnShutdown = types.KeyboardButton('⚠️ Shutdown')
# btnReboot = types.KeyboardButton('🔄 Reboot')
# btnSleep = types.KeyboardButton('💤 Sleep')
# btnLock = types.KeyboardButton('🔒 Lock')

# home_keyboard.row(btnShutdown, btnReboot,btnSleep,btnLock)

# #contol music and video
# pgControlWatch = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = False)
# btnVol = types.KeyboardButton('🔊 Volume')
# btnBright = types.KeyboardButton('☀️ Brightness')
# btnYoutube = types.KeyboardButton('▶️ Youtube')
# btnSearch = types.KeyboardButton('🔍 Search')
# btnBrowser = types.KeyboardButton('🌐 Browser')
# btnFullscreen = types.KeyboardButton('📺\ Fullscreen')
# btnFullMedia = types.KeyboardButton('📺 FullMedia')
# btnPrev = types.KeyboardButton('⏪ Prev')
# btnPause = types.KeyboardButton('⏯\n Pause')
# btnNext = types.KeyboardButton('⏩ Next')
# btnBack = types.KeyboardButton('🔙 Back')
# btnClose = types.KeyboardButton('❌ Close app')

# pgControlWatch.row(btnYoutube,btnSearch,btnBrowser)
# pgControlWatch.row(btnBright,btnVol,btnFullMedia)
# pgControlWatch.row(btnPrev,btnPause,btnNext)
# pgControlWatch.row(btnBack,btnFullscreen,btnClose)





# @bot.message_handler(content_types = 'text')
# def menu_process(message):
#     text = message.text
    
#     if text == '📺 Music or movie':
#        bot.send_message(message.chat.id, f'👟 Moved to category *{text}*',parse_mode = 'Markdown',reply_markup = pgControlWatch)
#        bot.register_next_step_handler(message, watch_process)
#     elif text == '1':
#         pass
# def watch_process(message):
#     text = message.text
#     if text == '▶️ Youtube':
#         bot.send_message(message.chat.id, 'Enter the URL')
#         bot.register_next_step_handler(message, Youtube_process)
#         bot.register_next_step_handler(message, watch_process)
#     elif text == '🔙 Back':
#    #    bot.send_message(message.chat.id, f'👟 Moved to *Menu*',parse_mode = 'Markdown',reply_markup = menu_keyboadr)
#        bot.register_next_step_handler(message, menu_process)