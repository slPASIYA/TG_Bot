import os
import telebot

bot = telebot.TeleBot("API Key Here")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello I'm CT bot")
    
@bot.message_handler(commands=["whatsapp"])
def send_message(message):
    bot.send_message(message, "https://wa.me/94772582943")   

bot.polling()