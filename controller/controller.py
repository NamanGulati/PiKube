from flask import Flask, render_template
from kubernetes import client, config
from time import sleep

import requests
import json

app = Flask(__name__)

nodesList = []
config.load_kube_config()
v1 = client.CoreV1Api()


@app.route("/on", methods=["GET"])
def on():
    pods = v1.list_pod_for_all_namespaces().items
    pods = list(filter(
        lambda pod: 'app' in pod.metadata.labels and pod.metadata.labels['app'] == 'pigpio', pods))
    for pod in pods:
        nodeIP = pod.status.host_ip
        print("http://"+nodeIP + ":30000/on")
        retry = True
        while retry is True:
            try:
                requests.get("http://"+nodeIP + ":30000/on", timeout=1.5)
                retry = False
            except:
                print('request failed: '+nodeIP)
    return render_template('on.html')


@app.route("/off", methods=["GET"])
def off():
    pods = v1.list_pod_for_all_namespaces().items
    pods = list(filter(
        lambda pod: 'app' in pod.metadata.labels and pod.metadata.labels['app'] == 'pigpio', pods))
    for pod in pods:
        nodeIP = pod.status.host_ip
        print("http://"+nodeIP + ":30000/off")
        retry = True
        while retry is True:
            try:
                requests.get("http://"+nodeIP + ":30000/off", timeout=1.5)
                retry = False
            except:
                print('request failed: '+nodeIP)
    return render_template('off.html')


app.run()
