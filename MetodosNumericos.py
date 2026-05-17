# MetodosNumericos.py
import sympy as sp

class EvaluadorDerivadas:
    def __init__(self, expresion_str: str):
        """
        Transforma la expresión de texto de la calculadora a un formato compatible 
        con análisis simbólico y matemático en Python.
        """
        # Reemplazos de formato de la calculadora a sintaxis pura de Python/SymPy
        formato_python = (expresion_str.replace("^", "**")
                                        .replace("ln", "log") # SymPy usa 'log' como logaritmo natural
                                        .replace("log10", "log") # Ajustamos para base 10 abajo si se requiere
                                        .lower())
        
        self.x = sp.Symbol('x')
        try:
            # Si el usuario usó log10 de la UI, lo convertimos al objeto simbólico correcto de SymPy
            if "log10(" in expresion_str:
                formato_python = formato_python.replace("log(", "sp.log(") # parche preventivo
            
            self.expr = sp.sympify(formato_python)
            # Compilación a NumPy para evaluaciones ultra rápidas en punto flotante
            self.f_lambda = sp.lambdify(self.x, self.expr, "numpy")
        except Exception:
            self.f_lambda = None

    def evaluar(self, val_x: float) -> float:
        """Evalúa numéricamente la función en un punto x dado."""
        if self.f_lambda is None:
            raise ValueError("Expresión matemática vacía o inválida.")
        return float(self.f_lambda(val_x))

    def calcular(self, metodo: str, x: float, h: float) -> dict:
        """
        Ejecuta el esquema de diferenciación numérica seleccionado 
        y retorna un diccionario con los nombres de las métricas y sus valores.
        """
        f = self.evaluar

        if metodo == "1. Diferencias finitas":
            return {
                "Diferencia Progresiva (Adelante)": (f(x + h) - f(x)) / h,
                "Diferencia Regresiva (Atrás)": (f(x) - f(x - h)) / h,
                "Diferencia Central": (f(x + h) - f(x - h)) / (2 * h)
            }

        elif metodo == "2. Metodo de 3 y 5 puntos":
            return {
                "3 Puntos (Extremo Progresivo)": (-3*f(x) + 4*f(x + h) - f(x + 2*h)) / (2 * h),
                "3 Puntos (Central)": (f(x + h) - f(x - h)) / (2 * h),
                "5 Puntos (Central)": (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12 * h)
            }

        elif metodo == "3. Derivada de orden superior":
            return {
                "Segunda Derivada (f'')": (f(x + h) - 2*f(x) + f(x - h)) / (h**2),
                "Tercera Derivada (f''')": (f(x + 2*h) - 2*f(x + h) + 2*f(x - h) - f(x - 2*h)) / (2 * h**3)
            }
        
        return {}