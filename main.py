from machine import Pin, I2C
from mfrc522 import MFRC522
from ssd1306 import SSD1306_I2C
from utime import sleep_ms

OLED_SDA_PIN=12
OLED_SCL_PIN=13
I2C_ID=0
WIDTH=128
HEIGHT=32

SPI_ID=0
MFRC522_SCK=2
MFRC522_MOSI=3
MFRC522_MISO=4
MFRC522_RST=22
MFRC522_CS=1

BTN_PIN = 21

def int_to_hexstr(lst: list) -> str:
    return "".join([f"{i:02X}".upper() for i in lst])

def hexstr_to_int(hexstr: str) -> list:
    return [int(hexstr[i:i+2], 16) for i in range(0, len(hexstr), 2)]


def init_oled() -> SSD1306_I2C:
    i2c = I2C(I2C_ID, sda=Pin(OLED_SDA_PIN), scl=Pin(OLED_SCL_PIN), freq=200000)
    oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
    oled.text("   PiFare v0.1", 0, 10)
    oled.text("   @aalmeidarr", 0, 20)
    oled.show()
    sleep_ms(1000)
    return oled

def search(reader: MFRC522) -> list:
    try:
        status, _ = reader.request(reader.REQIDL)
        while status != reader.OK:
            status, _ = reader.request(reader.REQIDL)
        status, uid = reader.SelectTagSN()
        if status == reader.OK:
            return uid
        else:
            return None
    except KeyboardInterrupt:
        oled.clear()
        oled.text("[!] Exiting...", 0, 0)
        oled.show()


def bruteforce(reader: MFRC522, oled: SSD1306_I2C, uid: list,  keys: list) -> list:
    results = []
    for sector in range(16):
        for letter in ['A', 'B']:
            i = 0
            status = reader.ERR
            while status == reader.ERR and i < len(keys):
                key = keys[i]
                oled.fill(0)
                oled.text("Bruteforcing...", 0, 0)
                oled.text(f"Sector: {sector}", 0, 10)
                oled.text(f"{letter}: {int_to_hexstr(key)}", 0, 20)
                oled.show()
                
                uid = search(reader)
                if letter == 'A':
                    status = reader.auth(reader.AUTHENT1A, sector*4, key, uid)
                elif letter == 'B':
                    status = reader.auth(reader.AUTHENT1B, sector*4, key, uid)

                if status != reader.ERR:
                    oled.fill(0)
                    oled.text(f"Sector: {sector}", 0, 0)
                    oled.text(f"Key {letter}:", 0, 10)
                    oled.text(f"   {int_to_hexstr(key)}", 0, 20)
                    oled.show()
                    oled.invert(0)
                    oled.show()
                    sleep_ms(1000)
                    reader.stop_crypto1()
                    results.append((sector, letter, key))
                i+=1
    return results

if __name__ == "__main__":
    oled = init_oled()
    btn = Pin(BTN_PIN, Pin.IN, Pin.PULL_UP)
    oled.fill(0)
    oled.text("Press to read", 0, 10)
    oled.show()
    while btn.value() != 0:
        pass
    reader = MFRC522(spi_id=SPI_ID, sck=MFRC522_SCK, miso=MFRC522_MISO, mosi=MFRC522_MOSI, rst=MFRC522_RST, cs=MFRC522_CS)
    uid = search(reader)
    oled.fill(0)
    oled.text("[?] Bruteforce:", 0, 0)
    oled.text(f"UID:{int_to_hexstr(uid)}", 0, 10)
    oled.text("Press to confirm", 0, 25)
    oled.show()
    sleep_ms(500)
    while btn.value() != 0:
        pass
    with open("keys.txt", "r") as f:
        keys_list = f.readlines()
    for i, key in enumerate(keys_list):
        key = hexstr_to_int(key.strip())
        keys_list[i] = key
    valid_keys = bruteforce(reader, oled, uid, keys_list)
    oled.fill(0)
    oled.text("Press to view", 0, 0)
    oled.text("      valid keys", 0, 10)
    oled.show()
    while btn.value() != 0:
        pass
    for sector, letter, key in valid_keys:
        oled.fill(0)
        oled.text(f"Sector: {sector}", 0, 0)
        oled.text(f"Letter: {letter}", 0, 10)
        oled.text(f"Key:{int_to_hexstr(key)}", 0, 20)
        oled.show()
        while btn.value() != 0:
            pass
        sleep_ms(500)
    oled.fill(0)
    oled.show()


    
