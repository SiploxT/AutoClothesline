from machine import Pin, I2C, ADC, PWM
from esp8266_i2c_lcd import I2cLcd
import dht
import time

LDR = ADC(26)
luz = LDR.read_u16()

sdaPIN = machine.Pin(0)
sclPIN = machine.Pin(1)

DEFAULT_I2C_ADDR = 0X27
i2c = machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

devices = i2c.scan()

global temp
global hum

d = dht.DHT11(machine.Pin(12))

rojo = PWM(Pin(15))
azul = PWM(Pin(14))
verde = PWM(Pin(16))

rele=Pin(6,Pin.OUT)

motor_1A = PWM(Pin(8))
motor_1B = PWM(Pin(9))
motor_1A.freq(10000)
motor_1B.freq(10000)
motor_2A = PWM(Pin(18))
motor_2B = PWM(Pin(19))
motor_2A.freq(10000)
motor_2B.freq(10000)

pulsadorA = Pin(20, Pin.IN, Pin.PULL_UP)
pulsadorB = Pin(21, Pin.IN, Pin.PULL_UP)

n = 0

while True:
    
    if pulsadorA.value() == 0:       
        n += 1
        if n>3:
            n = 0
            
        print(n)
        time.sleep_ms(300)
        
        if n == 0:
            motor_1A.duty_u16(0)
            motor_1B.duty_u16(55000)
            motor_2A.duty_u16(0)
            motor_2B.duty_u16(55000)
        elif n == 1:
            motor_1A.duty_u16(0)
            motor_1B.duty_u16(55000)
            motor_2A.duty_u16(0)
            motor_2B.duty_u16(55000)
        elif n == 2:
            motor_1A.duty_u16(0)
            motor_1B.duty_u16(0)
            motor_2A.duty_u16(0)
            motor_2B.duty_u16(0)
        elif n==3:
            motor_1A.duty_u16(55000)
            motor_1B.duty_u16(0)
            motor_2A.duty_u16(55000)
            motor_2B.duty_u16(0)

    if pulsadorB.value() == 0:
        motor_1A.duty_u16(0)
        motor_1B.duty_u16(0)
        motor_2A.duty_u16(0)
        motor_2B.duty_u16(0)
        time.sleep_ms(300)
        
    time.sleep(2)
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Temperatura:")
    lcd.move_to(0, 1)
    lcd.putstr(temp)
    sleep_ms(3000)

    lcd.clear()

    lcd.move_to(0, 0)
    lcd.putstr("Humedad:")
    lcd.move_to(0, 1)
    lcd.putstr(hum)
    sleep_ms(3000)
    
    lcd.clear()

    lcd.move_to(0, 0)
    lcd.putstr("Cantidad de luz:")
    lcd.move_to(0, 1)
    lcd.putstr(luz)
    sleep_ms(3000)
    
    lcd.clear()
    
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
        
    if temp>20:
        rele.on()
    else:
        rele.off()