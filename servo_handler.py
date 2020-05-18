import RPi.GPIO as io
import time

io.setmode(io.BOARD)
io.setup(13, io.OUT)
p = io.PWM(13, 50)
p.start(2.5)

class ServoHandler:
    def move(degs):
        global dc
        deg = abs(float(degs))
        dc = 0.056 * deg + 2.5
        p.ChangeDutyCycle(dc)

