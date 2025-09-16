
import streamlit as st

st.set_page_config(page_title="Formulario Creciendo Juntos", layout="wide")

st.title("Formulario Creciendo Juntos")

# Autenticación básica
st.subheader("Autenticación")
codigo_empleado = st.text_input("Código de empleado")
fecha_nacimiento = st.date_input("Fecha de nacimiento")

if codigo_empleado and fecha_nacimiento:
    st.success("Autenticación exitosa")

    # Sección 1: Datos personales
    st.header("Sección 1: Datos personales")
    nombre = st.text_input("Nombre completo")
    edad = st.number_input("Edad", min_value=0, max_value=100)
    genero = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])

    # Sección 2: Condicional
    st.header("Sección 2: Información adicional")
    participa_programa = st.radio("¿Participa en el programa Creciendo Juntos?", ["Sí", "No"])

    if participa_programa == "Sí":
        frecuencia = st.selectbox("¿Con qué frecuencia participa?", ["Semanal", "Mensual", "Ocasional"])
        beneficios = st.text_area("¿Qué beneficios ha recibido?")

    # Sección 3: Comentarios
    st.header("Sección 3: Comentarios")
    comentarios = st.text_area("¿Desea agregar algún comentario adicional?")

    # Botón de envío
    if st.button("Enviar formulario"):
        st.success("Formulario enviado correctamente.")
else:
    st.warning("Por favor ingrese sus credenciales para continuar.")
