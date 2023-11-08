#include <Wire.h>
#include <TinyGPS++.h>
#include <WiFi.h>
#include <WiFiAP.h>
#include <WiFiClient.h>

#define TRIG_PIN 12
#define TRIG_PIN_2 33
#define ECHO_PIN 32
#define ECHO_PIN_2 35
#define buzzer 25
#define push_me 26
#define TX 17
#define RX 16

float duration_us, distance_cm;
struct GPS_Data{
    double latitude;
    double longitude;; 
    uint time;
};
//AP credentials
const char* mySSID = "ESP32-AP";
const char* myPassword = "esp32wifi";
/* GPS Setup*/
HardwareSerial hard(2);
TinyGPSPlus gps;

void setup() {
  // begin serial port
  Serial.begin (9600);

  /* Setup GPS*/
  hard.begin(9600, SERIAL_8N1, RX, TX);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(TRIG_PIN_2, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(ECHO_PIN_2, INPUT);
  pinMode(buzzer,OUTPUT);
  pinMode(push_me,INPUT);

  //setup hotspot
  WiFi.softAP(mySSID, myPassword);
  IPAddress myIP = WiFi.softAPIP();
  Serial.println();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
}

void loop() {
  float sonic1 = getDistance1();
  float sonic2 = getDistance2();
  GPS_Data gps = readGPS();
  // Serial.println(runHTTPclient("data","{\"sonic1\":"+String(sonic1)+",\"sonic2\":"+String(sonic2)+"}"));
  // Serial.println(runHTTPclient("data","{\"lat\":"+String(gps.latitude)+",\"long\":"+String(gps.longitude)+"}"));
  /*if (distance_cm < 50)
    digitalWrite(buzzer,HIGH);
  else
    digitalWrite(buzzer,LOW);*/
  
  //delay(500);

  int push_button_state = digitalRead(push_me);
  Serial.print("Butt = ");
  Serial.println(push_button_state);

  if (push_button_state == 1){
    Serial.println("Shouting !!!");
    digitalWrite(buzzer,HIGH);
    delay(5000);
    Serial.println("\tPin Drop");
  }
  else
    digitalWrite(buzzer,LOW);
}

float getDistance1(){
  // generate 10-microsecond pulse to TRIG pin
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // measure duration of pulse from ECHO pin
  duration_us = pulseIn(ECHO_PIN, HIGH);

  // calculate the distance
  distance_cm = 0.017 * duration_us;

  // print the value to Serial Monitor
  Serial.print("distance: ");
  Serial.print(distance_cm);
  Serial.println(" cm");
  return distance_cm;
}

float getDistance2(){
  // generate 10-microsecond pulse to TRIG pin
  digitalWrite(TRIG_PIN_2, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN_2, LOW);

  // measure duration of pulse from ECHO pin
  duration_us = pulseIn(ECHO_PIN_2, HIGH);

  // calculate the distance
  distance_cm = 0.017 * duration_us;

  // print the value to Serial Monitor
  Serial.print("distance: ");
  Serial.print(distance_cm);
  Serial.println(" cm");
  return distance_cm;
}

bool runHTTPclient(String command,String payload){
  const int    HTTP_PORT   = 80;
  const String HTTP_METHOD = "GET"; // or "POST"
  const char   HOST_NAME[] = "192.168.4.2"; // hostname of web server:
  const String PATH_NAME   = "";
  String queryString = "/distance?command="+command+"&payload="+payload;

  WiFiClient client;
  if(client.connect(HOST_NAME, HTTP_PORT)) {
    Serial.println("Connected to server");
    // send HTTP request header
    client.println("GET " + PATH_NAME + queryString + " HTTP/1.1");
    client.println("Host: " + String(HOST_NAME));
    client.println("Connection: close");
    client.println(); // end HTTP header
    return true;
  } else {
    Serial.println("connection failed");
    return false;
  }
}

GPS_Data readGPS(){
  struct GPS_Data gps_data;
  while (hard.available() > 0) gps.encode(hard.read());
  if (gps.location.isUpdated()){
      gps_data.latitude = gps.location.lat();
      gps_data.longitude = gps.location.lng();
      gps_data.time = gps.time.value();
      Serial.println("[!!] GPS Data Received [!!]");
  }
  return gps_data;
}