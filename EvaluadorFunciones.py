import re
from math import sin, cos, tan, asin, acos, atan
from math import sqrt, log10, log as ln, pi, e


class EvaluadorFunciones:

    def __init__(self, ecuacion_str: str, x0: float, h: float):

        self.ecuacion_original = ecuacion_str
        self.x0 = x0
        self.h = h

    def evaluar(self, punto: float) -> float:

        ecuacion = self.ecuacion_original

        # -----------------------------------------
        # POTENCIAS
        # -----------------------------------------

        ecuacion_operable = ecuacion.replace("^", "**")

        # -----------------------------------------
        # MULTIPLICACIÓN IMPLÍCITA
        # -----------------------------------------

        ecuacion_operable = re.sub(
            r'(\d)(x)',
            r'\1*\2',
            ecuacion_operable
        )

        ecuacion_operable = re.sub(
            r'\)\(',
            ')*(',
            ecuacion_operable
        )

        ecuacion_operable = re.sub(
            r'x\(',
            'x*(',
            ecuacion_operable
        )

        ecuacion_operable = re.sub(
            r'\)x',
            ')*x',
            ecuacion_operable
        )

        ecuacion_operable = re.sub(
            r'(\))(?=(sin|cos|tan|asin|acos|atan|ln|log10|sqrt))',
            r'\1*',
            ecuacion_operable
        )

        # -----------------------------------------
        # REEMPLAZO DE X
        # -----------------------------------------

        ecuacion_evaluable = ecuacion_operable.replace(
            "x",
            f"({punto})"
        )

        try:

            contexto_matematico = {
                "sin": sin,
                "cos": cos,
                "tan": tan,
                "asin": asin,
                "acos": acos,
                "atan": atan,
                "sqrt": sqrt,
                "log10": log10,
                "ln": ln,
                "pi": pi,
                "e": e
            }

            return eval(
                ecuacion_evaluable,
                {"__builtins__": None},
                contexto_matematico
            )

        except Exception:

            raise ValueError(
                "Error de sintaxis matemática en la expresión."
            )