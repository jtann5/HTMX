
from flask import Flask, render_template, send_from_directory, jsonify, request, Blueprint, redirect
from flask_sqlalchemy import SQLAlchemy
import itertools
import os
import pandas as pd

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

@app.route('/elements/header')
def header():
    page = request.args.get("page")
    return render_template('elements/header.html', page=page)

@app.route('/elements/footer')
def footer():
    return render_template('elements/footer.html')


@app.route('/store')
def store():
    id = request.args.get("id")

    if id: 
        return render_template('store.html', content='/product_page?id='+id)
        
    return render_template('store.html', content='/active_search')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product_page')
def product_page():
    id = request.args.get("id")
    product = Product.query.filter(Product.id == id).first()

    if product:
        return render_template('store/product_page.html', product=product)
    else:
        return render_template('store/product_not_found.html')

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

@app.route('/search_page')
def search_page():
    return render_template('store/search_page.html')

@app.route('/active_search')
def active_search():
    return render_template('store/active_search.html')

@app.route('/filter_search')
def filter_search():
    return render_template('store/filter_search.html')

@app.route("/search")
def search():
    query = request.args.get("query")
    minPrice = request.args.get("minPrice")
    maxPrice = request.args.get("maxPrice")
    sortBy = request.args.get("sortBy")
    sortOrder = request.args.get("sortOrder")

    if query.lower() == "gigachad":
        return render_template("store/cool.html")
    
    # Start building the base query
    base_query = Product.query

    # Apply filters based on parameters
    if query:
        base_query = base_query.filter(Product.name.ilike(f"%{query}%"))
    if minPrice:
        base_query = base_query.filter(Product.price >= float(minPrice))
    if maxPrice:
        base_query = base_query.filter(Product.price <= float(maxPrice))

    # Apply sorting based on parameters
    if sortBy:
        sort_column = getattr(Product, sortBy)
        if sortOrder.lower() == 'descending':
            base_query = base_query.order_by(sort_column.desc())
        else:
            base_query = base_query.order_by(sort_column.asc())

    # Execute the final query
    products = base_query.all()

    return render_template("store/search_results.html", products=products)

def add_data_from_csv(csv_file_path):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Iterate through the rows and add data to the database
    for index, row in df.iterrows():
        product = Product(
            name=row['name'],
            image=row['image'],
            price=row['price'],
            illegalness=row['illegalness'],
            description=row['description']
        )
        db.session.add(product)

    # Commit the changes to the database
    db.session.commit()

if __name__ == '__main__':
    #inp = input("Create database: ")
    #if inp.lower() == 'y' or inp.lower() == 'yes':
    with app.app_context():
        db.drop_all()
        db.create_all()
        add_data_from_csv('data.csv')

    app.run(debug=True, host="localhost", port=3061)