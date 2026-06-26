from EvaluadorFunciones import EvaluadorFunciones


class OrdenSuperior(EvaluadorFunciones):

    def calcular(self) -> list:

        h = self.h
        x0 = self.x0

        # ===================================================
        # EVALUACIÓN DE NODOS
        # ===================================================

        f0 = self.evaluar(x0)

        # HACIA ADELANTE
        fp1 = self.evaluar(x0 + h)
        fp2 = self.evaluar(x0 + 2*h)
        fp3 = self.evaluar(x0 + 3*h)
        fp4 = self.evaluar(x0 + 4*h)
        fp5 = self.evaluar(x0 + 5*h)

        # HACIA ATRÁS
        fm1 = self.evaluar(x0 - h)
        fm2 = self.evaluar(x0 - 2*h)
        fm3 = self.evaluar(x0 - 3*h)
        fm4 = self.evaluar(x0 - 4*h)
        fm5 = self.evaluar(x0 - 5*h)

        # ===================================================
        # HACIA ADELANTE - 1RA DIFERENCIA
        # ===================================================

        ad1_segunda = (
            fp2 - 2*fp1 + f0
        ) / (h**2)

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
            -2*fp5 + 11*fp4 - 24*fp3 +
            26*fp2 - 14*fp1 + 3*f0
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
            3*f0 - 14*fm1 + 26*fm2 -
            24*fm3 + 11*fm4 - 2*fm5
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
            -fp2 + 16*fp1 - 30*f0 +
            16*fm1 - fm2
        ) / (12*(h**2))

        cen2_tercera = (
            -fp3 + 8*fp2 - 12*fp1 +
            12*fm1 - 8*fm2 + fm3
        ) / (8*(h**3))

        cen2_cuarta = (
            -fp3 + 12*fp2 - 39*fp1 +
            56*f0 - 39*fm1 + 12*fm2 - fm3
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