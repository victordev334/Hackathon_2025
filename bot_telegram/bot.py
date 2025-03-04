import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from dotenv import load_dotenv
import os

# Cargar el archivo .env
load_dotenv()

# Obtener el token desde el archivo .env
API_TOKEN = os.getenv("API_TOKEN")

# Configurar el logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Función para enviar el menú de preguntas
async def send_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje con un menú de opciones cada vez que alguien inicia el bot o envía un mensaje"""
    keyboard = [
        [InlineKeyboardButton("💡 ¿Qué es el grooming?", callback_data='grooming_info')],
        [InlineKeyboardButton("🛡️ ¿Cómo prevenirlo?", callback_data='prevent_grooming')],
        [InlineKeyboardButton("🚨 ¿Qué hacer si soy víctima?", callback_data='victim_help')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 ¡Hola! Estoy aquí para ayudarte a entender más sobre el grooming. Elige una opción para obtener información 👇",
        reply_markup=reply_markup
    )

# Función para manejar las respuestas de los botones sin borrar el menú
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde a los botones sin borrar el menú"""
    query = update.callback_query
    await query.answer()  # Confirmar la interacción con el botón

    respuestas = {
        'grooming_info': "📌 *El grooming* es cuando un adulto se gana la confianza de un menor en internet con malas intenciones. Es importante reconocerlo y saber cómo actuar. 🚨",
        'prevent_grooming': "🔐 *Para prevenir el grooming*, evita compartir información personal con desconocidos y mantén la privacidad en redes sociales. Si algo te incomoda, ¡habla con alguien de confianza! 🛡️",
        'victim_help': "🚔 *Si eres víctima de grooming*, guarda pruebas y busca ayuda de un adulto de confianza o denuncia a las autoridades. No estás solo. ❤️"
    }

    # Enviar un nuevo mensaje con la respuesta sin borrar el menú anterior
    await query.message.reply_text(respuestas.get(query.data, "⚠️ Opción no válida"))

# Función principal
def main() -> None:
    """Función principal para iniciar el bot"""
    application = Application.builder().token(API_TOKEN).build()

    # Manejadores de comandos y mensajes
    application.add_handler(CommandHandler("start", send_menu))  # /start sigue funcionando
    application.add_handler(MessageHandler(filters.TEXT | filters.StatusUpdate.NEW_CHAT_MEMBERS, send_menu))  # Detecta cualquier mensaje o nuevos miembros

    # Añadir manejador para los botones del menú
    application.add_handler(CallbackQueryHandler(button))

    # Ejecutar el bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
