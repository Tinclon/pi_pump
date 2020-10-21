#!/usr/bin/env python

from time import sleep
from RPi.GPIO as GPIO

SENSOR_POWER_ON   = GPIO.HIGH
SENSOR_POWER_PIN  = 18
SENSOR_GROUND_PIN = 20
SENSOR_INPUT_PIN  = 22

PUMP_POWER_PIN    = 4
PUMP_GROUND_PIN   = 6
PUMP_CONTROL_PIN  = 8
PUMP_CONTROL_ON   = GPIO.LOW
PUMP_CONTROL_OFF  = GPIO.HIGH

def cleanup():
    GPIO.setwarnings(False)
    GPIO.cleanup()

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SENSOR_INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(SENSOR_POWER_PIN, GPIO.OUT)
    GPIO.setup(PUMP_CONTROL_PIN, GPIO.OUT)
    GPIO.output(SENSOR_POWER_PIN, SENSOR_POWER_ON)
    GPIO.output(PUMP_CONTROL_PIN, PUMP_CONTROL_OFF)


def inputChange():
    GPIO.remove_event_detect(SENSOR_INPUT_PIN)
    pumpIsOn = False
    currentSpeed = 1
    try:
        while currentSpeed > 0 and currentSpeed < 100:
            hits = 0
            for x in range (0,100):
                hits += GPIO.input(SENSOR_INPUT_PIN)
                sleep(0.001)
            currentSpeed = hits
            if pumpIsOn is False and currentSpeed > 1:
                #print("PUMP ON")
                pumpIsOn = True
                GPIO.output(PUMP_CONTROL_PIN, PUMP_CONTROL_ON)
            #if pumpIsOn = True:
            #    print("Current Speed: ", hits)
    finally:
        #if pumpIsOn is True:
            #print("PUMP OFF")
        GPIO.output(PUMP_CONTROL_PIN, PUMP_CONTROL_OFF)
        sleep(2)
        cleanup()
        setup()
        GPIO.add_event_detect(SENSOR_INPUT_PIN, GPIO.BOTH, callback=lambda pin: inputChange(), bouncetime = 100)

def listen():
    sleep(2)
    cleanup()
    setup()
    print("LISTENING")
    GPIO.add_event_detect(SENSOR_INPUT_PIN, GPIO.BOTH, callback=lambda pin: inputChange(), bouncetime = 100)
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        pass
    finally
        cleanup()

listen()
