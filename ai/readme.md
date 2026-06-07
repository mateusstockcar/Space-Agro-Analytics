# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# Space Agro Analytics - Módulo de Inteligência Artificial (Visão Computacional)

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

Este módulo contém o núcleo de inteligência e processamento espacial da plataforma Space Agro Analytics. O foco principal é a aplicação de algoritmos de Visão Computacional em dados orbitais (imagens de satélite) para extrair insights preditivos sobre o agronegócio.

Desenvolvemos um pipeline em Python utilizando Jupyter Notebook para calcular o Índice de Vegetação por Diferença Normalizada (NDVI). O algoritmo processa as bandas de luz infravermelha e vermelha da imagem simulada da lavoura, identificando zonas de estresse hídrico. A visualização gerada (mapa de calor) permite a tomada de decisão preditiva, sinalizando a área exata onde a irrigação deve ser ajustada.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz deste módulo, definem-se:

- **src**: Contém o arquivo `space_agro_cv.ipynb`, o Jupyter Notebook com todo o pipeline de processamento de matrizes e renderização visual do mapa de calor.
- **README.md**: Arquivo guia com a documentação do modelo de IA.


## 📎 Links e Observações

- **Tecnologias Core**: Python, Numpy (cálculo matricial) e Matplotlib (renderização gráfica B2B).
- **Observações Gerais**: QUERO CONCORRER.


## 🔧 Como executar o código

Para validar e executar este módulo, siga os passos abaixo:

**Pré-requisitos:**
- Python 3.10+ instalado.
- VS Code com as extensões de Python e Jupyter instaladas.
- Bibliotecas necessárias: `pip install numpy matplotlib opencv-python ipykernel`

**Passo a passo:**
1. Abra o arquivo `space_agro_cv.ipynb` no VS Code.
2. Certifique-se de que o Kernel do Python está selecionado no canto superior direito.
3. Clique no botão de execução (Play / Run Cell) no bloco de código.
4. O gráfico de mapa de calor NDVI será renderizado logo abaixo da célula.


## 🗃 Histórico de lançamentos

* 0.1.0 - 07/06/2026
    * Criação do pipeline analítico em Jupyter Notebook.
    * Implementação do cálculo computacional de NDVI utilizando matrizes do Numpy.
    * Estilização visual em modo dark para painéis executivos.

---


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
