# PiFare
Project with a Raspberry Pi Pico interfacing through MicroPython with SSD1306 and MFRC522 aimed to perform actions with Mifare Classic 1K cards

There are some libraries used to interface SSD1306 and MFRC522:
- [micropython-mfrc522](https://github.com/danjperron/micropython-mfrc522)
- [micropython-ssd1306](https://github.com/stlehmann/micropython-ssd1306)

Current features are:
- [X] Bruteforcing Key A and Key B in all sectors.

To do features are:
- [ ] UID cloner with Mifare Classic 1k Gen 1A
- [ ] Some Popular Attacks in Mifare Classic 1k
- [ ] PCB

# Usage
## Wiring
MFRC522 is connected using SPI and SSD1306 (128x32) is connected using I2C.
| Device | Signal | GPIO |
| - | - | - |
|MFRC522|SCK|GP2|
|MFRC522|MOSI|GP3|
|MFRC522|MISO|GP4|
|MFRC522|RST|GP22|
|MFRC522|CS|GP1|
|SSD1306|SDA|GP12|
|SSD1306|SCL|GP13|

## Micropython 
Put all the modules and main.py to the root of Pico (you must have micropython in it) and then follow the instruction in oled screen. You can do it using rshell:

shell
$ rshell -p /dev/ttyACM0 --buffer-size 512
/Projects/PiFare> cp * /pyboard/
Copying '/Projects/PiFare/README.md' to '/pyboard/README.md' ...
Copying '/Projects/PiFare/keys.txt' to '/pyboard/keys.txt' ...
Copying '/Projects/PiFare/ssd1306.py' to '/pyboard/ssd1306.py' ...
Copying '/Projects/PiFare/main.py' to '/pyboard/main.py' ...
Omitting directory /Projects/PiFare/.git
Copying '/Projects/PiFare/mfrc522.py' to '/pyboard/mfrc522.py' ...



## Keys
The keys are stored in keys.txt.
