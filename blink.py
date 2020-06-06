#!/usr/bin/env python 3

from gpiozero import LED
from flask import Flask, jsonify
from time import sleep
import threading

app = Flask(__name__)
led = LED(17)


def blink(led):
    t = threading.currentThread()
    while getattr(t, "run_b", True):
        if getattr(t, "blink", False):
            led.on()
            sleep(0.5)
            led.off()
            sleep(0.5)


proc = threading.Thread(target=blink,args=(led,))
proc.run_b = True
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

proc.run_b = False
proc.join(3)
led.off()
