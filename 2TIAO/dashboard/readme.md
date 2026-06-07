# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# Space Agro Analytics - Módulo de Visualização (Dashboard B2B)

## Grupo - Grupo S

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/leno-siqueira-36789544?utm_source=share_via&utm_content=profile&utm_medium=member_ios">Leno Siqueira</a> — RM: 567893  
- <a href="https://www.linkedin.com/in/paulo-benfica-76057a7b">Paulo Benfica</a> — RM: 567648  
- <a href="https://www.linkedin.com/in/federico-villagra-97378838a">Fred Villagra</a> — RM: 567187  
- <a href="https://www.linkedin.com/in/math-penteado-1b4807200/">Mateus Lima</a> — RM: 568518 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/sabrina-otoni-22525519b?utm_source=share_via&utm_content=profile&utm_medium=member_ios/">Sabrina Otoni FIAP</a>

### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca/">André Godoi FIAP</a>


## 📜 Descrição

Este módulo é a camada de apresentação (Front-end) da plataforma Space Agro Analytics. Ele atua como o ponto de convergência de toda a inteligência do sistema, consolidando os dados de telemetria de borda (IoT) e as análises orbitais (Visão Computacional / IA) em uma interface executiva B2B.

Desenvolvido em Python utilizando o framework Streamlit, o dashboard permite que o usuário final (gestor agrícola) visualize em tempo real o status dos sensores em solo e o mapa de calor NDVI gerado a partir das imagens de satélite. O sistema conta com alertas automatizados para facilitar a tomada de decisão rápida frente a anomalias hídricas.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz deste módulo, definem-se:

- **src**: Contém o arquivo `app.py`, script principal responsável pela renderização da interface web, estilização CSS injetada e carregamento dos painéis de dados.
- **README.md**: Documentação técnica referente à execução da interface.


## 📎 Links e Observações

- **Tecnologias Core**: Python e Streamlit.
- **Estilização**: Interface otimizada para visualização em modo Dark, focada em painéis de controle industriais/agrícolas.
- **Observações Gerais**: QUERO CONCORRER.


## 🔧 Como executar o código

Para executar a interface da Prova de Conceito na sua máquina local, siga os passos abaixo:

**Pré-requisitos:**
- Python 3.10+ instalado.
- Biblioteca do Streamlit instalada (`pip install streamlit`).

**Passo a passo:**
1. Abra o terminal na raiz do projeto.
2. Execute o comando: `streamlit run dashboard/app.py`
3. O servidor local será iniciado e o seu navegador padrão abrirá automaticamente a aplicação no endereço genérico `http://localhost:8501`.
4. Para encerrar a execução, pressione `Ctrl + C` no terminal.


## 🗃 Histórico de lançamentos

* 0.1.0 - 07/06/2026
    * Criação da interface web com Streamlit.
    * Integração dos painéis de métricas simuladas (IoT) e plotagem do gráfico gerado pelo modelo NDVI.
    * Injeção de CSS para identidade visual premium e alertas condicionais.

---


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
