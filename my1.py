import telebot
from telebot import types
import constants
import random




#1946911081:AAFY09FOeJRZ16bf4cN2LWRFDauuLHTjV0U
banner = 'Если хочешь посочнее используй "+" или "-"', 'Твои яйца не готовы осилить такой напор? Другое? Используй "+" или "-"','Ты слишком скромен? Используй "+" или "-"?','Нужен другой подход? Используй "+" или "-"'
banner_choice = lambda: random.choice(banner)
message_store = 'Глядя на тебя , сразу вспомнил домашнее задание с доски, хочется сфоткать и сделать уже всё дома.','А на тебе зимой случайно бомжи не спят? А то ты настолько красивая , что труба!',\
                'Скажу как мой дед, когда говорил своей ласточке: Да хорош ломаться, поехали!','Говорят все крошки любят плохишей? Я голосовал не за ЕР. Зажглось?','Ты как дохлая кошка на асфальте , хочется тыкать в тебя из любопытства',\
                'Ты как маникен из магазина, все что на тебе , так и хочется порвать','Ты такая маленькая,миленькая, прям как муровейчик. Кстати , если хочешь поднять вес в 100 раз больше своего , можешь поднять мой член.',\
                'Я,конечно, не из того же города , что и Мила Кунис , но Кунис у меня неплохо получается','Я конечно не больной , но постельный режим с тобой готов соблюдать'
message_winner = lambda: random.choice(message_store)


bot = telebot.TeleBot("1946911081:AAFY09FOeJRZ16bf4cN2LWRFDauuLHTjV0U", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Эй чорт, какой start')
    bot.send_message(message.chat.id, 'Поздаровайся со мной , если не хочешь всю оставшуюуся жизнь лимонить свой стручок и видеть голых девочек только на картинке')
    bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(content_types=['text'])
def echo_all(message):
    if message.text == 'Привет':
        bot.reply_to(message, 'Йоу-йоу-йоу, парнишка! Ты оказался там где надо! Сегодня ты очистишь историю браузера и навсегда забудешь баннер прнхаба!'
                              ' Напиши /lonely , чтобы наконец-то я помог тебе!')
    elif message.text == 'привет':
        bot.reply_to(message, 'Йоу-йоу-йоу, парнишка! Ты оказался там где надо! Сегодня ты очистишь историю браузера и навсегда забудешь баннер прнхаба!'
                              ' Напиши /lonely , чтобы наконец-то я помог тебе!')
    elif message.text == '/lonely':
        bot.send_message(message.chat.id, 'П - поехали')
        bot.send_message(message.chat.id,str(message_winner()))
        bot.send_message(message.chat.id,str(banner_choice()),)
    elif message.text == 'Да':
        bot.reply_to(message, 'Лови подкат:')
        bot.send_message(message.chat.id, str(message_winner()))
        bot.send_message(message.chat.id, 'Еще? (Напиши "+" или "-")' )
    elif message.text == '+':
        bot.send_message(message.chat.id, str(message_winner()))
        bot.send_message(message.chat.id, str(banner_choice()), )
    elif message.text == '-':
        bot.reply_to(message, 'Буква Ю \nШишка задымится , вспомнишь обо мне')

    elif message.text == 'да':
        bot.reply_to(message, 'Лови подкат:')
        bot.send_message(message.chat.id, str(message_winner()))
        bot.send_message(message.chat.id, 'Еще? (Напиши "+" или "-")' )
    elif message.text == 'yes':
        bot.reply_to(message, 'Лови подкат:')
        bot.send_message(message.chat.id, str(message_winner()))
        bot.send_message(message.chat.id, 'Еще? (Напиши "+" или "-")' )



bot.remove_webhook()

bot.polling()
