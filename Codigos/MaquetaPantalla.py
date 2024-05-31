from machine import Pin, I2C, ADC
from esp8266_i2c_lcd import I2cLcd
import dht
import time

LDR = ADC(26)
luz = LDR.read_u16()
luz = round(luz/65535*100,2)

sdaPIN = machine.Pin(0)
sclPIN = machine.Pin(1)

DEFAULT_I2C_ADDR = 0X27
i2c = machine.I2C(0,sda=sdaPIN, scl=sclPIN, freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

temp = 0
hum = 0

d = dht.DHT11(machine.Pin(12))

while True:
    
    time.sleep(2)
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("Temperatura:")
    lcd.move_to(0, 1)
    lcd.putstr(str(temp) + chr (0xDF) + "C")
    time.sleep(3)

    lcd.clear()

    lcd.move_to(0, 0)
    lcd.putstr("Humedad:")
    lcd.move_to(0, 1)
    lcd.putstr(str(hum) + "%")
    time.sleep(3)
    
    lcd.clear()

    lcd.move_to(0, 0)
    lcd.putstr("Cantidad de luz:")
    lcd.move_to(0, 1)
    lcd.putstr(str(luz) + "%")
    time.sleep(3)    
    lcd.clear()