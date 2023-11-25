
from flask import Flask, render_template, send_from_directory, jsonify
import itertools
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'), static_folder='static')

images = ['../../static/images/rocketpic1.JPG', '../../static/images/rocketpie2.JPG', '../../static/images/skateboard1.JPG']

@app.route('/')


def index():
    print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

    return render_template('index.html')


@app.route('/images/logo.png')
def download_file(filename):
    return send_from_directory('static/images', filename)

@app.route('/get_images')
def get_images():
    image_data = []
    image_folder = 'images'
    for filename in os.listdir('static/images'):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Filter by image extension
            image_data.append({'filename': filename})
    return jsonify(image_data)


@app.route('/click', methods=['GET'])
def click():
    # This is just a simple example to return some data on click
    return "Button Clicked motherfucker!"


@app.route('/tab1')
def tab1():
    return render_template('html/tab1.html')

@app.route('/tab2')
def tab2():
    return render_template('html/tab2.html')

@app.route('/tab3')
def tab3():
    return render_template('html/tab3.html')


if __name__ == '__main__':
    app.run(debug=True)