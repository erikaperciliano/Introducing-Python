from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# Creates Model
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  price = db.Column(db.Float, nullable=False)
  description = db.Column(db.Text, nullable=True)

@app.route('/api/products/add', methods=['POST'])
def add_product():
    data = request.json
    product = Product(name=data['price'], price=data['price'], description=data.get('description', '')) #creates product
    db.session.add(product) # add the product at database
    db.session.commit() # sett the command to database
    return 'Product registered successfully!'

@app.route('/')
def hello_world():
  return 'Hello World'

if __name__ == '__main__':
  app.run(debug=True)
