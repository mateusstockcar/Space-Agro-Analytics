import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Space Agro Analytics", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { background-color: #0E1117; }
    h1 { color: #FFD700; font-weight: 800; }
    h2, h3 { color: #00BFFF; }
    .stMetric label { color: #A0AEC0 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🛰️ Space Agro Analytics")
st.markdown("### Plataforma de Inteligência Espacial e Telemetria de Solo")

# Botão para simular a chegada de novos dados do IoT
if st.button("🔄 Sincronizar Dados da Nuvem (AWS IoT Core)"):
    # Gera pequenas variações para simular leitura em tempo real
    st.session_state.umidade = round(random.uniform(40.0, 48.0), 1)
    st.session_state.temperatura = round(random.uniform(27.0, 31.0), 1)
else:
    # Valores iniciais
    if 'umidade' not in st.session_state: st.session_state.umidade = 45.2
    if 'temperatura' not in st.session_state: st.session_state.temperatura = 28.5

st.divider()

st.header("📡 Telemetria de Borda em Tempo Real (IoT)")
col1, col2, col3, col4 = st.columns(4)

col1.metric(label="Status do Sensor", value="Ativo", delta="Conectado")
col2.metric(label="Umidade do Solo", value=f"{st.session_state.umidade}%", delta="-12.3%", delta_color="inverse")
col3.metric(label="Temperatura do Solo", value=f"{st.session_state.temperatura} °C", delta="+1.2 °C", delta_color="inverse")
col4.metric(label="Risco de Estresse Hídrico", value="ALTO", delta="Atenção Requerida", delta_color="inverse")

st.divider()

st.header("🌍 Análise Orbital de Safra (NDVI)")
st.markdown("Cruzamento de dados espaciais (bandas NIR/Red) para detecção de anomalias.")

tamanho = (500, 500)
nir_band = np.random.uniform(0.5, 0.9, tamanho)
red_band = np.random.uniform(0.1, 0.4, tamanho)

nir_band[200:300, 200:300] = 0.3
red_band[200:300, 200:300] = 0.6

ndvi = (nir_band - red_band) / (nir_band + red_band)

fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor('#0E1117')
ax.set_facecolor('#0E1117')

cax = ax.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
ax.axis('off')

cbar = fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Índice de Vegetação Saudável', color='#00BFFF', fontsize=12)
cbar.ax.tick_params(colors='white')

st.pyplot(fig)

st.error("🚨 **ALERTA DO SISTEMA:** Anomalia hídrica detectada no setor central da lavoura (Coordenadas Espaciais cruzadas com Node IoT 01). Recomendada ativação de irrigação automatizada.")
