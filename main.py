from flask import Flask, jsonify, make_response, request, render_template
import base64
from fastai.vision.all import load_learner
from math.math_lib import Math


app = Flask(__name__)

math = Math()

model = load_learner('export.pkl')

the_list = []

def transform_image(data):
    data = str(data).split(',')[1]
    image = base64.b64decode(data)
    return image


def get_prediction(image_bytes):
    image = transform_image(image_bytes)
    output = model.predict(image)
    the_list.append(str(output[0]))
    if '∫' in the_list:
        if len(the_list) > 1:
            return math.integration(the_list)
        else:
            return '∫'
    elif 'sqrt' in the_list:
        if len(the_list) > 1:
            return math.sqrt(the_list)
        else:
            return '√'

    else:
        return math.just_maths(the_list)

@app.route('/',methods=["POST","GET"])
def home():
    file = request.data
    rndm = 0
    string = str(file)
    if 'True' in string:
        the_list.clear()
    if len(file.split(b',')) == 2:
        answer = get_prediction(file)
        rndm = answer
        return jsonify('', render_template('second_main.html',x = rndm))

    else:
        return render_template('main.html', x = rndm)

if __name__ == '__main__':
    app.run(debug=True)
