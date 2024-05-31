from machine import Pin, PWM
import time

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