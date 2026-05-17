import math

class MecanismoCalculadora:
    def __init__(self):
        # Aquí guardamos lo que el usuario ve y lo que usaremos después
        self.expresion = ""

    def agregar_caracter(self, caracter: str):
        """Añade números, operadores básicos o constantes a la expresión."""
        self.expresion += str(caracter)

    def agregar_funcion(self, funcion: str):
        """Añade funciones matemáticas abriendo paréntesis para el argumento."""
        funciones_map = {
            "sqrt": "sqrt(",
            "frac": "1/(",
            "log": "log10(",
            "ln": "ln(",
            "exp": "exp(",
            "sin": "sin(",
            "cos": "cos(",
            "tan": "tan(",
            "asin": "asin(",
            "acos": "acos(",
            "atan": "atan("
        }
        if funcion in funciones_map:
            self.expresion += funciones_map[funcion]

    def procesar_teclado(self, tecla: str):
        """Mapea las teclas físicas del teclado, incluyendo x, p (para pi) y e."""
        # Permitimos 'p' y 'e' desde el teclado físico
        if tecla in "0123456789+-*/.()^xpe":
            # Si el usuario presiona 'p' en el teclado físico, guardamos 'pi'
            if tecla == "p":
                self.agregar_caracter("pi")
            else:
                self.agregar_caracter(tecla)
        elif tecla == "Backspace":
            self.borrar_ultimo()
        elif tecla == "Escape":
            self.limpiar()

    def limpiar(self):
        """Borra toda la pantalla."""
        self.expresion = ""

    def borrar_ultimo(self):
        """Borra el último carácter introducido de forma inteligente."""
        # Si lo último es 'pi', borramos ambos caracteres de un solo golpe
        if self.expresion.endswith("pi"):
            self.expresion = self.expresion[:-2]
        else:
            self.expresion = self.expresion[:-1]

    def obtener_expresion(self) -> str:
        """Devuelve la cadena actual para mostrar en el label."""
        return self.expresion if self.expresion != "" else "0"