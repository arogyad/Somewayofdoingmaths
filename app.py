from flask import Flask, redirect, url_for, render_template, request, jsonify, session
from webapp.HWES.canvas_process import Canvas
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/canvas", methods=['POST','GET'])
def canvas():
    canvass = Canvas()
    file = request.data
    string = str(file)
    if 'True' in string:
        canvass.clear()
    if len(file.split(b',')) == 2:
        try:
            high_low = session['high_low']
            answer, prediction, list = canvass.get_prediction(file, high_low)
        except:
            high_low = [0,1]
            answer, prediction, list = canvass.get_prediction(file, high_low)
        if '∫' in list:
            int = True
        else:
            int = False
        return jsonify('', render_template('canvas_jen.html',answer = answer, prediction=prediction[0], int=int))
    else:
        canvass.clear()
        return render_template('canvas.html')
@app.route('/high_low', methods=['POST'])
def high_low():
    if request.data:
        data = request.data
        a = re.findall(".+'(.+)'", str(data))[0]
        high_low = a.strip('][').split(',')
        high_low = [int(i) for i in high_low ]
        session['high_low'] = high_low
        return render_template('canvas.html')

if __name__ == '__main__':
    app.secret_key = 'this_session'
    app.run(debug = True)
    session.clear()
