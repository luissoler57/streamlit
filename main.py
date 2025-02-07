import streamlit as st

from utils import calculator_compound_interest

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


interes_generado, total_final, total_contribuciones, df = calculator_compound_interest(
    compounding_frequency=compounding_frequency,
    contribucion_mensual=contribucion_mensual,
    principal=principal,
    tasa_anual=tasa_anual,
    tiempo=tiempo,
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
