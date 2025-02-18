from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz

app = Flask(_name_)

@app.route('/htop')
def htop():
    username = os.getenv("USER") or os.getenv("USERNAME")
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <pre>
    Name: Your Full Name
    Username: {username}
    Server Time (IST): {server_time}

    TOP output:
    {top_output}
    </pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
