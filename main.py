import telebot
import os
import qrcode


bot = telebot.TeleBot(os.environ.get("TOKEN", "Your_TOKEN"), parse_mode=None)


START_TEXT = """
Hi, I can generate QR code for your text! Just send "/QR {text to QRize}" and wait me for sending generated QR code. 
"""
SUCCESS_TEXT = """
Here is your QR code, enjoy or generate another!
"""
ERROR_TEXT = """
Whoops, something bad happened... We will fire existing devs.
"""


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, START_TEXT)


@bot.message_handler(commands=['QR', 'qr'])
def handle_QR(message):
    try:
        text_to_qrize = ' '.join(message.text.split(" ")[1:])
        qrcode.make(text_to_qrize).save("image.png")
        bot.send_photo(message.chat.id, open("image.png", "rb").read())
        bot.send_message(message.chat.id, SUCCESS_TEXT)
    except Exception as _:
        bot.send_message(message.chat.id, ERROR_TEXT)


if __name__ == '__main__':
    bot.infinity_polling()
