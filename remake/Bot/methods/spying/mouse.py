import mouse
from ..middleware import check


@check
def mouse(self):
    # TODO mouse
    pass
    # self.bot.send_message(self.message.chat.id, '🖱  *Mouse* is *now* *controlled*', reply_markup = mouse_keyboard, parse_mode = 'Markdown' )
    # bot.register_next_step_handler(message, Mouse_process)


def mouse_process(message):
    if message.text == "⬆️":
        bot.send_chat_action(message.chat.id ,'upload_photo')
        currentMouseX,  currentMouseY  =  mouse.get_position()
        mouse.move(currentMouseX,  currentMouseY - curs)
        bot.register_next_step_handler(message, Mouse_process)
        screenWithMouse(message)
    elif message.text == "⬇️":
        bot.send_chat_action(message.chat.id ,'upload_photo')
        
        currentMouseX,  currentMouseY  =  mouse.get_position()
        mouse.move(currentMouseX,  currentMouseY + curs)
        bot.register_next_step_handler(message, Mouse_process)
        screenWithMouse(message)

    elif message.text == "⬅️":
        bot.send_chat_action(message.chat.id ,'upload_photo')
        
        currentMouseX,  currentMouseY  =  mouse.get_position()
        mouse.move(currentMouseX - curs,  currentMouseY)
        bot.register_next_step_handler(message, Mouse_process)
        screenWithMouse(message)


    elif message.text == "➡️":
        bot.send_chat_action(message.chat.id ,'upload_photo')
        
        currentMouseX,  currentMouseY  =  mouse.get_position()
        mouse.move(currentMouseX + curs,  currentMouseY)
        bot.register_next_step_handler(message, Mouse_process)
        screenWithMouse(message)


    elif message.text == "🆗":
        bot.send_chat_action(message.chat.id ,'upload_photo')
        mouse.click()
        bot.register_next_step_handler(message, Mouse_process)
        screenWithMouse(message)
       
    elif message.text == '⛔ Stop':
        bot.send_message(message.chat.id, '🛑  *Mouse control* is terminated', parse_mode = 'Markdown',reply_markup = delButtons)

    elif message.text == 'Specify the cursor range':
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id, f"Specify a new cursor range, now this value is equal to *{str(curs)}px*", parse_mode = 'Markdown')
        bot.register_next_step_handler(message, MouseSettings_process)


def mouseSettings_process(message, self):
    global curs
    if message.text.isdigit():
        curs = int(message.text)
        bot.send_message(message.chat.id, f"✅ Changed successfully")
        bot.register_next_step_handler(message, Mouse_process)
    else:
        bot.send_message(message.chat.id, "⛔ Incorrect value", reply_markup = mouse_keyboard)
        bot.register_next_step_handler(message, Mouse_process)
