"""modulo de importaciones necesarias"""
import telebot
# Conexión del bot
TOKEN = '7038513675:AAHziPGzD83O6ewGvZd4oAaHedbuARWnFs0'  # Token de Telegram
bot = telebot.TeleBot(TOKEN)
# Inicializar el diccionario de estado de conversación
conversation_state = {}
# Lista de canales disponibles
channels = [
    "Sport Apuestas",
    "Apuestas Einstein",
    "DM7 Vip",
    "DM7 Free",
    "The King",
    "Merlwin",
    "Dani Pix",
    "DM7 Tenis",
    "Nemesis"
]
#Manejador para el comando start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """ Manejador para el comando /start """
    bot.reply_to(message, '¡Hola! Soy el primer bot creado para dar respuestas a'
                 ' Sebastian Hernández')
#Manejador para el comando help
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

# Manejador para las pulsaciones de botones
@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    """Manejador para las pulsaciones"""
    option = call.data
    chat_id = call.message.chat.id

    if option == 'opcion1':
        # Si se selecciona la opción 1 (Subir apuesta), muestra el menú de canales
        show_channels_menu(chat_id)
        # Establece el estado de conversación para este usuario
        conversation_state[chat_id] = 'waiting_for_channel'

# Función para mostrar el menú de canales
def show_channels_menu(chat_id):
    """Crea un teclado inline con los canales"""
    keyboard = telebot.types.InlineKeyboardMarkup()
    for channel in channels:
        keyboard.row(telebot.types.InlineKeyboardButton(channel, callback_data=f'canal_{channel}'))
    # Envía el mensaje con el teclado inline
    bot.send_message(chat_id, 'Selecciona un canal:', reply_markup=keyboard)

# Inicia el bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
