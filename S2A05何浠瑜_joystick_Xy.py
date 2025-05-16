from machine import Pin, ADC
from time import sleep

# 設定 LED 腳位
led_up = Pin(5, Pin.OUT)    # D1
led_down = Pin(4, Pin.OUT)  # D2
led_left = Pin(0, Pin.OUT)  # D3
led_right = Pin(2, Pin.OUT) # D4

joystick_x = ADC(0) 
joystick_y = ADC(0)  

CENTER = 512   # 中心值
THRESHOLD = 150 

def clear_leds():
    led_up.off()
    led_down.off()
    led_left.off()
    led_right.off()

while True:
    x_val = joystick_x.read() 
    y_val = joystick_y.read()  

    clear_leds() 

    if x_val < CENTER - THRESHOLD:
        led_left.on()
    elif x_val > CENTER + THRESHOLD:
        led_right.on()

    if y_val < CENTER - THRESHOLD:
        led_up.on()
    elif y_val > CENTER + THRESHOLD:
        led_down.on()

    sleep(0.1)