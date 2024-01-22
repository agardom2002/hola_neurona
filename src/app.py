import streamlit as st

st.image("img/neurona_transparente.png", width=300)

# Title
st.title("¡Hola neurona!")

# Títulos de las pestañas
tab_titles = ["Una entrada", "Dos entradas", "Tres entradas y sesgo"]

# Crear pestañas
tab1, tab2, tab3 = st.tabs(tab_titles)

# Contenido en función de la pestaña seleccionada
with tab1:
    # Personalizar el tamaño del contenido de la pestaña 1
    st.markdown("<style>h1 { font-size: 28px; }</style>", unsafe_allow_html=True)
    st.title("Una neurona con una entrada y un peso")
    
    w = st.slider("Peso", step=0.01, value=0.00, max_value=5.0, key="s1")
    x = st.number_input("Introduzca el valor de la entrada", key="n1")

    if st.button('Calcular la salida', key='boton_tab1'):
        st.write(f"La salida de la neurona es {x * w}")

with tab2:
    col1, col2= st.columns(2)

    with col1:
        w0 = st.slider("Peso w0", step=0.01, value=0.00, max_value=5.0, key="s2")
        x0 = st.number_input("Entrada x0", key="n2") 
    
    with col2:
        w1 = st.slider("Peso w1", step=0.01, value=0.00, max_value=5.0, key="s3")
        x1 = st.number_input("Entrada x1", key="n3") 

    if st.button('Calcular la salida', key='boton_tab2'):
        st.write(f"La salida de la neurona es {x0 * w0 + x1 * w1}")

with tab3:
    col1, col2, col3= st.columns(3)

    with col1:
        w0 = st.slider("Peso w0", step=0.01, value=0.00, max_value=5.0, key="s4")
        x0 = st.number_input("Entrada x0", key="n4") 
    
    with col2:
        w1 = st.slider("Peso w1", step=0.01, value=0.00, max_value=5.0, key="s5")
        x1 = st.number_input("Entrada x1", key="n5") 
    
    with col3:
        w2 = st.slider("Peso w2", step=0.01, value=0.00, max_value=5.0, key="s6")
        x2 = st.number_input("Entrada x2", key="n6") 

    b = st.number_input("Introduzca el valor del sesgo", key="n7")

    if st.button('Calcular la salida', key='boton_tab3'):
        st.write(f"La salida de la neurona es {x0 * w0 + x1 * w1 + x2 * w2 + b}")

