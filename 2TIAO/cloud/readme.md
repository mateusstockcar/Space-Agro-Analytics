# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="../../../assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# Space Agro Analytics - Módulo Cloud (Serverless & IoT Core)

## Grupo [Nome do seu Grupo]

## 👨‍🎓 Integrantes: 
- <a href="#">Mateus Penteado</a>
- <a href="#">[Nome do integrante 2]</a>
- <a href="#">[Nome do integrante 3]</a> 
- <a href="#">[Nome do integrante 4]</a> 
- <a href="#">[Nome do integrante 5]</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="#">[Nome do Tutor]</a>
### Coordenador(a)
- <a href="#">[Nome do Coordenador]</a>


## 📜 Descrição

Este módulo representa a arquitetura de Nuvem (Cloud Computing) da plataforma Space Agro Analytics. Ele atua como o middleware escalável que conecta a geração de dados físicos na borda (Edge/IoT) ao banco de dados que alimenta nosso painel preditivo.

Adotamos uma arquitetura 100% Serverless utilizando serviços gerenciados da AWS. A prova de conceito demonstra a estruturação de uma AWS Lambda em Python. Na esteira de produção, o AWS IoT Core recebe as mensagens MQTT enviadas pelo ESP32 e, através de uma IoT Rule, aciona esta função Lambda que trata o payload JSON e o persiste em uma tabela NoSQL do Amazon DynamoDB, garantindo alta disponibilidade e baixa latência.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz deste módulo, definem-se:

- **src**: Contém o script `lambda_function.py`, que encapsula a lógica de processamento em nuvem utilizando a biblioteca `boto3`.
- **README.md**: Documentação arquitetural e técnica da infraestrutura em nuvem.


## 📎 Links e Observações

- **Tecnologias Core**: AWS IoT Core, AWS Lambda, Amazon DynamoDB e Python (`boto3`).
- **Arquitetura**: Event-Driven Serverless.
- **Observações Gerais**: QUERO CONCORRER.


## 🔧 Como executar o código

Por se tratar de um código Serverless projetado para execução em ambiente gerenciado AWS, este script não possui execução local autônoma padrão (sem frameworks como o AWS SAM). 

**Para validação estrutural do código:**
1. O script `lambda_function.py` pode ser revisado quanto à sintaxe e integração com o SDK `boto3`.
2. Em um ambiente real AWS, este código seria colado na interface do serviço AWS Lambda, configurando o gatilho (Trigger) para uma Regra do AWS IoT Core.


## 🗃 Histórico de lançamentos

* 0.1.0 - 07/06/2026
    * Criação do handler da AWS Lambda.
    * Implementação de extração de payload JSON e formatação de timestamp.
    * Estruturação do objeto de inserção para o Amazon DynamoDB.

---


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>