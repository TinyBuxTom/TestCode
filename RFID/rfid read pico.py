from mfrc522 import MFRC522
from machine import Pin, Timer, PWM
import time
import _thread

led = Pin(5, Pin.OUT)
buzzer = PWM(Pin(15))
buzzer.freq(1000)

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
    
              
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

def buzz():
    buzzer.duty_u16(10000)
    time.sleep(0.5)
    buzzer.duty_u16(0)



print("")
print("Place card before reader to read from address 0x08")
print("")


try:
    while True:

        (stat, tag_type) = reader.request(reader.REQIDL)

        if stat == reader.OK:
    
            (stat, uid) = reader.SelectTagSN()
        
            if stat == reader.OK:
                print("")
                print("New card detected %s" % uidToString(uid))
                led.toggle()
                _thread.start_new_thread(buzz, ())
                time.sleep(1.5)
                led.toggle()
            else:
                print("Authentication error")

except KeyboardInterrupt:
    print("Bye")

