from EvaluadorFunciones import EvaluadorFunciones


class Metodo3y5Puntos(EvaluadorFunciones):

    def calcular(self) -> list:

        f_x0 = self.evaluar(self.x0)

        f_x0_mas_h = self.evaluar(self.x0 + self.h)
        f_x0_mas_2h = self.evaluar(self.x0 + 2*self.h)
        f_x0_mas_3h = self.evaluar(self.x0 + 3*self.h)
        f_x0_mas_4h = self.evaluar(self.x0 + 4*self.h)

        # -----------------------------------------
        # 3 PUNTOS
        # -----------------------------------------

        tres_puntos = (
            (-3 * f_x0) +
            (4 * f_x0_mas_h) -
            f_x0_mas_2h
        ) / (2 * self.h)

        # -----------------------------------------
        # 5 PUNTOS
        # -----------------------------------------

        cinco_puntos = (
            (-25 * f_x0) +
            (48 * f_x0_mas_h) -
            (36 * f_x0_mas_2h) +
            (16 * f_x0_mas_3h) -
            (3 * f_x0_mas_4h)
        ) / (12 * self.h)

        return [

            f"Método de 3 puntos: {tres_puntos:.6f}",
            f"Método de 5 puntos: {cinco_puntos:.6f}"
        ]