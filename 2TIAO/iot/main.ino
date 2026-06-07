#include <WiFi.h>
#include <PubSubClient.h>

// ---------------------------------------------------------
// 1. Configurações de Rede (Substitua pelos seus dados)
// ---------------------------------------------------------
const char* ssid = "NOME_DA_SUA_REDE_WIFI";
const char* password = "SENHA_DA_SUA_REDE";

// ---------------------------------------------------------
// 2. Configurações do Broker MQTT (Usando um público para a POC)
// ---------------------------------------------------------
const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;
// Tópico exclusivo para o seu projeto não cruzar com outros
const char* mqtt_topic = "fiap/spaceagro/borda/telemetria_solo";

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Conectando-se a rede: ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado com sucesso!");
  Serial.print("Endereço IP: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop até reconectar ao Broker
  while (!client.connected()) {
    Serial.print("Tentando conexão MQTT...");
    // Gera um ID de cliente único para evitar conflitos
    String clientId = "ESP32_Agro_";
    clientId += String(random(0xffff), HEX);
    
    if (client.connect(clientId.c_str())) {
      Serial.println("Conectado ao Broker MQTT!");
    } else {
      Serial.print("Falha na conexão, rc=");
      Serial.print(client.state());
      Serial.println(" Tentando novamente em 5 segundos...");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // ---------------------------------------------------------
  // 3. Simulação de Leitura de Sensores (Mock Data)
  // ---------------------------------------------------------
  // Em um cenário real, você usaria analogRead(PINO_SENSOR)
  // Simulando umidade do solo entre 30% e 80%
  float umidade_solo = random(300, 800) / 10.0; 
  // Simulando temperatura do solo entre 20°C e 35°C
  float temperatura = random(200, 350) / 10.0;  

  // ---------------------------------------------------------
  // 4. Montagem do Payload (Formato JSON)
  // ---------------------------------------------------------
  char payload[150];
  snprintf(payload, sizeof(payload), 
           "{\"dispositivo\": \"esp32_solo_01\", \"umidade_solo\": %.1f, \"temperatura_celsius\": %.1f, \"status\": \"ativo\"}", 
           umidade_solo, temperatura);

  Serial.print("Publicando dados na nuvem: ");
  Serial.println(payload);

  // Envia a mensagem para o tópico MQTT
  client.publish(mqtt_topic, payload);

  // Aguarda 5 segundos antes de fazer a próxima leitura
  delay(5000);
}