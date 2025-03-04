from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler
from key import api_key

# Función de inicio /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje con un menú de opciones al iniciar el bot"""
    keyboard = [
        [InlineKeyboardButton("¿Qué es el grooming?", callback_data='grooming_info')],
        [InlineKeyboardButton("¿Cómo prevenir el grooming?", callback_data='prevent_grooming')],
        [InlineKeyboardButton("¿Qué hacer si soy víctima de grooming?", callback_data='victim_help')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bienvenido, elige una opción para saber más sobre grooming:", reply_markup=reply_markup)

# Función para manejar las respuestas de los botones
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja las respuestas de los botones del menú"""
    query = update.callback_query
    await query.answer()  # Necesario para confirmar la interacción

    # Según la opción seleccionada, muestra una pregunta
    if query.data == 'grooming_info':
        await query.edit_message_text(text="El grooming es el proceso mediante el cual un adulto se gana la confianza de un menor para manipularlo y explotarlo sexualmente. ¿Te gustaría saber más sobre cómo prevenirlo?")
    elif query.data == 'prevent_grooming':
        await query.edit_message_text(text="La mejor forma de prevenir el grooming es educar a los niños sobre el peligro de compartir información personal en línea y fomentar el uso seguro de internet. ¿Quieres saber qué hacer si eres víctima?")
    elif query.data == 'victim_help':
        await query.edit_message_text(text="Si eres víctima de grooming, es importante hablar con un adulto de confianza o denunciarlo a las autoridades. ¿Necesitas ayuda para saber cómo hacerlo?")
        
        # También podrías agregar más botones para redirigir a recursos o a más preguntas.

# Función principal
def main() -> None:
    """Función principal para iniciar el bot"""
    application = Application.builder().token("TU_BOT_TOKEN").build()

    # Añadir manejadores de comandos
    application.add_handler(CommandHandler("start", start))

    # Añadir manejador para los botones del menú
    application.add_handler(CallbackQueryHandler(button))

    # Ejecutar el bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
