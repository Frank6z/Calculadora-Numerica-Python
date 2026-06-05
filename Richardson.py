from EvaluadorFunciones import EvaluadorFunciones


class Richardson(EvaluadorFunciones):

    def __init__(
        self,
        ecuacion_str: str,
        x0: float,
        h: float,
        esquema: str,
        niveles: int
    ):
        super().__init__(ecuacion_str, x0, h)

        self.esquema = esquema
        self.niveles = niveles

    # ==================================================
    # DIFERENCIAS FINITAS BASE
    # ==================================================

    def _aproximacion_base(self, h_actual):

        f0 = self.evaluar(self.x0)

        fp1 = self.evaluar(self.x0 + h_actual)
        fp2 = self.evaluar(self.x0 + 2*h_actual)

        fm1 = self.evaluar(self.x0 - h_actual)
        fm2 = self.evaluar(self.x0 - 2*h_actual)

        if self.esquema == "Adelante (Primera Dif)":
            return (fp1 - f0) / h_actual

        elif self.esquema == "Adelante (Segunda Dif)":
            return (
                -fp2 +
                4*fp1 -
                3*f0
            ) / (2*h_actual)

        elif self.esquema == "Atrás (Primera Dif)":
            return (
                f0 - fm1
            ) / h_actual

        elif self.esquema == "Atrás (Segunda Dif)":
            return (
                3*f0 -
                4*fm1 +
                fm2
            ) / (2*h_actual)

        elif self.esquema == "Central (Primera Dif)":
            return (
                fp1 - fm1
            ) / (2*h_actual)

        elif self.esquema == "Central (Segunda Dif)":
            return (
                -fp2 +
                8*fp1 -
                8*fm1 +
                fm2
            ) / (12*h_actual)

        else:
            raise ValueError(
                "Esquema de diferencias finitas no válido."
            )

    # ==================================================
    # TABLA DE RICHARDSON
    # ==================================================

    def calcular(self):

        n = self.niveles

        tabla = [
            [0.0 for _ in range(n)]
            for _ in range(n)
        ]

        # ------------------------------------------
        # Primera columna D(0,i)
        # ------------------------------------------

        h_actual = self.h

        for i in range(n):

            tabla[i][0] = self._aproximacion_base(
                h_actual
            )

            h_actual = h_actual / 2

        # ------------------------------------------
        # Extrapolación
        # ------------------------------------------

        for j in range(1, n):

            for i in range(n - j):

                tabla[i][j] = (
                    (4**j) * tabla[i+1][j-1]
                    - tabla[i][j-1]
                ) / (
                    (4**j) - 1
                )

        return tabla