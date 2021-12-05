#Libraries
from gpiozero import Buzzer, LED
from time import sleep

#Set buzzer
buzzer = Buzzer (12)

#Set LED
led = LED(14)

#make variable timeOn and timeOff
timeOn = 0.5
timeOff = 2

def buzz ():
    buzzer.value = 1
    sleep (timeOn)
    buzzer.value = 0

#Forever loop:
try:
    while True:
        buzzer.toggle ()
        led.toggle ()
        sleep (timeOn)
        buzzer.toggle ()
        led.toggle ()
        sleep (timeOff)
        
except KeyboardInterrupt:
    print ('exiting...')