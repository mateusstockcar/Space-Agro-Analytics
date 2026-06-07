# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🎓 Graduação ON em Inteligência Artificial  
## 📚 Repositório Oficial de Projetos e Trabalhos Acadêmicos

---

## 🚀 DESTAQUE ATUAL: Global Solution 2026.1 - Space Agro Analytics

**QUERO CONCORRER**

### 👥 Integrantes da Equipe
* **Mateus Penteado** - RM: 568518
* **Federico Enrique Villagra** - RM: 567187
* **Leno Siqueira** - RM: 567893
* **Paulo Henrique Benfica** - RM: 567648

---

## 🎯 Objetivo

Validar e apresentar uma Prova de Conceito (POC) robusta que demonstre como a inteligência artificial e os dados orbitais podem transformar o agronegócio tradicional em um setor preditivo e de alta precisão, garantindo:

- 📌 Integração de Escalas: Cruzar com precisão dados macro (análise computacional de imagens de satélite) com métricas micro (telemetria de solo via IoT).
- 📌 Arquitetura Serverless de Ponta a Ponta: Validar um pipeline de dados escalável e de baixa latência utilizando serviços gerenciados da AWS.
- 📌 Tomada de Decisão em Tempo Real: Disponibilizar inteligência preditiva por meio de um painel analítico voltado para o mercado B2B.
- 📌 Reprodutibilidade e Rigor Técnico: Assegurar que todo o ecossistema (modelos de IA, firmwares de borda e infraestrutura em nuvem) possa ser replicado através de documentação clara e versionamento limpo.

---

### 🌍 O Projeto
A **Space Agro Analytics** é uma plataforma preditiva focada em integrar a Nova Economia Espacial com o Agronegócio. Nossa prova de conceito (POC) cruza dados macro (imagens orbitais de satélite) com dados micro (sensores no solo) para identificar anomalias climáticas e estresse hídrico.

---

### 📁 Estrutura da Solução (Diretórios)
* `/ai`: Modelos de Visão Computacional para análise de índices de vegetação em imagens orbitais.
* `/cloud`: Infraestrutura AWS (IoT Core, Lambda).
* `/dashboard`: Interface B2B em Streamlit para visualização dos alertas.
* `/iot`: Scripts de telemetria (C/C++) para ESP32 e sensores de umidade.

---

### 🎥 Demonstração Prática (Vídeo)
👉 **[Assistir à Demonstração do SpaceAgro](https://youtu.be/MRSurJx_MxA)**

---

## 🧠 Estrutura Macro do Repositório

```bash
📂 Space-Agro-Analytics
│
├── 📂 ai            # Inteligência Artificial & Visão Computacional
│   ├── 📂 notebooks    # Jupyter Notebooks com o processamento de imagens orbitais
│   └── 📄 readme.md    # Documentação dos modelos (YOLO, índices NDVI e treinamento)
│
├── 📂 cloud         # Infraestrutura em Nuvem & Computação Serverless
│   ├── 📂 lambdas      # Scripts e funções de processamento de dados (AWS Lambda)
│   └── 📄 readme.md    # Desenho da arquitetura AWS (IoT Core, Banco de Dados, APIs)
│
├── 📂 dashboard     # Interface B2B & Visualização Analítica
│   ├── 📄 app.py       # Código-fonte da aplicação (Streamlit/Python)
│   └── 📄 readme.md    # Instruções de implantação e rotas de consumo do painel
│
├── 📂 iot           # Engenharia de Borda (Edge Computing)
│   ├── 📂 firmware     # Códigos em C/C++ para o microcontrolador ESP32
│   └── 📄 readme.md    # Esquema de ligação dos sensores e payload do protocolo MQTT
│
├── 📂 assets        # Identidade visual, diagramas de arquitetura e prints da POC
└── 📄 README.md     # Documentação principal e vitrine do projeto (este arquivo)
```

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
