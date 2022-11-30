from os import ( path as os_path, remove as os_remove )
from mss import mss
# import PIL

from ...middleware import check


@check
def screenshot(self):
    self.bot.send_chat_action(self.message.chat.id ,'upload_photo')
    self.screenshotCount += 1

    with mss() as screen:
        screen.shot(mon = -1, output = f'Screenshot{self.screenshotCount}.png')

    if not os_path.exists(f'./Screenshot{self.screenshotCount}.png'):
        self.bot.send_message(self.message.chat.id, '*🏞  Error*, screenshot not found', parse_mode = 'Markdown')
        return

    self.bot.send_message(self.message.chat.id, '*Done ✅*', parse_mode = 'Markdown')
    file = open(f'Screenshot{self.screenshotCount}.png', 'rb')
    self.bot.send_document(self.message.chat.id, file)
    file.close()

    if os_path.exists(f'Screenshot{self.screenshotCount}.png'):
        os_remove(f'Screenshot{self.screenshotCount}.png')


# def screenshotWithMouse(message):
#     try:
#         currentMouseX, currentMouseY  =  mouse.get_position()
#         img = PIL.ImageGrab.grab()
#         img.save("screen.png", "png")
#         img = PIL.Image.open("screen.png")
#         draw = PIL.ImageDraw.Draw(img)
#         draw.polygon((currentMouseX, currentMouseY, currentMouseX, currentMouseY + 15, currentMouseX + 10, currentMouseY + 10), fill="white", outline="black")
#         img.save("screen_with_mouse.png", "PNG")
#         bot.send_photo(message.chat.id, open("screen_with_mouse.png", "rb"))
#         os.remove("screen.png")
#         os.remove("screen_with_mouse.png")
#     except:
#         bot.send_message(message.chat.id,'*⛔  Error occurred*', parse_mode = 'Markdown')