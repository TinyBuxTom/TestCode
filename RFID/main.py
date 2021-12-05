import time
from machine import I2C, Pin, SPI
from mfrc522 import MFRC522

led = Pin(25, Pin.OUT)
true = Pin(15, Pin.OUT)
false = Pin(14, Pin.OUT)
sck = Pin(2, Pin.OUT)
mosi = Pin(3, Pin.OUT)
miso = Pin(4, Pin.OUT)
sda = Pin(1, Pin.OUT)
rst = Pin(0, Pin.OUT)
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
card1 = ""
card2 = ""
card3 = ""
card4 = ""
card5 = ""
card6 = ""

while True:
    led.value(1)
    time.sleep(0.06)
    led.value(0)
    rdr = MFRC522(spi, sda, rst)
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print(uid)
            if uid == card1:
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
            elif uid == card2:
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
            elif uid == card3:
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
            elif uid == card4:
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
            elif uid == card5:
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
            elif uid == card6:
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
            else:
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(0.1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(0.1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(1)