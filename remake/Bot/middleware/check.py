def check(f):
    def wrapper(*args, **kwargs):
        # self = args[0]
        # if self.message.from_user.username == self.data.USER:
        #     f(*args, **kwargs)
        # else:
        #     self.bot.send_message(self.message.chat.id, '⚠️  *Warning*\n\n' + 'You are not allowed to use this bot', parse_mode = 'Markdown')



        try:
            self = args[0]

            try:
                if self.message.from_user.username == self.data.USERNAME:
                    f(*args, **kwargs)
                else:
                    self.bot.send_message(self.message.chat.id, '⚠️  *Warning*\n\n' + 'You are not allowed to use this bot', parse_mode = 'Markdown')

            except Exception as e:
                self.bot.send_message(self.message.chat.id, '*⛔  Error occurred*', parse_mode = 'Markdown')
                print(e)
                return

        except:
            pass

    return wrapper