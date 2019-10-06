/*
* Ultrasonic Sensor HC-SR04 and Arduino Tutorial
*https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/
*For the MQTT client publish
*https://randomnerdtutorials.com/esp32-mqtt-publish-subscribe-arduino-ide/
*/

#include <WiFi.h>
#include <PubSubClient.h>

//Wifi
const char* ssid = "H368N42C130";
const char* wifi_password = "KrijgJeNiet11";

//MQTT
const char* mqtt_server = "35.204.110.87";
const char* mqtt_username = "xvgfmnhm";
const char* mqtt_password = "YD2yAN5wS9_U";
const char* clientID = "ESP32_HCSR04";

// Initialise the WiFi and MQTT Client objects
WiFiClient wifiClient;
PubSubClient client(mqtt_server, 1883, wifiClient);

// defines pins numbers
int trigPins[] = {21, 24, 27, 35};
int echoPins[] = {22, 25, 34, 38};
int num_sensors = 4;    // number of HCSR04 sensors connected
const char *topics[] = {"beker1/stock", "beker2/stock", "beker3/stock", "beker4/stock"};

// defines variables
long duration, cm;

void setup() {
  Serial.begin(115200); // Starts the serial communication

  for (int i = 0; i <= num_sensors; i++){
    pinMode(trigPins[i], OUTPUT); // Sets the trigPin as an Output
    pinMode(echoPins[i], INPUT);  // Sets the echoPin as an Output
  }
  
  setup_wifi();
}

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, wifi_password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect(clientID)) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void calc_distance( int trigPin, int echoPin, const char *topic ) {
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  cm = (duration/2)/29.1;
  // Prints the distance on the Serial Monitor
  Serial.print("Cm: ");
  Serial.println(cm);

  // Convert the value to a char array
  char cmString[8];
  dtostrf(cm, 4, 2, cmString);
  client.publish(topic, cmString);
  
  }

  
void loop() {
  if (!client.connected()) {
    reconnect();
  }
  
  // client.loop() just tells the MQTT client code to do what it needs to do itself (i.e. check for messages, etc.)
  client.loop(); 
  
  for (int i = 0; i <= 3; i++){
    calc_distance( trigPins[i], echoPins[i], topics[i]);
  }
  
}
