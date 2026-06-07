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

# Botão de Sincronização
if st.button("🔄 Sincronizar Dados da Nuvem (AWS IoT Core)"):
    # Umidade varia entre 30% (muito seco) e 60% (saudável)
    st.session_state.umidade = round(random.uniform(30.0, 60.0), 1)
    st.session_state.temperatura = round(random.uniform(27.0, 31.0), 1)
else:
    if 'umidade' not in st.session_state: st.session_state.umidade = 45.2
    if 'temperatura' not in st.session_state: st.session_state.temperatura = 28.5

st.divider()

st.header("📡 Telemetria de Borda em Tempo Real (IoT)")
col1, col2, col3, col4 = st.columns(4)

# Lógica de Risco baseada na umidade lida pelo sensor
risco = "ALTO" if st.session_state.umidade < 40 else "MÉDIO" if st.session_state.umidade < 50 else "BAIXO"

col1.metric(label="Status do Sensor", value="Ativo", delta="Conectado")
col2.metric(label="Umidade do Solo", value=f"{st.session_state.umidade}%", delta="Atualizado", delta_color="off")
col3.metric(label="Temperatura do Solo", value=f"{st.session_state.temperatura} °C", delta="Atualizado", delta_color="off")
col4.metric(label="Risco de Estresse Hídrico", value=risco, delta="Atenção Requerida" if risco == "ALTO" else "Estável", delta_color="inverse" if risco == "ALTO" else "normal")

st.divider()

st.header("🌍 Análise Orbital de Safra (NDVI)")
st.markdown("Cruzamento de dados espaciais (bandas NIR/Red) para detecção de anomalias.")

tamanho = (500, 500)
nir_band = np.random.uniform(0.5, 0.9, tamanho)
red_band = np.random.uniform(0.1, 0.4, tamanho)

# INTEGRAÇÃO IA + IOT: O tamanho da anomalia responde à umidade lida
# Se a umidade cai, o quadrado da anomalia cresce. Se sobe, ele diminui.
fator_estresse = int((65.0 - st.session_state.umidade) * 2.5) 
centro = 250
raio = max(15, fator_estresse) # Garante um tamanho mínimo visual

# Aplica a anomalia na matriz espacial
nir_band[centro-raio:centro+raio, centro-raio:centro+raio] = 0.3
red_band[centro-raio:centro+raio, centro-raio:centro+raio] = 0.6

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

if risco == "ALTO":
    st.error(f"🚨 **ALERTA DO SISTEMA:** Expansão de anomalia hídrica detectada no setor central. Umidade crítica em {st.session_state.umidade}%. Irrigação de emergência recomendada.")
elif risco == "MÉDIO":
    st.warning(f"⚠️ **ATENÇÃO:** Índices hídricos caindo (Umidade em {st.session_state.umidade}%). Manter monitoramento via satélite nas próximas 24h.")
else:
    st.success(f"✅ **SISTEMA ESTÁVEL:** Umidade do solo adequada ({st.session_state.umidade}%). Nenhuma intervenção necessária no momento.")
