import pandas as pd
import streamlit as st

st.set_page_config(page_title="Use Pygwalker In Streamlit", layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.subheader("Compound Calculator Interest")

    principal = st.number_input(label="Initial Investment", value=1000, min_value=0)
    tasa_anual = st.number_input(
        label="Anual Interest Rate", value=0.01, max_value=0.99
    )
    compounding_frequency = st.number_input(
        label="Number of Times Interest is Compounded", value=1, max_value=365
    )
    contribucion_mensual = st.number_input(
        label="Additional Monthly Contribution", value=0, step=100, min_value=0
    )
    tiempo = st.number_input(label="Number of Years", value=10, min_value=1)

# Determinar la frecuencia de capitalización
periodos_capitalizacion = 12 if compounding_frequency == "monthly" else 1


# Convertir la contribución mensual a contribución por periodo
contribucion_por_periodo = contribucion_mensual * (12 / periodos_capitalizacion)
# Listas para almacenar los montos año por año
years = []
amounts_with_interest = []
amounts_without_interest = []
total_contributions = []

# Calcular el monto año por año
for year in range(int(tiempo) + 1):
    factor = (1 + tasa_anual / periodos_capitalizacion) ** (
        periodos_capitalizacion * year
    )
    monto_capital_inicial = principal * factor
    monto_contribuciones = (
        contribucion_por_periodo
        * ((factor - 1) / (tasa_anual / periodos_capitalizacion))
        if tasa_anual > 0
        else contribucion_por_periodo * periodos_capitalizacion * year
    )

    monto_total = monto_capital_inicial + monto_contribuciones
    contribuciones_totales = principal + contribucion_mensual * 12 * year

    # Guardar los montos en las listas
    years.append(year)
    amounts_with_interest.append(monto_total)
    amounts_without_interest.append(contribuciones_totales)
    total_contributions.append(contribuciones_totales)
    # Calcular el interés generado al final del período
    interes_generado = amounts_with_interest[-1] - total_contributions[-1]
    total_final = amounts_with_interest[-1]
    total_contribuciones = total_contributions[-1]

    # Create a DataFrame for plotting with Streamlit
    df = pd.DataFrame(
        {
            "Year": years,
            "With Interest": amounts_with_interest,
            "Without Interest": amounts_without_interest,
        }
    )

with col2:
    st.subheader("Interest Generated Over Time")

    # Create the plot using Streamlit
    st.line_chart(df.set_index("Year"))

    # Display the financial summary
    st.write("Financial Summary:")
    st.write(f"Total Contributions: ${total_contribuciones:,.2f}")
    st.write(f"Interest Generated: ${interes_generado:,.2f}")
    st.write(f"Final Amount: ${total_final:,.2f}")
