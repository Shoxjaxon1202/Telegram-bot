from telebot import TeleBot,types
bot = TeleBot("7778364023:AAFnSWAZUqj9TxOEG306tQuFF1GdDeFhaN0")
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Image",callback_data="img")
    button2 = types.InlineKeyboardButton("Video",callback_data="vid")
    button3 = types.InlineKeyboardButton("Gif",callback_data="g")

    markup.add(button1,button2,button3)

    bot.send_message(message.chat.id, "Buttonlardan birini tanlang", reply_markup=markup)
    
@bot.callback_query_handler(func=lambda callback: True)
def nimadir(call):
    if call.data == "img":
        rasm1 = open("Images/robotics-26.webp","rb")
        bot.send_photo(call.message.chat.id,rasm1)
    elif call.data == "vid":
        video1 = open("Images/venom.mp4","rb")
        bot.send_video(call.message.chat.id, video1)

print("Dastur ishga tushdi")
bot.infinity_polling()