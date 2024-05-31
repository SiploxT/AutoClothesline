from machine import ADC, Pin, PWM
from time import sleep_ms
import dht

d = dht.DHT11(machine.Pin(12))

temp = 0

rojo = PWM(Pin(15))
azul = PWM(Pin(14))
verde = PWM(Pin(16))

rele=Pin(6,Pin.OUT)
          
while True:
    
    if temp>=25:
        rojo.duty_u16(65535)
        verde.duty_u16(0)
        azul.duty_u16(0)
    elif temp<25 and temp>10:
        rojo.duty_u16(0)
        verde.duty_u16(65535)
        azul.duty_u16(0)
    else:
        rojo.duty_u16(0)
        verde.duty_u16(0)
        azul.duty_u16(65535)
        
    if temp>10:
        rele.on()
    else:
        rele.off()