from telebot import types
import telebot

token = '5993234240:AAHEqBrRMds1oP-JcdsYgCrQ24tSW4bdnu4'

bot = telebot.TeleBot(token)
#
#
# @bot.message_handler(types = ['message'])
# def send_text(message):
#     if message.from_user.language_code == 'ru':
#         bot.send_message(message.chat.id, 'Привет, человек')
#     elif message.from_user.language_code == 'en':
#         bot.send_message(message.chat.id, 'Hello, man')
#     print(message)
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     welcome = 'Привет я Олег вот что я умею\n/start - показать это окно\n/poem - я раскажу тебе стих\n/cat - отправлю тебе кота\n/sticker - отправлю тебе стикер'
#
#     bot.send_message(message.chat.id, welcome)
#
#
#
# @bot.message_handler(commands=['poem'])
# def send_welcome(message):
#     poem = "Муха села на варенье вот и всё стихотворение \U0001F609"
#     bot.send_message(message.chat.id, poem)
#
# @bot.message_handler(commands=['cat'])
# def send_cats(message):
#     cat_number = str(random.randint(1, 9))
#     cat_img = open('img/' + cat_number + '.jpg', 'rb')
#     bot.send_photo(message.chat.id, cat_img)
#
#
# @bot.message_handler(commands=['sticker'])
#
# def send_stickers(message):
#     sticker_number = random.randint(1, 3)
#     if sticker_number == 1:
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI8-GT3b1wHV9J7zWjz0tDWao82E4cfAAKtIAACMvDRS0Zyeew-Gj9_MAQ')
#     elif sticker_number == 2:
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI8-mT3b4p42PoIb_cgZ7DPsEMnn0DrAAKwCAACXAJlA2wMhH4gIzzAMAQ')
#     else:
#         bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAI8_mT3b7RkWgABfXLPP0TZPDe28ChcewAC9CQAAj8mAUlTjd6Q8ZON8TAE')
#
#
#
#     @bot.message_handler()
#     def send_text(message):
#         if message.from_user.language_code == 'ru':
#             bot.send_message(message.chat.id, 'Привет, человек')
#         elif message.from_user.language_code == 'en':
#             bot.send_message(message.chat.id, 'Hello, man')
#         print(message)


@bot.message_handler(commands=['start'])
def button(message):
    print(message)
    markup = types.InlineKeyboardMarkup(row_width=2)
    id = types.InlineKeyboardButton('Узнать свой id в Telegram', callback_data='id')
    language_code = types.InlineKeyboardButton('Узнать свой language_code в Telegram', callback_data='language_code')
    first_name = types.InlineKeyboardButton('Узнать свой first_name в Telegram', callback_data='first_name')
    username = types.InlineKeyboardButton('Узнать свой username в Telegram', callback_data='username')
    last_name = types.InlineKeyboardButton('Узнать свой last_name в Telegram', callback_data='last_name')
    markup.add(id, language_code, first_name, username, last_name)
    bot.send_message(message.chat.id, "Что вам интересно", reply_markup = markup)



@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'id':
            markup = types.InlineKeyboardMarkup(row_width=1)
            text = types.InlineKeyboardButton('Текстом', callback_data='text')
            sticker = types.InlineKeyboardButton('Стикерами', callback_data='sticker')
            markup.add(text, sticker)
            bot.send_message(call.message.chat.id, 'Как вы хотите получить id', reply_markup=markup)
        elif call.data == 'language_code':
            bot.send_message(call.message.chat.id, str(call.from_user.language_code))
        elif call.data == 'first_name':
            bot.send_message(call.message.chat.id, str(call.from_user.first_name))
        elif call.data == 'username':
            bot.send_message(call.message.chat.id, str(call.from_user.username))
        elif call.data == 'last_name':
            bot.send_message(call.message.chat.id, str(call.from_user.last_name))
        elif call.data == 'text':
            bot.send_message(call.message.chat.id, str(call.from_user.id))
        elif call.data == 'sticker':
            for i in str(call.from_user.id):
                if i == '0':
                    bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAJbYWVba1KLETeKssBqEtrgpg8t66OsAALiAAOGCGoCnnoHMfovcNYzBA')
                if i == '1':
                    bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAJbY2Vba4BPSpxsK1w5q22ZG6jPiECJAALkAAOGCGoCqHa5S50SroUzBA')
                if i == '2':
                    bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAJbZWVba_I-KR75K7nWOEiPsjMM04vBAALmAAOGCGoCkyFoU_HFdakzBA')
                if i == '3':
                    bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAJbZ2VbbAvBm4lZsJ2DZSsZOul20PMjAALoAAOGCGoCSitJu9jiAlkzBA')
                if i == '4':
                    bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAJbaWVbbBYwCji8Xa0wnmq7reXzUHa_AALqAAOGCGoC6rQY0i3wJEgzBA')
                if i == '5':
                    bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAJba2VbbCZ5AfEwPxvnfnJgHunDLjRPAALsAAOGCGoCvDplOys4Y8EzBA')
                if i == '6':
                    bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAJbbWVbbDdIugLkILJkKiJjg6h3GGE-AALuAAOGCGoCVyrRTc0CbLQzBA')
                if i == '7':
                    bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAJbb2VbbEaKMFqV0Yf7_SlE6ZVArLWsAALwAAOGCGoCQg0y1NC-_fEzBA')
                if i == '8':
                    bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAJbcWVbbFOq0UxPvMR01NlN8OC42KpUAALyAAOGCGoC0TXQbJa5DR4zBA')
                if i == '9':
                    bot.send_sticker(call.message.chat.id, 'CAACAgQAAxkBAAJbc2VbbF0OPrSy_uMBs4TS9caiWR8nAAL0AAOGCGoCd_QrarVznSczBA')





bot.polling()


