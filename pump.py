#!/usr/bin/env python

from time import sleep
from RPi.GPIO as GPIO

INPUT_PIN = 8
OUTPUT_PIN = 11

def cleanup():
    GPIO.setwarnings(False)
    GPIO.cleanup()

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(OUTPUT_PIN, GPIO.OUT)

def inputChange():
    GPIO.remove_event_detect(INPUT_PIN)
    print("PUMP ON")
    GPIO.output(OUTPUT_PIN, GPIO.HIGH)
    sleep(1)
    currentSpeed = 1
    try:
        while currentSpeed > 0 and currentSpeed < 500
        hits = 0
        for x in range (0,500):
            hits += GPIO.input(INPUT_PIN)
            sleep(0.001)
        currentSpeed = hits
        print("Current Speed: ", hits)
    finally:
        print("PUMP OFF")
        GPIO.output(OUTPUT_PIN, GPIO.LOW)
        listen()

def listen():
    cleanup()
    setup()
    print("LISTENING")
    GPIO.add_event_detect(INPUT_PIN, GPIO.BOTH, callback=lambda pin: inputChange(), bouncetime = 500)
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        pass
    finally
        cleanup()

listen()
