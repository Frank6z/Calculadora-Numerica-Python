import re
from math import sin, cos, tan, asin, acos, atan, sqrt, log10, log as ln, pi, e

class DiferenciasFinitas:
    def __init__(self, ecuacion_str: str, x0: float, h: float):
        self.ecuacion_original = ecuacion_str
        self.x0 = x0
        self.h = h

    def _evaluar_en(self, punto: float) -> float:
        """
        Método privado para traducir el string y evaluarlo en un punto de forma segura.
        Soporta constantes (e, pi), potencias (**), inversas y multiplicación implícita.
        """

        ecuacion = self.ecuacion_original

        # ---------------------------------------------------
        # POTENCIAS
        # ---------------------------------------------------

        ecuacion_operable = ecuacion.replace("^", "**")

        # ---------------------------------------------------
        # MULTIPLICACIÓN IMPLÍCITA
        # ---------------------------------------------------

        ecuacion_operable = re.sub(r'(\d)(x)', r'\1*\2', ecuacion_operable)
        ecuacion_operable = re.sub(r'\)\(', ')*(', ecuacion_operable)
        ecuacion_operable = re.sub(r'x\(', 'x*(', ecuacion_operable)
        ecuacion_operable = re.sub(r'\)x', ')*x', ecuacion_operable)

        ecuacion_operable = re.sub(
            r'(\))(?=(sin|cos|tan|asin|acos|atan|ln|log10|sqrt))',
            r'\1*',
            ecuacion_operable
        )

        # ---------------------------------------------------
        # REEMPLAZO DE X
        # ---------------------------------------------------

        ecuacion_evaluable = ecuacion_operable.replace("x", f"({punto})")

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
                "Error de sintaxis matemática en la expresión de la calculadora."
            )

    # ===================================================
    # DIFERENCIAS FINITAS + 3 Y 5 PUNTOS
    # ===================================================

    def calcular_todas(self) -> list:

        # ---------------------------------------------------
        # PRE-EVALUACIÓN DE NODOS
        # ---------------------------------------------------

        f_x0 = self._evaluar_en(self.x0)

        # HACIA ADELANTE
        f_x0_mas_h = self._evaluar_en(self.x0 + self.h)
        f_x0_mas_2h = self._evaluar_en(self.x0 + (2 * self.h))
        f_x0_mas_3h = self._evaluar_en(self.x0 + (3 * self.h))
        f_x0_mas_4h = self._evaluar_en(self.x0 + (4 * self.h))

        # HACIA ATRÁS
        f_x0_menos_h = self._evaluar_en(self.x0 - self.h)
        f_x0_menos_2h = self._evaluar_en(self.x0 - (2 * self.h))

        # ---------------------------------------------------
        # DIFERENCIAS FINITAS
        # ---------------------------------------------------

        adelante_1 = (f_x0_mas_h - f_x0) / self.h

        adelante_2 = (
            -f_x0_mas_2h +
            (4 * f_x0_mas_h) -
            (3 * f_x0)
        ) / (2 * self.h)

        atras_1 = (f_x0 - f_x0_menos_h) / self.h

        atras_2 = (
            (3 * f_x0) -
            (4 * f_x0_menos_h) +
            f_x0_menos_2h
        ) / (2 * self.h)

        central_1 = (
            f_x0_mas_h - f_x0_menos_h
        ) / (2 * self.h)

        central_2 = (
            -f_x0_mas_2h +
            (8 * f_x0_mas_h) -
            (8 * f_x0_menos_h) +
            f_x0_menos_2h
        ) / (12 * self.h)

        # ---------------------------------------------------
        # 3 Y 5 PUNTOS
        # ---------------------------------------------------

        tres_puntos = (
            (-3 * f_x0) +
            (4 * f_x0_mas_h) -
            f_x0_mas_2h
        ) / (2 * self.h)

        cinco_puntos = (
            (-25 * f_x0) +
            (48 * f_x0_mas_h) -
            (36 * f_x0_mas_2h) +
            (16 * f_x0_mas_3h) -
            (3 * f_x0_mas_4h)
        ) / (12 * self.h)

        resultados = [
            f"Adelante (1ra diferencia): {adelante_1:.6f}",
            f"Adelante (2da diferencia): {adelante_2:.6f}",
            f"Atrás (1ra diferencia): {atras_1:.6f}",
            f"Atrás (2da diferencia): {atras_2:.6f}",
            f"Central (1ra diferencia): {central_1:.6f}",
            f"Central (2da diferencia): {central_2:.6f}",
            f"Método de 3 puntos: {tres_puntos:.6f}",
            f"Método de 5 puntos: {cinco_puntos:.6f}"
        ]

        return resultados

    # ===================================================
    # DERIVADAS DE ORDEN SUPERIOR
    # ===================================================

    def calcular_orden_superior(self) -> list:

        h = self.h
        x0 = self.x0

        # ---------------------------------------------------
        # EVALUACIÓN DE NODOS
        # ---------------------------------------------------

        f0 = self._evaluar_en(x0)

        fp1 = self._evaluar_en(x0 + h)
        fp2 = self._evaluar_en(x0 + 2*h)
        fp3 = self._evaluar_en(x0 + 3*h)
        fp4 = self._evaluar_en(x0 + 4*h)
        fp5 = self._evaluar_en(x0 + 5*h)

        fm1 = self._evaluar_en(x0 - h)
        fm2 = self._evaluar_en(x0 - 2*h)
        fm3 = self._evaluar_en(x0 - 3*h)
        fm4 = self._evaluar_en(x0 - 4*h)
        fm5 = self._evaluar_en(x0 - 5*h)

        # ===================================================
        # HACIA ADELANTE - 1RA DIFERENCIA
        # ===================================================

        ad1_segunda = (fp2 - 2*fp1 + f0) / (h**2)

        ad1_tercera = (
            f0 - 3*fm1 + 3*fm2 - fm3
        ) / (h**3)

        ad1_cuarta = (
            f0 - 4*fm1 + 6*fm2 - 4*fm3 + fm4
        ) / (h**4)

        # ===================================================
        # HACIA ADELANTE - 2DA DIFERENCIA
        # ===================================================

        ad2_segunda = (
            -fp3 + 4*fp2 - 5*fp1 + 2*f0
        ) / (h**2)

        ad2_tercera = (
            -3*fp4 + 14*fp3 - 24*fp2 + 18*fp1 - 5*f0
        ) / (h**3)

        ad2_cuarta = (
            -2*fp5 + 11*fp4 - 24*fp3 + 26*fp2 - 3*fp1 + f0
        ) / (h**4)

        # ===================================================
        # HACIA ATRÁS - 1RA DIFERENCIA
        # ===================================================

        at1_segunda = (
            f0 - 2*fm1 + fm2
        ) / (h**2)

        at1_tercera = (
            f0 - 3*fm1 + 3*fm2 - fm3
        ) / (h**3)

        at1_cuarta = (
            f0 - 4*fm1 + 6*fm2 - 4*fm3 + fm4
        ) / (h**4)

        # ===================================================
        # HACIA ATRÁS - 2DA DIFERENCIA
        # ===================================================

        at2_segunda = (
            2*f0 - 5*fm1 + 4*fm2 - fm3
        ) / (h**2)

        at2_tercera = (
            5*f0 - 18*fm1 + 24*fm2 - 14*fm3 + 3*fm4
        ) / (h**3)

        at2_cuarta = (
            3*f0 - 14*fm1 + 26*fm2 - 24*fm3 + 11*fm4 - 2*fm5
        ) / (h**4)

        # ===================================================
        # CENTRADAS - 1RA DIFERENCIA
        # ===================================================

        cen1_segunda = (
            fp1 - 2*f0 + fm1
        ) / (h**2)

        cen1_tercera = (
            fp2 - 2*fp1 + 2*fm1 - fm2
        ) / (2*(h**3))

        cen1_cuarta = (
            fp2 - 4*fp1 + 6*f0 - 4*fm1 + fm2
        ) / (h**4)

        # ===================================================
        # CENTRADAS - 2DA DIFERENCIA
        # ===================================================

        cen2_segunda = (
            -fp2 + 16*fp1 - 30*f0 + 16*fm1 - fm2
        ) / (12*(h**2))

        cen2_tercera = (
            -fp3 + 8*fp2 - 2*fp1 + 12*fm1 - 8*fm2 + fm3
        ) / (8*(h**3))

        cen2_cuarta = (
            -fp3 + 12*fp2 - 39*fp1 + 56*f0 - 39*fm1 + 12*fm2 - fm3
        ) / (6*(h**4))

        # ===================================================
        # RESULTADOS
        # ===================================================

        resultados = [

            "HACIA ADELANTE (1ra Diferencia)",
            f"f''(x): {ad1_segunda:.6f}",
            f"f'''(x): {ad1_tercera:.6f}",
            f"f''''(x): {ad1_cuarta:.6f}",

            "HACIA ADELANTE (2da Diferencia)",
            f"f''(x): {ad2_segunda:.6f}",
            f"f'''(x): {ad2_tercera:.6f}",
            f"f''''(x): {ad2_cuarta:.6f}",

            "HACIA ATRÁS (1ra Diferencia)",
            f"f''(x): {at1_segunda:.6f}",
            f"f'''(x): {at1_tercera:.6f}",
            f"f''''(x): {at1_cuarta:.6f}",

            "HACIA ATRÁS (2da Diferencia)",
            f"f''(x): {at2_segunda:.6f}",
            f"f'''(x): {at2_tercera:.6f}",
            f"f''''(x): {at2_cuarta:.6f}",

            "CENTRADAS (1ra Diferencia)",
            f"f''(x): {cen1_segunda:.6f}",
            f"f'''(x): {cen1_tercera:.6f}",
            f"f''''(x): {cen1_cuarta:.6f}",

            "CENTRADAS (2da Diferencia)",
            f"f''(x): {cen2_segunda:.6f}",
            f"f'''(x): {cen2_tercera:.6f}",
            f"f''''(x): {cen2_cuarta:.6f}"
        ]

        return resultados