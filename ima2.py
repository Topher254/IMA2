print("INTELLIGENT MOBILITY AID")
from machine import Pin, time_pulse_us
import time

# distance calculation parameters
speed_of_sound = 330
pulse_trig_duration = 15
min_distance = 30000

# configure ultrasonic pins
echo_pin = Pin(35,Pin.IN)
trig_pin = Pin(32,Pin.OUT)
# configure vibration motro pin --we will replace led later
vibrator = Pin(26,Pin.OUT)
#panic button 
panic_button = Pin(14,Pin.IN)

while True:
  trig_pin.value(0)
  time.sleep_us(5)
  trig_pin.value(1)
  time.sleep_us(pulse_trig_duration)
  trig_pin.value(0)
  echo_duration = time_pulse_us(echo_pin,1,30000)
  distance = speed_of_sound*echo_duration / 20000
  
  

  print("DISTANCE IS : ", distance)
  time.sleep_ms(600)
#if the distance between is less than 30 cm , vibrator turns on
  def vibrator_motor(distance_1):
    if distance_1 > min_distance:
      vibrator.value(1)
      time.sleep(1)
      vibrator.value(0)
      time.sleep(1)
    else:
        vibrator.value(0)
  vibrator_motor(distance)
  #function for the buzzer
  def buzzer_part():
      logic = panic_button.value()
      if logic == 1:
          vibrator_motor(distance)
      else:
          vibrator.value(0)
  buzzer_part()
      
    

