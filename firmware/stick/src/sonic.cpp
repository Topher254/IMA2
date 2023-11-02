#include <Arduino.h>
#include "defs.h"

void setupSonic(){
  pinMode(ultrasonic1_trigger, OUTPUT);
  pinMode(ultrasonic1_echo, INPUT);
  pinMode(ultrasonic2_trigger, OUTPUT);
  pinMode(ultrasonic2_echo, INPUT);
}
void runSonic1(){
  digitalWrite(ultrasonic1_trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(ultrasonic1_echo, HIGH);
  delayMicroseconds(10);
  digitalWrite(ultrasonic1_trigger, LOW);
  int duration = pulseIn(ultrasonic1_echo, HIGH);
  int distance = duration * 0.034 / 2;
  Serial.print("Distance: ");
  Serial.println(distance);
}
void runSonic2(){
  digitalWrite(ultrasonic2_trigger, LOW);
  delayMicroseconds(2);
  digitalWrite(ultrasonic2_echo, HIGH);
  delayMicroseconds(10);
  digitalWrite(ultrasonic2_trigger, LOW);
  int duration = pulseIn(ultrasonic2_echo, HIGH);
  int distance2 = duration * 0.034 / 2;
  Serial.print("Distance: ");
  Serial.println(distance2); 
}
