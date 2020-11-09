from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)
app.secret_key = "blahblah"


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/training')
def training():
    return render_template('programme.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6549)
