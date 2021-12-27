from telegram import Update, ReplyKeyboardMarkup,  ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler


TOKEN = 'TOKEN'


def main():
    updater = Updater(token=TOKEN) # объект, который ловит сообщения от Telegrama

    dispather = updater.dispatcher

    handler = MessageHandler(Filters.all, do_echo)
    start_handler = CommandHandler('start', do_start)
    help_handler = CommandHandler('help', do_help)
    keyboard_handler = MessageHandler(Filters.text, do_something)
    sticker_handler = MessageHandler(Filters.sticker, do_sticker)

    dispather.add_handler(start_handler)
    dispather.add_handler(help_handler)
    dispather.add_handler(keyboard_handler)
    dispather.add_handler(sticker_handler)
    dispather.add_handler(handler)

    updater.start_polling()
    updater.idle()


def do_echo(update, context):

    update.message.reply_text(text='who are you?')

def do_start(update, context):
    keyboard = [
        ['1', 'стикер', '❤️'],
        ['🤘', 'Ты', '7'],
    ]
    update.message.reply_text(
        text='что надо?',
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    )

def do_help(update: Update, context):
    user_id = update.message.from_user.id
    name = update.message.from_user.first_name
    update.message.reply_text(text=f'Привет, {name}!\nТвой user_id: {user_id}\nПомощь на подходе')


def do_something(update: Update, context):
    text = update.message.text
    if text == '1':
        update.message.reply_text('Вы нажали 1', reply_markup=ReplyKeyboardRemove())
    elif text == 'стикер':
        update.message.reply_sticker('CAACAgIAAxkBAAOQYEimPszdjgYmwhYVQ3aa_P-NcfYAAggAA8A2TxNvbCYL3hqbaR4E')
    elif text == '❤️':
        update.message.reply_text('Вы нажали ❤')
    elif text == '🤘':
        update.message.reply_text('Вы нажали 🤘')
    elif text == 'Ты':
        update.message.reply_text('Лох))))))')
    elif text == '7':
        update.message.reply_text('Вы нажали 7')
    else:
        update.message.reply_text('Ты дурак?')


def do_sticker(update: Update, context):
    sticker_id = update.message.sticker.file_id
    update.message.reply_sticker(sticker_id)


main()
