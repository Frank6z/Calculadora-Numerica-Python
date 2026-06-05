import streamlit as st
from CalculadoraUI import MecanismoCalculadora
from Diferencias_Finitas_Class import DiferenciasFinitas
from Metodo3y5Puntos import Metodo3y5Puntos
from OrdenSuperior import OrdenSuperior
from Richardson import Richardson
import pandas as pd

st.set_page_config(page_title="Zen Calc - Análisis Numérico", layout="wide")

if "calc" not in st.session_state:
    st.session_state.calc = MecanismoCalculadora()

calc = st.session_state.calc

st.title("Calculadora de Diferenciación Numérica")

# Dividimos la pantalla en dos columnas principales
# Columna 1: Panel de la Calculadora / Columna 2: Parámetros del Método Numérico
col_calculadora, col_metodos = st.columns([1.2, 1])

with col_calculadora:
    st.subheader("Entrada de la Función $f(x)$")
    
    # --- PANTALLA DE LA CALCULADORA (El Label) ---
    st.markdown(
        f"""
        <div style="
            background-color: #1e1e24; 
            padding: 20px; 
            border-radius: 10px; 
            text-align: right; 
            font-size: 2rem; 
            color: #00ffcc;
            font-family: monospace;
            margin-bottom: 20px;
            box-shadow: inset 0px 0px 10px rgba(0,0,0,0.5);
        ">
            {calc.obtener_expresion()}
        </div>
        """, 
        unsafe_allow_html=True
    )

    # --- BOTONERA SUPERIOR (CLEAR largo y Borrar) ---
    col_c1, col_c2 = st.columns([3, 1])

    with col_c1:
        if st.button("CLEAR", use_container_width=True, type="secondary"):
            calc.limpiar()
            st.rerun()

    with col_c2:
        if st.button("⌫", use_container_width=True):
            calc.borrar_ultimo()
            st.rerun()

    # --- NUEVA FILA: CONSTANTES Y PARÉNTESIS ---
    const_col1, const_col2, const_col3, const_col4 = st.columns(4)

    with const_col1:
        if st.button("π", use_container_width=True, type="secondary"):
            calc.agregar_caracter("pi")
            st.rerun()

    with const_col2:
        if st.button("e", use_container_width=True, type="secondary"):
            calc.agregar_caracter("e")
            st.rerun()

    with const_col3:
        if st.button("(", use_container_width=True):
            calc.agregar_caracter("(")
            st.rerun()

    with const_col4:
        if st.button(")", use_container_width=True):
            calc.agregar_caracter(")")
            st.rerun()

    # Funciones Avanzadas
    f_col1, f_col2, f_col3, f_col4 = st.columns(4)

    with f_col1:
        if st.button("√x", use_container_width=True):
            calc.agregar_funcion("sqrt")
            st.rerun()

        if st.button("sin", use_container_width=True):
            calc.agregar_funcion("sin")
            st.rerun()

        if st.button("asin", use_container_width=True):
            calc.agregar_funcion("asin")
            st.rerun()

    with f_col2:
        if st.button("1/x", use_container_width=True):
            calc.agregar_funcion("frac")
            st.rerun()

        if st.button("cos", use_container_width=True):
            calc.agregar_funcion("cos")
            st.rerun()

        if st.button("acos", use_container_width=True):
            calc.agregar_funcion("acos")
            st.rerun()

    with f_col3:
        if st.button("log₁₀", use_container_width=True):
            calc.agregar_funcion("log")
            st.rerun()

        if st.button("tan", use_container_width=True):
            calc.agregar_funcion("tan")
            st.rerun()

        if st.button("atan", use_container_width=True):
            calc.agregar_funcion("atan")
            st.rerun()

    with f_col4:
        if st.button("ln", use_container_width=True):
            calc.agregar_funcion("ln")
            st.rerun()

        # Ahora en lugar de agregar "exp(", escribe directamente la base "e^"
        if st.button("eˣ", use_container_width=True):
            calc.agregar_caracter("e^")
            st.rerun()

        if st.button("^", use_container_width=True):
            calc.agregar_caracter("^")
            st.rerun()

    # Teclado Numérico, Operadores y Variable X
    num_col1, num_col2, num_col3, num_col4 = st.columns(4)

    with num_col1:
        if st.button("7", use_container_width=True):
            calc.agregar_caracter("7")
            st.rerun()

        if st.button("4", use_container_width=True):
            calc.agregar_caracter("4")
            st.rerun()

        if st.button("1", use_container_width=True):
            calc.agregar_caracter("1")
            st.rerun()

        if st.button("0", use_container_width=True):
            calc.agregar_caracter("0")
            st.rerun()

    with num_col2:
        if st.button("8", use_container_width=True):
            calc.agregar_caracter("8")
            st.rerun()

        if st.button("5", use_container_width=True):
            calc.agregar_caracter("5")
            st.rerun()

        if st.button("2", use_container_width=True):
            calc.agregar_caracter("2")
            st.rerun()

        if st.button(".", use_container_width=True):
            calc.agregar_caracter(".")
            st.rerun()

    with num_col3:
        if st.button("9", use_container_width=True):
            calc.agregar_caracter("9")
            st.rerun()

        if st.button("6", use_container_width=True):
            calc.agregar_caracter("6")
            st.rerun()

        if st.button("3", use_container_width=True):
            calc.agregar_caracter("3")
            st.rerun()

        if st.button("X", use_container_width=True, type="primary"):
            calc.agregar_caracter("x")
            st.rerun()

    with num_col4:
        if st.button("/", use_container_width=True):
            calc.agregar_caracter("/")
            st.rerun()

        if st.button("*", use_container_width=True):
            calc.agregar_caracter("*")
            st.rerun()

        if st.button("-", use_container_width=True):
            calc.agregar_caracter("-")
            st.rerun()

        if st.button("+", use_container_width=True):
            calc.agregar_caracter("+")
            st.rerun()

with col_metodos:
    st.subheader("Configuración del Método")

    # Inputs numéricos para los parámetros de análisis numérico
    h_value = st.number_input(
        "Tamaño de paso (H)",
        value=0.1,
        step=0.01,
        format="%.2f"
    )

    x_value = st.number_input(
        "Punto a evaluar (X)",
        value=0.0,
        step=0.1,
        format="%.2f"
    )

    # Lista de selección con los 3 casos solicitados
    casos_diferenciacion = [
        "1. Diferencias finitas",
        "2. Metodo de 3 y 5 puntos",
        "3. Derivada de orden superior",
        "4. Extrapolación de Richardson"
    ]

    metodo_seleccionado = st.selectbox(
    "Selecciona el esquema de diferenciación:",
    casos_diferenciacion
    )

    # --------------------------------------------------
    # CONTROLES DE RICHARDSON
    # --------------------------------------------------

    if metodo_seleccionado == "4. Extrapolación de Richardson":

        esquema_richardson = st.selectbox(
            "Esquema base",
            [
                "Adelante (Primera Dif)",
                "Adelante (Segunda Dif)",
                "Atrás (Primera Dif)",
                "Atrás (Segunda Dif)",
                "Central (Primera Dif)",
                "Central (Segunda Dif)"
            ],
            key = "richardson_esquema"
        )

        niveles_richardson = st.number_input(
            "Número de niveles (n)",
            min_value=2,
            max_value=10,
            value=4,
            step=1,
            key = "richardson_niveles"
        )

    st.write("---")

    # Botón para ejecutar la operación analítica
    if st.button("Calcular Diferenciación", use_container_width=True, type="primary"):

        st.info(
            f"Evaluando f(x) = {calc.obtener_expresion()} en X = {x_value} con H = {h_value}"
        )

        # -------------------------------------------------------
        # 1. DIFERENCIAS FINITAS
        # -------------------------------------------------------

        if metodo_seleccionado == "1. Diferencias finitas":

            try:
                # 1. Recuperamos la ecuación en string de nuestra calculadora
                string_ecuacion = calc.obtener_expresion()

                # 2. Instanciamos la clase matemática
                solucionador = DiferenciasFinitas(
                    string_ecuacion,
                    x_value,
                    h_value
                )

                # 3. Obtenemos el array de strings con los resultados
                lista_resultados = solucionador.calcular()

                # 4. Mostramos SOLO diferencias finitas clásicas
                st.write("Resultados de Diferencias Finitas:")

                for res in lista_resultados[:6]:
                    st.success(res)

            except Exception as err:
                st.error(f"❌ {err}")

        # -------------------------------------------------------
        # 2. MÉTODO DE 3 Y 5 PUNTOS
        # -------------------------------------------------------

        elif metodo_seleccionado == "2. Metodo de 3 y 5 puntos":

            try:
                # Recuperamos la ecuación
                string_ecuacion = calc.obtener_expresion()

                # Instanciamos la clase
                solucionador = Metodo3y5Puntos(
                    string_ecuacion,
                    x_value,
                    h_value
                )

                lista_resultados = solucionador.calcular()

                # Mostramos solamente 3 y 5 puntos
                st.write("Resultados del Método de 3 y 5 puntos:")

                for res in lista_resultados:
                    st.success(res)

            except Exception as err:
                st.error(f"❌ {err}")

        # -------------------------------------------------------
        # 3. DERIVADAS DE ORDEN SUPERIOR
        # -------------------------------------------------------

        elif metodo_seleccionado == "3. Derivada de orden superior":

            try:

                # Recuperamos la ecuación
                string_ecuacion = calc.obtener_expresion()

                # Instanciamos la clase matemática
                solucionador = OrdenSuperior(
                    string_ecuacion,
                    x_value,
                    h_value
                )

                lista_resultados = solucionador.calcular()

                # ---------------------------------------------------
                # VISUALIZACIÓN
                # ---------------------------------------------------

                st.write("Resultados de Derivadas de Orden Superior:")

                for res in lista_resultados:

                    # Títulos de sección
                    if "HACIA" in res or "CENTRADAS" in res:
                        st.markdown(f"### {res}")

                    # Resultados numéricos
                    else:
                        st.success(res)

            except Exception as err:
                st.error(f"❌ {err}")

        

                # -------------------------------------------------------
        # 4. EXTRAPOLACIÓN DE RICHARDSON
        # -------------------------------------------------------

        elif metodo_seleccionado == "4. Extrapolación de Richardson":

            try:

                string_ecuacion = calc.obtener_expresion()

                solucionador = Richardson(
                    string_ecuacion,
                    x_value,
                    h_value,
                    esquema_richardson,
                    niveles_richardson
                )

                tabla = solucionador.calcular()

                st.write("Tabla de Extrapolación de Richardson")

                columnas = [
                    f"D{i}"
                    for i in range(niveles_richardson)
                ]

                tabla_visual = []

                for fila in tabla:

                    nueva_fila = []

                    for valor in fila:

                        if valor == 0:
                            nueva_fila.append("")
                        else:
                            nueva_fila.append(
                                round(valor, 10)
                            )

                    tabla_visual.append(nueva_fila)

                df = pd.DataFrame(
                    tabla_visual,
                    columns=columnas
                )

                st.dataframe(
                    df,
                    use_container_width=True
                )

                st.success(
                    f"Resultado Richardson = "
                    f"{tabla[0][niveles_richardson - 1]:.10f}"
                )

            except Exception as err:
                st.error(f"❌ {err}")    