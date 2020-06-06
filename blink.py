#!/usr/bin/env python 3

from gpiozero import LED
from flask import Flask, jsonify
from time import sleep
import threading

app = Flask(__name__)
led = LED(17)


def blink(led):
    t = threading.currentThread()
    while getattr(t, "run", True):
        if getattr(t, "blink", False):
            led.on()
            sleep(1)
            led.off()
            sleep(1)


proc = threading.Thread(target=blink,args=(led,))
proc.run = True
proc.blink = False
proc.start()


@app.route("/on", methods=['GET'])
def ledOn():
    proc.blink = True
    return jsonify({'message': 'turning on'})


@app.route("/off", methods=['GET'])
def ledOff():
    proc.blink = False
    led.off()
    return jsonify({'message': 'turning off'})


app.run(host='0.0.0.0')

proc.run = False
proc.join(3)
