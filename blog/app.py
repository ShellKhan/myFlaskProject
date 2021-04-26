from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return 'This is a POST request'
    else:
        return 'This is a GET request'
