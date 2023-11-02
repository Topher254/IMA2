#include <Arduino.h>
#include "sonic.h"

void setup() {
  Serial.begin(115200);
  setupSonic();
}

void loop() {
  runSonic1();
  runSonic2();
}