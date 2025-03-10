from flask import Flask,jsonify
import psutil
import time
app = Flask(__name__)


@app.route("/")
def mem_cpu():
    cpu_usage=psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent

    return jsonify({"cpu_usage": cpu_usage, "memory_usage": mem})