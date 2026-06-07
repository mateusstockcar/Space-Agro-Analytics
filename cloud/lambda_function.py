import json
import boto3
import os
from datetime import datetime

# Inicializa o cliente do DynamoDB (Banco de Dados NoSQL da AWS)
# Na POC local, ele atua como um mock estrutural
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'SpaceAgro_Telemetry')

def lambda_handler(event, context):
    """
    Função Serverless acionada automaticamente pelo AWS IoT Core Rule Engine.
    Recebe o payload MQTT do ESP32 e persiste no DynamoDB.
    """
    try:
        # O 'event' traz o JSON disparado pelo ESP32 na borda
        # Exemplo esperado: {"dispositivo": "esp32_solo_01", "umidade_solo": 45.2, "temperatura_celsius": 28.5}
        
        dispositivo_id = event.get('dispositivo', 'unknown_device')
        umidade = event.get('umidade_solo', 0.0)
        temperatura = event.get('temperatura_celsius', 0.0)
        status = event.get('status', 'inativo')
        
        # Gera o timestamp exato do recebimento na nuvem
        timestamp = datetime.utcnow().isoformat()
        
        # Prepara o item para inserção no banco NoSQL
        item = {
            'DeviceID': dispositivo_id,
            'Timestamp': timestamp,
            'Umidade': str(umidade),
            'Temperatura': str(temperatura),
            'Status': status
        }
        
        # Simulação da inserção na tabela (Descomentar em ambiente real AWS)
        # table = dynamodb.Table(table_name)
        # table.put_item(Item=item)
        
        print(f"[SUCESSO] Dados recebidos do Edge {dispositivo_id} e processados na Nuvem.")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Telemetria processada e armazenada com sucesso no DynamoDB!')
        }
        
    except Exception as e:
        print(f"[ERRO] Falha ao processar o payload IoT: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Erro interno no processamento Serverless.')
        }