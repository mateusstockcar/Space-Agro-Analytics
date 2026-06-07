# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# Space Agro Analytics - Módulo IoT (Telemetria de Solo)

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

Este módulo compõe a infraestrutura de borda (Edge Computing) da plataforma Space Agro Analytics. O objetivo é atuar como o validador físico ("ground truth") para os modelos de Inteligência Artificial que analisam imagens de satélite. 

Para a prova de conceito (POC), desenvolvemos um firmware em C++ para o microcontrolador ESP32. Ele simula a leitura contínua de sensores de umidade do solo e temperatura ambiente. Esses dados são convertidos em um payload estruturado em JSON e transmitidos em tempo real via rede Wi-Fi utilizando o protocolo de mensageria MQTT. O envio contínuo alimenta nosso ecossistema na nuvem, permitindo o cruzamento de dados macro (espaço) com dados micro (solo) para prever anomalias hídricas na agricultura.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz deste módulo, definem-se:

- **src**: Contém o código-fonte (`sketch.ino` / `main.cpp`) desenvolvido em C++ para a placa ESP32, incluindo a lógica de conexão Wi-Fi e roteamento MQTT.
- **README.md**: Arquivo que serve como guia e explicação geral sobre o módulo de hardware.


## 📎 Links e Observações

- **Simulação Oficial (Wokwi)**: [Acessar o circuito virtual rodando em tempo real](https://wokwi.com/projects/466192451980960769)
- **Explicação de decisões técnicas**: Optou-se por utilizar o broker público HiveMQ (`broker.hivemq.com:1883`) pelo tópico `fiap/spaceagro/borda/telemetria_solo` para garantir a facilidade de testes pela banca avaliadora, sem a necessidade de autenticação via certificados TLS nesta etapa da POC.
- **Observações Gerais**: QUERO CONCORRER.


## 🔧 Como executar o código

Para validar e executar este módulo, não é necessário possuir o hardware físico. O ambiente foi virtualizado para facilitar a correção.

**Pré-requisitos:**
- Navegador de internet atualizado.
- Acesso ao link da simulação.

**Passo a passo:**
1. Acesse o link oficial do simulador Wokwi listado acima.
2. Na interface da ferramenta, clique no botão verde de **"Play" (Start the simulation)** localizado no topo da tela.
3. Aguarde a conexão com a rede virtual `Wokwi-GUEST` (o status aparecerá na aba "Serial Monitor" no canto inferior direito).
4. Em seguida, o dispositivo se conectará ao Broker MQTT e começará a disparar os pacotes JSON a cada 5 segundos.
5. Verifique as leituras de umidade e temperatura sendo exibidas no terminal.


## 🗃 Histórico de lançamentos

* 0.1.0 - 07/06/2026
    * Criação do firmware inicial em C++ para ESP32.
    * Implementação da lógica de conexão Wi-Fi e integração com a biblioteca PubSubClient para MQTT.
    * Estruturação do envio de dados simulados (mock) em formato JSON.

---


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
