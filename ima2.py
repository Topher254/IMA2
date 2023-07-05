print("INTELLIGENT MOBILITY AID")
from machine import Pin, time_pulse_us
import time

# distance calculation parameters
speed_of_sound = 330
pulse_trig_duration = 15

# configure ultrasonic pins
echo_pin = Pin(35,Pin.IN)
trig_pin = Pin(32,Pin.OUT)
# configure vibration motro pin --we will replace led later
vibrator = Pin(26,Pin.OUT)

while True:
  trig_pin.value(0)
  time.sleep_us(5)
  trig_pin.value(1)
  time.sleep_us(pulse_trig_duration)
  trig_pin.value(0)
  echo_duration = time_pulse_us(echo_pin,1,30000)
  distance = speed_of_sound*echo_duration / 2000
  
  

  print("DISTANCE IS : ", distance)
  time.sleep_ms(600)
#if the distance between is less than 30 cm , vibrator turns on
  #def vibrator_motor(distance):
  if distance >= -10:
    vibrator.value(1)
    time.sleep(1)
    vibrator.value(0)
    time.sleep(1)
#     vibrator_motor()
    

