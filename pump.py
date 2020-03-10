#!/usr/bin/env python

from time import sleep
from RPi.GPIO as GPIO

POWER_PIN  = 18
GROUND_PIN = 20
INPUT_PIN  = 22

OUTPUT_PIN = 8

def cleanup():
    GPIO.setwarnings(False)
    GPIO.cleanup()

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(POWER_PIN, GPIO.OUT)
    GPIO.setup(OUTPUT_PIN, GPIO.OUT)
    GPIO.output(POWER_PIN, GPIO.HIGH)


def inputChange():
    GPIO.remove_event_detect(INPUT_PIN)
    pumpIsOn = False
    currentSpeed = 1
    try:
        while currentSpeed > 0 and currentSpeed < 500
        hits = 0
        for x in range (0,500):
            hits += GPIO.input(INPUT_PIN)
            sleep(0.001)
        currentSpeed = hits
        if pumpIsOn is False and currentSpeed > 50 and currentSpeed < 450:
            print("PUMP ON")
            pumpIsOn = True
            GPIO.output(OUTPUT_PIN, GPIO.HIGH)
        if pumpIsOn = True:
            print("Current Speed: ", hits)
    finally:
        if pumpIsOn is True:
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
