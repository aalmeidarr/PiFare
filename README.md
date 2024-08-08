# PiFare
Project with a Raspberry Pi Pico interfacing through MicroPython with SSD1306 and MFRC522 aimed to perform actions with Mifare Classic 1K cards.



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
| Signal | GPIO |
| - | - |
| 

## Micropython 
Put all the modules and `main.py` to the root of Pico (you must have micropython in it) and then follow the instruction in oled screen. You can do it using `rshell`:
```shell

```




