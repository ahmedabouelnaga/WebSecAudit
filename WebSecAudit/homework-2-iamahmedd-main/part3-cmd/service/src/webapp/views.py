from flask import render_template, request, jsonify
from webapp import app
import subprocess
from datetime import datetime
import re
def hostPing(ip):
    if not re.match(r"^(?:\d{1,3}\.){3}\d{1,3}$|^[a-zA-Z0-9.-]+$", ip):
        return {"error": "Invalid IP or hostname"}
    response = {"host": ip}
    try:
        result = subprocess.run(
            ["ping", "-c1", ip],
            capture_output=True,
            text=True,
            timeout=5
        )
        response["output"] = result.stdout
        if "0% packet loss" in result.stdout:
            response["status"] = "online"
        else:
            response["status"] = "offline"
    except subprocess.TimeoutExpired:
        response["status"] = "offline"
        response["output"] = "Ping command timed out"
    except Exception as e:
        response["status"] = "error"
        response["output"] = str(e)
    response["last_checked"] = str(datetime.now())
    return response
@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')
@app.route("/status", methods=["POST"])
def host_status():
    ip = request.form.get("ip", None)
    if ip:
        return jsonify(hostPing(ip))
    else:
        return jsonify({"error": "IP address is required"})
