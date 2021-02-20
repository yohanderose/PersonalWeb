from flask import Flask, render_template, redirect, send_file
import requests

app = Flask(__name__)
app.secret_key = "blahblah"


# @app.route('/misc')
# def hello_world():
    # return render_template('about.php')

@app.route('/misc/harry')
def harry():
    return render_template('harry.html')

@app.route('/misc/training')
def training():
    return render_template('programme.html')

@app.route('/misc/wallpaper')
def wallpaper():
    return send_file('background.jpg', mimetype='image/png')

@app.route('/misc/life')
def life():
    return send_file('LifeMap.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6549)
