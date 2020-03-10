#!/usr/bin/env python

from time import sleep
from RPi.GPIO as GPIO

INPUT_PIN=8

def cleanup():
    GPIO.cleanup()

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def inputChange():
    print("PUMP ON")
    GPIO.remove_event_detect(INPUT_PIN)
    sleep(1)
    currentSpeed = 100
    try:
        while currentSpeed > 10 and currentSpeed < 490
        hits = 0
        for x in range (0,500):
            hits += GPIO.input(INPUT_PIN)
            sleep(0.001)
        currentSpeed = hits
        print("Current Speed: ", hits)
    finally:
        print("PUMP OFF")
        listen()

def listen():
    cleanup()
    setup()
    print("LISTENING")
    GPIO.add_event_detect(INPUT_PIN, GPIO.BOTH, callback=lambda pin: inputChange(), boundetime=500)
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        pass
    finally
        cleanup()

listen()
