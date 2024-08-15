"""modulo de importaciones necesarias"""
import telebot
# Conexión del bot
TOKEN = '7038513675:AAHziPGzD83O6ewGvZd4oAaHedbuARWnFs0'  # Token de Telegram
bot = telebot.TeleBot(TOKEN)
#manejador para el comando start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """ Manejador para el comando /start """
    bot.reply_to(message, '¡Hola! Soy el primer bot creado para dar respuestas a'
                 ' Sebastian Hernández')
#manejador para el comando help
@bot.message_handler(commands=['help'])
def send_help(message):
    """ Manejador para el comando /help"""
    bot.reply_to(message, '¡Este bot está listo para interactuar con Hernan,'
                 'toda la información está restringida.')

@bot.message_handler(func=lambda message: message.text.lower() == 'hola')
def reply_to_hello(message):
    """Crea un teclado inline con 3 botones en filas independientes"""
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Subir apuesta', callback_data='opcion1'))
    keyboard.row(telebot.types.InlineKeyboardButton('Ver tabla', callback_data='opcion2'))
    keyboard.row(telebot.types.InlineKeyboardButton('Subir respuestas', callback_data='opcion3'))

    # Envía el mensaje con el teclado inline
    bot.send_message(message.chat.id, '¡Hola! ¿Qué opción prefieres?', reply_markup=keyboard)

# Inicia el bot
if __name__ == "__main__":
    bot.polling(none_stop=True)

