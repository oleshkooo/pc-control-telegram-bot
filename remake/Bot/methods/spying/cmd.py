from subprocess import call, check_output

from ...middleware import check


@check
def cmd(self):
    self.bot.send_message(self.message.chat.id, '*👨‍💻 Enter command*', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, cmd_process, self)


def cmd_process(message, self):
    command = self.message.text
    # TODO cmd
    # result = call(f'{command}', shell = True, stdout=PIPE).stdout
    result = check_output(f'{command}', shell = True, text = True)
    self.bot.send_message(self.message.chat.id, result)

    # if command == '':
    #     self.bot.send_message(self.message.chat.id, '*⚠️ Enter command*', parse_mode = 'Markdown')
    # elif not call(f'{command}', shell = True) and not command == 'cmd':
    #     self.bot.send_message(self.message.chat.id, '*✅ Command success*', parse_mode = 'Markdown')
    # else:
    #     self.bot.send_message(self.message.chat.id, '*⛔ Command failed*', parse_mode = 'Markdown')
