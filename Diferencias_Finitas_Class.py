from EvaluadorFunciones import EvaluadorFunciones


class DiferenciasFinitas(EvaluadorFunciones):

    def calcular(self) -> list:

        f_x0 = self.evaluar(self.x0)

        f_x0_mas_h = self.evaluar(self.x0 + self.h)
        f_x0_mas_2h = self.evaluar(self.x0 + (2 * self.h))

        f_x0_menos_h = self.evaluar(self.x0 - self.h)
        f_x0_menos_2h = self.evaluar(self.x0 - (2 * self.h))

        # -----------------------------------------
        # DIFERENCIAS
        # -----------------------------------------

        adelante_1 = (
            f_x0_mas_h - f_x0
        ) / self.h

        adelante_2 = (
            -f_x0_mas_2h +
            (4 * f_x0_mas_h) -
            (3 * f_x0)
        ) / (2 * self.h)

        atras_1 = (
            f_x0 - f_x0_menos_h
        ) / self.h

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

        return [

            f"Adelante (1ra diferencia): {adelante_1:.6f}",
            f"Adelante (2da diferencia): {adelante_2:.6f}",

            f"Atrás (1ra diferencia): {atras_1:.6f}",
            f"Atrás (2da diferencia): {atras_2:.6f}",

            f"Central (1ra diferencia): {central_1:.6f}",
            f"Central (2da diferencia): {central_2:.6f}"
        ]