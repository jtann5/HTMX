
from flask import Flask, render_template, send_from_directory, jsonify, request, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
import itertools
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'), static_folder='static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy()
db.init_app(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(100))
    price = db.Column(db.Float)
    illegalness = db.Column(db.Integer)
    description = db.Column(db.Text)
    
images = ['../../static/images/rocketpic1.JPG', '../../static/images/rocketpie2.JPG', '../../static/images/skateboard1.JPG']

@app.errorhandler(404) 
def not_found(e): 
   return render_template('error404.html')

@app.route('/')
def index():
    print(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))

    return render_template('index.html')

@app.route('/store')
def store():
    id = request.args.get("id")

    if id: 
        if int(id) < 100:
            return render_template('store.html', content='/product_page?id='+id)
        else:
            return render_template('store.html', content='/product_not_found?id='+id)
        
    return render_template('store.html', content='/tab4')

@app.route('/product_page')
def product_page():
    id = request.args.get("id")
    return render_template('html/product_page.html', id=id)

@app.route('/product_not_found')
def product_not_found():
    id = request.args.get("id")
    return render_template('html/product_not_found.html', id=id)

@app.route('/images/logo.png')
def download_file(filename):
    return send_from_directory('static/images', filename)

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

@app.route('/tab4')
def tab4():
    return render_template('html/tab4.html')

@app.route("/search")
def search():
    query = request.args.get("query")
    minPrice = request.args.get("minPrice")
    maxPrice = request.args.get("maxPrice")

    print("Search Term: " + query)
    print("Price range: " + minPrice + " to " + maxPrice)

    if query.lower() == "gigachad":
        return render_template("html/cool.html")

    products=[]

    for i in range(100):
        products.append(Product(id=i, name="Interplanetary Technologies Booty Shorts", image="../../static/images/theshorts.jpg", price=99.99, illegalness=10, description="SEX TIME"))

    return render_template("html/search_results.html", products=products)


if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=3061)