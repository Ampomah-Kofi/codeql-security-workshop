
import ipaddress
import subprocess
from flask import request, Flask

app = Flask(__name__)

@app.route("/ping")
def ping():
    target = request.args.get("host", "127.0.0.1")

    try:
        address = str(ipaddress.ip_address(target))
    except ValueError:
        return "Invalid IP address", 400

    subprocess.check_output(
        ["ping", "-c", "1", address],
        shell=False,
        timeout=5
    )

    return "OK"
