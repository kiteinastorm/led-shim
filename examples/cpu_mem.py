#!/usr/bin/env python

import time
from sys import exit

try:
    import psutil
except ImportError:
    exit('This script requires the psutil module\nInstall with: sudo pip install psutil')

import ledshim

ledshim.set_clear_on_exit()


def show_graph(i, v, r, g, b):
    v *= ledshim.NUM_PIXELS/2
    for x in range(ledshim.NUM_PIXELS/2):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
        ledshim.set_pixel(x + i*ledshim.NUM_PIXELS/2, r, g, b)
        v -= 1

    ledshim.show()


ledshim.set_brightness(0.6)

while True:
    c = psutil.cpu_percent() / 100.0
    show_graph(0, c, 255, 255, 255)
        
    m = psutil.virtual_memory().percent / 100.0
    show_graph(1, m, 255, 255, 255)
    
    time.sleep(0.01)
