import pandas as pd


def calculator_compound_interest(
    compounding_frequency, contribucion_mensual, principal, tasa_anual, tiempo
):

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

    return interes_generado, total_final, total_contribuciones, df
