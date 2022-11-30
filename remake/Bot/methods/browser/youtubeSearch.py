from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from youtubesearchpython import VideosSearch

from ...middleware import check


@check
def youtubeSearch(self):
    self.bot.send_message(self.message.chat.id, '🔍 Enter search query:', parse_mode = 'Markdown')
    self.bot.register_next_step_handler(self.message, youtube_process, self)


def youtube_process(message, self):
    query = self.message.text
    search = VideosSearch(query, limit = self.MAX_SEARCH_LEN)
    result = search.result()
    markupInlineYtSearch = InlineKeyboardMarkup()

    for index in range(len(result['result'])):
        callback = f'ytSearch_{index}'
        title = result['result'][index]['title']
        duration = result['result'][index]['duration']
        link = result['result'][index]['link']
        self.ytResults.append({
            'callback': callback,
            'title': title,
            'duration': duration,
            'link': link
        })
        btnYtSearch = InlineKeyboardButton(text = f'{duration} • {title}', callback_data = callback)
        markupInlineYtSearch.add(btnYtSearch)

    if len(self.ytResults) > 0:
        self.bot.send_message(self.message.chat.id, f'🎥 Results for *{query}*', parse_mode = 'Markdown', reply_markup = markupInlineYtSearch, disable_web_page_preview = True)
    else:
        self.bot.send_message(self.message.chat.id, f'🎥 There are *no results* for *{query}*', parse_mode = 'Markdown')