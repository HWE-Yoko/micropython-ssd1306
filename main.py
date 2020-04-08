import time
from SSD1306 import SSD1306
import lcd_gfx
import network
import bmp

d = SSD1306()
d.poweron()
d.init_display()

d.clear()
d.p_string('The quick brown fox jumped over the lazy dog')
d.display()
time.sleep(5)

d.clear()
lcd_gfx.drawTrie(42,2,21,23,63,23,d,1)
d.display()
time.sleep(1)

d.clear()
lcd_gfx.drawFillRect(10,12,20,20,d,1)
d.display()
time.sleep(1)

d.clear()
lcd_gfx.drawCircle(70,24,20,d,1)
d.display()
time.sleep(1)

d.clear()
bmp.bmp('icon.bmp',d)
d.display()
time.sleep(5)

d.clear()
d.p_string('HHHHHHHHHHHHHHHHHHHHH')
d.p_string('HHHHHHHHHHHHHHHHHHHHH')
d.p_string('HHHHHHHHHHHHHHHHHHHHH')
d.p_string('HHHHHHHHHHHHHHHHHHHHH')
d.p_string('HHHHHHHHHHHAHHHHHHHHH')
d.p_string('HHHHHHHHHHHHHHHHHHHHH')
d.p_string('HHHHHHHHHHHHHHHHHHHHH')
d.p_string('HHHHHHHHHHHHHHHHHHHHH')
d.display()
time.sleep(5)

while 0:

    d.clear()
    bmp.bmp('icon.bmp',d)
    d.display()
    time.sleep(1)

    d.clear()
    bmp.bmp('icon1.bmp',d)
    d.display()
    time.sleep(1)
