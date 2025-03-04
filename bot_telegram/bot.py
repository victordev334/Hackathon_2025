import logging
import os
import requests
import json
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
from rol import contenido as system_prompt

# Cargar variables de entorno
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")  # Token del bot de Telegram
API_KEY = os.getenv("API_KEY")  # Clave para la IA de Groq

# Configurar el logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Información de denuncia
DENUNCIA_INFO = (
    "☎️ *Líneas de ayuda en caso de grooming:*\n"
    "📞 *088* - Disponible las 24 horas, todos los días del año.\n"
    "🐦 Twitter: [@CNAC_GN](https://twitter.com/CNAC_GN)\n"
    "📩 Correo: cert-mx@sspc.gob.mx\n"
    "📱 *App:* PF Móvil (disponible en todas las plataformas móviles)."
)

# Función para enviar el menú de preguntas
async def send_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje con un menú de opciones cuando el usuario inicia el bot o envía un mensaje"""
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

# Función para obtener respuesta de la IA usando historial
async def get_ai_response(chat_history: list) -> str:
    """Obtiene una respuesta de la IA usando el historial de conversación"""
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    messages = [{"role": "system", "content": system_prompt}] + chat_history

    data = {
        "model": "gemma2-9b-it",
        "messages": messages,
        "temperature": 0.6,
        "max_tokens": 4096,
        "top_p": 0.95,
        "stream": False
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        ai_response = response_data['choices'][0]['message']['content']

        # Si el usuario aún no ha recibido la información de denuncia, la agregamos
        if "088" not in "".join(msg["content"] for msg in chat_history):
            ai_response += f"\n\n{DENUNCIA_INFO}"

        return ai_response
    else:
        return "Lo siento, no pude obtener una respuesta en este momento."

# Función para manejar mensajes de texto y recordar contexto
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responde a los mensajes de texto con la IA manteniendo contexto"""
    user_message = update.message.text

    # Obtener historial del usuario
    chat_history = context.user_data.get("history", [])
    
    # Agregar el mensaje del usuario al historial
    chat_history.append({"role": "user", "content": user_message})
    
    # Mantener un historial corto (últimos 10 mensajes)
    chat_history = chat_history[-10:]

    # Obtener respuesta de la IA
    ai_response = await get_ai_response(chat_history)

    # Agregar respuesta de la IA al historial
    chat_history.append({"role": "assistant", "content": ai_response})
    context.user_data["history"] = chat_history  # Guardar historial en el contexto

    await update.message.reply_text(ai_response)  # Enviar respuesta

# Función principal para iniciar el bot
def main() -> None:
    """Función principal para iniciar el bot"""
    application = Application.builder().token(API_TOKEN).build()

    # Manejadores de comandos y mensajes
    application.add_handler(CommandHandler("start", send_menu))  # Comando /start
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, send_menu))  # Cuando se une un nuevo miembro
    application.add_handler(CallbackQueryHandler(button))  # Manejador de botones del menú
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))  # Manejador de IA para mensajes de texto

    # Ejecutar el bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# Ejecutar la función principal
if __name__ == "__main__":
    main()
