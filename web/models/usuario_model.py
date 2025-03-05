import psycopg2
from config import DATABASE_URL
from datetime import datetime

class UsuarioModel:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(DATABASE_URL)
            print("✅ Conexión a la base de datos establecida correctamente.")
        except Exception as e:
            print("❌ ERROR conectando a la base de datos:", e)
            self.conn = None

    def obtener_modulos(self):
        """
        Obtiene la lista de módulos de prevención de grooming
        """
        modulos = [
            {
                'id': 1,
                'titulo': 'Grooming: Conceptos Fundamentales',
                'descripcion': 'Comprender el acoso sexual online en profundidad',
                'emoji': '🕵️'
            },
            {
                'id': 2,
                'titulo': 'Psicología del Groomer',
                'descripcion': 'Estrategias de manipulación y control emocional',
                'emoji': '🎭'
            },
            {
                'id': 3,
                'titulo': 'Identificación de Riesgos',
                'descripcion': 'Reconoce señales de peligro en entornos digitales',
                'emoji': '🚨'
            },
            {
                'id': 4,
                'titulo': 'Estrategias de Protección',
                'descripcion': 'Técnicas de prevención y defensa digital',
                'emoji': '🛡️'
            },
            {
                'id': 5,
                'titulo': 'Seguridad en Redes Sociales',
                'descripcion': 'Configuración de privacidad y gestión de contactos',
                'emoji': '📱'
            },
            {
                'id': 6,
                'titulo': 'Marco Legal',
                'descripcion': 'Leyes y consecuencias del grooming',
                'emoji': '⚖️'
            }
        ]
        return modulos

    def obtener_detalle_modulo(self, modulo_id):
        """
        Obtiene los detalles de un módulo específico
        """
        detalles_modulos = {
            1: {
                'id': 1,
                'titulo': 'Grooming: Conceptos Fundamentales',
                'descripcion_detallada': 'Módulo introductorio que profundiza en el concepto de grooming, sus características, formas de manifestación y el impacto psicológico en víctimas.',
                'contenidos': [
                    {'tipo': 'video', 'titulo': 'Introducción al Grooming', 'url': '/recursos/modulo1/intro.mp4'},
                    {'tipo': 'documento', 'titulo': 'Conceptos Clave', 'url': '/recursos/modulo1/conceptos.pdf'}
                ]
            },
            2: {
                'id': 2,
                'titulo': 'Psicología del Groomer',
                'descripcion_detallada': 'Análisis de las estrategias psicológicas utilizadas por groomers para manipular y controlar a sus víctimas.',
                'contenidos': [
                    {'tipo': 'video', 'titulo': 'Perfilamiento Psicológico', 'url': '/recursos/modulo2/psicologia.mp4'},
                    {'tipo': 'infografía', 'titulo': 'Estrategias de Manipulación', 'url': '/recursos/modulo2/estrategias.png'}
                ]
            },
            3: {
                'id': 3,
                'titulo': 'Identificación de Riesgos',
                'descripcion_detallada': 'Reconocimiento de señales de peligro y comportamientos de riesgo en entornos digitales.',
                'contenidos': [
                    {'tipo': 'interactivo', 'titulo': 'Simulador de Riesgos', 'url': '/recursos/modulo3/simulador.html'},
                    {'tipo': 'checklist', 'titulo': 'Señales de Alerta', 'url': '/recursos/modulo3/checklist.pdf'}
                ]
            },
            4: {
                'id': 4,
                'titulo': 'Estrategias de Protección',
                'descripcion_detallada': 'Técnicas y herramientas para prevenir y defenderse del grooming en línea.',
                'contenidos': [
                    {'tipo': 'video', 'titulo': 'Protección Digital', 'url': '/recursos/modulo4/proteccion.mp4'},
                    {'tipo': 'guía', 'titulo': 'Manual de Seguridad', 'url': '/recursos/modulo4/manual.pdf'}
                ]
            },
            5: {
                'id': 5,
                'titulo': 'Seguridad en Redes Sociales',
                'descripcion_detallada': 'Configuración de privacidad y gestión segura de contactos en plataformas digitales.',
                'contenidos': [
                    {'tipo': 'tutorial', 'titulo': 'Configuración de Privacidad', 'url': '/recursos/modulo5/tutorial.mp4'},
                    {'tipo': 'documento', 'titulo': 'Guía de Configuración', 'url': '/recursos/modulo5/guia.pdf'}
                ]
            },
            6: {
                'id': 6,
                'titulo': 'Marco Legal',
                'descripcion_detallada': 'Aspectos legales relacionados con el grooming, legislación y consecuencias.',
                'contenidos': [
                    {'tipo': 'webinar', 'titulo': 'Aspectos Legales', 'url': '/recursos/modulo6/webinar.mp4'},
                    {'tipo': 'documento', 'titulo': 'Legislación Vigente', 'url': '/recursos/modulo6/legislacion.pdf'}
                ]
            }
        }

        return detalles_modulos.get(modulo_id)

    def registrar_progreso_modulo(self, usuario_id, modulo_id, porcentaje):
        """
        Simula el registro de progreso de un módulo
        """
        print(f"✅ Progreso registrado - Usuario: {usuario_id}, Módulo: {modulo_id}, Porcentaje: {porcentaje}%")
        return True

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("🔌 Conexión cerrada correctamente.")