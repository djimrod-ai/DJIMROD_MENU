import streamlit as st

# =============================================================================
# 1. CONFIGURACIÓN DE LA PÁGINA
# =============================================================================
st.set_page_config(
    page_title="Editorial Intelligence Suite",
    page_icon="🏢",
    layout="wide"
)

# Estilos para que el portal sea visualmente atractivo
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 3.5rem;
        font-weight: 900;
        color: #1E3A8A;
        margin-bottom: 10px;
    }
    .sub-title {
        text-align: center;
        font-size: 1.3rem;
        color: #6B7280;
        margin-bottom: 40px;
    }
    .app-card {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# =============================================================================
# 2. CONTENIDO DEL PORTAL
# =============================================================================
st.markdown("<h1 class='main-title'>🏢 Editorial Intelligence Suite</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Ecosistema de herramientas avanzadas para la vigilancia y procesamiento de información</p>", unsafe_allow_html=True)

st.markdown("---")

# Creamos dos columnas para las aplicaciones
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="app-card">
            <h2 style='text-align:center;'>🌐 Hub de Noticias</h2>
            <p style='text-align:center;'>Vigilancia de medios en tiempo real, detección de bulos y análisis de tendencias globales.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # EL TRUCO: st.switch_page cambia la página inmediatamente
    if st.button("Abrir Hub de Noticias 🚀", use_container_width=True):
        st.switch_page("pages/app.py")

with col2:
    st.markdown("""
        <div class="app-card">
            <h2 style='text-align:center;'>🎙️ Transcriptor Pro</h2>
            <p style='text-align:center;'>Conversión de video a texto de alta precisión con modelos Whisper de última generación.</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("Abrir Transcriptor 🚀", use_container_width=True):
        st.switch_page("pages/api.py")

st.markdown("<br><br>", unsafe_allow_html=True)
st.info("💡 También puedes navegar utilizando el menú de la izquierda.")
