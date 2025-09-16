
import streamlit as st

st.set_page_config(page_title='Formulario Creciendo Juntos - Prueba Completa', layout='wide')

st.title('Formulario Creciendo Juntos - Versión de Prueba')

# Autenticación
st.subheader('Autenticación')
codigo_empleado = st.text_input('Código de empleado')
fecha_nacimiento = st.date_input('Fecha de nacimiento')

if codigo_empleado and fecha_nacimiento:
    st.success('Autenticación exitosa')

    # Sección 1: Datos personales
    st.header('Sección 1: Datos personales')
    nombre = st.text_input('Nombre completo')
    edad = st.number_input('Edad', min_value=0, max_value=100)
    genero = st.selectbox('Género', ['Masculino', 'Femenino', 'Otro'])
    municipio = st.text_input('Municipio')
    departamento = st.text_input('Departamento')

    # Sección 2: Información familiar
    st.header('Sección 2: Información familiar')
    vive_con_familia = st.radio('¿Vive con su familia?', ['Sí', 'No'])
    cantidad_personas = st.number_input('¿Cuántas personas viven en su hogar?', min_value=0)
    ingreso_mensual = st.number_input('Ingreso mensual aproximado del hogar (USD)', min_value=0)

    # Sección 3: Participación en el programa
    st.header('Sección 3: Participación en el programa')
    participa_programa = st.radio('¿Participa en el programa Creciendo Juntos?', ['Sí', 'No'])
    if participa_programa == 'Sí':
        frecuencia = st.selectbox('¿Con qué frecuencia participa?', ['Semanal', 'Mensual', 'Ocasional'])
        actividades = st.text_area('¿En qué actividades ha participado?')
        beneficios = st.text_area('¿Qué beneficios ha recibido?')

    # Sección 4: Educación
    st.header('Sección 4: Educación')
    nivel_educativo = st.selectbox('Nivel educativo alcanzado', ['Primaria', 'Secundaria', 'Bachillerato', 'Universidad', 'Otro'])
    estudia_actualmente = st.radio('¿Está estudiando actualmente?', ['Sí', 'No'])
    if estudia_actualmente == 'Sí':
        institucion = st.text_input('Nombre de la institución educativa')
        grado = st.text_input('Grado o nivel que cursa')

    # Sección 5: Salud
    st.header('Sección 5: Salud')
    tiene_seguro = st.radio('¿Cuenta con seguro médico?', ['Sí', 'No'])
    enfermedades = st.text_area('¿Padece alguna enfermedad crónica?')
    acceso_salud = st.radio('¿Tiene acceso a servicios de salud?', ['Sí', 'No'])

    # Sección 6: Comentarios finales
    st.header('Sección 6: Comentarios finales')
    comentarios = st.text_area('¿Desea agregar algún comentario adicional?')

    # Botón de envío
    if st.button('Enviar formulario'):
        st.success('Formulario enviado correctamente (versión de prueba).')
else:
    st.warning('Por favor ingrese sus credenciales para continuar.')
