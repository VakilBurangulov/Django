import telebot
import os
import random
from telebot import types

token = '5993234240:AAHEqBrRMds1oP-JcdsYgCrQ24tSW4bdnu4'

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['tag'])
def add_id(message):
        username = str(message.from_user.username) # Записываем в переменую username тег адресанта
        id = str(message.from_user.id) # Записываем в переменую id идентификатор адресанта
        file = open(('tags/'+username+'.txt'), 'w+')
        file.write(id)
        file.close()
        if message.from_user.language_code == 'ru':
            bot.send_message(message.from_user.id, 'Ваш тег записан')
        else:
            bot.send_message(message.from_user.id, 'Your tag is recorded')
@bot.message_handler(commands=['start'])
def send_text(message):
    print(message.from_user.language_code)
    if message.from_user.language_code == 'ru':
        bot.send_message(message.chat.id, 'Привет если ты хочешь отправить валентинку то пожалуйста отправь сюда тег адресата без @ которому хочешь отправить валентинку. Например: Vany_Ivanov\nИли напиши /tag что бы записать свой тег и тебе могли отправлять валентинки')
    else:
        bot.send_message(message.chat.id,'Hi, if you want to send a valentine, then please send here the tag of the recipient without @ to whom you want to send a valentine. For example: Vany_Ivanov\n Or write /tag to write down your tag and they could send you valentines')
@bot.message_handler()
def send_valentin(message):
    folder = './tags'
    file = (message.text+'.txt')
    path = os.path.join(folder, file)
    if os.path.isfile(path):
        file = open(('tags/'+message.text+'.txt'),'r')
        id = file.read()
        val_number = str(random.randint(1, 5))
        val_img = open('img/' + val_number + '.jpg', 'rb')
        markup = types.InlineKeyboardMarkup(row_width=1)
        if message.from_user.language_code == 'ru':
            button1 = types.InlineKeyboardButton('Да', callback_data='Yes')
            button2 = types.InlineKeyboardButton('Нет', callback_data='No')
        else:
            button1 = types.InlineKeyboardButton('Yes', callback_data='Yes')
            button2 = types.InlineKeyboardButton('No', callback_data='No')

        markup.add(button1, button2)

        if message.from_user.language_code == 'ru':
            mes = bot.send_message(message.chat.id, 'Ты хочешь что бы адресат увидел что валентинка пришла от тебя?', reply_markup=markup)
        else:
            mes = bot.send_message(message.chat.id, 'Do you want the recipient to see that the valentine came from you?', reply_markup=markup)

        @bot.callback_query_handler(func=lambda call: True)
        def callback(call):
                if call.message:
                    if call.data == 'Yes':
                        bot.send_message(int(id), text=f'Вам пришла валентинка от {message.from_user.username}')
                        bot.send_photo(int(id), val_img)
                    elif call.data == 'No':
                        bot.send_photo(int(id), val_img)
                    bot.delete_message(chat_id=message.chat.id, message_id=mes.message_id)


                if message.from_user.language_code == 'ru':
                    bot.send_message(message.chat.id, 'Валентинка отправлена')
                else:
                    bot.send_message(message.chat.id, 'The Valentine card has been sent')
        file.close()

    else:
        if message.from_user.language_code == 'ru':
            bot.send_message(message.chat.id, 'Я тебя не понимаю')
        else:
            bot.send_message(message.chat.id, 'I dont understand you')




bot.polling()
