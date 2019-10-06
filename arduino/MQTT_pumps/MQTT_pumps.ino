#include <WiFi.h>
#include <PubSubClient.h>
 
const char* ssid = "H368N42C130";
const char* password =  "KrijgJeNiet11";
const char* mqttServer = "35.204.110.87";
const int mqttPort = 1883;

// defines pins numbers
const int numPumps = 4;
const int pumpPins[numPumps] = {4, 16, 17, 5};

const char *mqtt_topic[] = {"beker1/pump","beker2/pump","beker3/pump", "beker4/pump"} ;
 
WiFiClient espClient;
PubSubClient client(espClient);
 
void setup() {
 
  Serial.begin(115200);

  for (int i = 0; i <= numPumps; i++){
    pinMode(pumpPins[i], OUTPUT); // Sets the pumpPins as an Output
  }
  
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
 
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
 
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
 
    if (client.connect("ESP32Client" )) {
 
      Serial.println("connected");  
 
    } else {
 
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
 
    }
  }

  for (int i = 0; i <= numPumps; i++){
    client.subscribe(mqtt_topic[i]);
  }
 
}

void callback(char* topic, byte* payload, unsigned int length) {

  payload[length] = '\0';
  String s = String((char*)payload);
  float set_time = s.toFloat();
  
  Serial.println(topic);
  Serial.println(set_time);
  
  if(strcmp(topic,mqtt_topic[0])==0){
    digitalWrite(pumpPins[0], HIGH);
    delay(set_time);
    digitalWrite(pumpPins[0], LOW);
  } 
  
  if (strcmp(topic,mqtt_topic[1])==0){
    digitalWrite(pumpPins[1], HIGH);
    delay(set_time);
    digitalWrite(pumpPins[1], LOW);
  }
  
  if(strcmp(topic,mqtt_topic[2])==0){
    digitalWrite(pumpPins[2], HIGH);
    delay(set_time);
    digitalWrite(pumpPins[2], LOW);
  }
  
  if (strcmp(topic,mqtt_topic[3])==0){
    digitalWrite(pumpPins[3], HIGH);
    delay(set_time);
    digitalWrite(pumpPins[3], LOW);
  }
}

void loop() {
  client.loop();
}
