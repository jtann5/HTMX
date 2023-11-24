
from flask import Flask, render_template
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

@app.route('/')


def index():
    print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

    return render_template('index.html')

@app.route('/click', methods=['GET'])
def click():
    # This is just a simple example to return some data on click
    return "Button Clicked!"

if __name__ == '__main__':
    app.run(debug=True)