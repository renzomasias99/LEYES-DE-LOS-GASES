import streamlit as st
st.imagen("imagen2.jpg")
st.set_page_config(page_title="Leyes de los Gases", layout="centered")
st.title("🌡️ Calculadora Interactiva - Leyes de los Gases")

st.markdown("""
Selecciona una ley para calcular una variable desconocida.  
Unidades sugeridas:
- **Presión**: atm  
- **Volumen**: litros (L)  
- **Temperatura**: kelvin (K)
""")

ley = st.selectbox("📘 Selecciona una Ley", ["Ley de Boyle", "Ley de Charles", "Ley de Gay-Lussac"])

# Funciones de cálculo
def calcular_boyle(variable, P1=None, V1=None, P2=None, V2=None):
    if variable == "P1":
        return (P2 * V2) / V1
    elif variable == "V1":
        return (P2 * V2) / P1
    elif variable == "P2":
        return (P1 * V1) / V2
    elif variable == "V2":
        return (P1 * V1) / P2

def calcular_charles(variable, V1=None, T1=None, V2=None, T2=None):
    if variable == "V1":
        return (V2 * T1) / T2
    elif variable == "T1":
        return (T2 * V1) / V2
    elif variable == "V2":
        return (V1 * T2) / T1
    elif variable == "T2":
        return (T1 * V2) / V1

def calcular_gay_lussac(variable, P1=None, T1=None, P2=None, T2=None):
    if variable == "P1":
        return (P2 * T1) / T2
    elif variable == "T1":
        return (T2 * P1) / P2
    elif variable == "P2":
        return (P1 * T2) / T1
    elif variable == "T2":
        return (T1 * P2) / P1

# Mostrar inputs dinámicos
if ley == "Ley de Boyle":
    st.subheader("📘 Ley de Boyle: P₁ × V₁ = P₂ × V₂")
    variable = st.selectbox("¿Qué variable deseas calcular?", ["P1", "V1", "P2", "V2"])
    datos = {}
    for var in ["P1", "V1", "P2", "V2"]:
        if var != variable:
            datos[var] = st.number_input(f"Ingresar {var}", min_value=0.001)
    if st.button("Calcular"):
        resultado = calcular_boyle(variable, **datos)
        st.success(f"✅ {variable} = {resultado:.3f}")

elif ley == "Ley de Charles":
    st.subheader("📘 Ley de Charles: V₁ / T₁ = V₂ / T₂")
    variable = st.selectbox("¿Qué variable deseas calcular?", ["V1", "T1", "V2", "T2"])
    datos = {}
    for var in ["V1", "T1", "V2", "T2"]:
        if var != variable:
            datos[var] = st.number_input(f"Ingresar {var}", min_value=0.001)
    if st.button("Calcular"):
        resultado = calcular_charles(variable, **datos)
        st.success(f"✅ {variable} = {resultado:.3f}")

elif ley == "Ley de Gay-Lussac":
    st.subheader("📘 Ley de Gay-Lussac: P₁ / T₁ = P₂ / T₂")
    variable = st.selectbox("¿Qué variable deseas calcular?", ["P1", "T1", "P2", "T2"])
    datos = {}
    for var in ["P1", "T1", "P2", "T2"]:
        if var != variable:
            datos[var] = st.number_input(f"Ingresar {var}", min_value=0.001)
    if st.button("Calcular"):
        resultado = calcular_gay_lussac(variable, **datos)
        st.success(f"✅ {variable} = {resultado:.3f}")
