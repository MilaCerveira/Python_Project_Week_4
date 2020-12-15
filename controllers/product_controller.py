from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint("product", __name__)

@products_blueprint.route("/products", methods=['GET'])
def products():
    products = product_repository.select_all() # NEW
    print(products)
    return render_template("products/index.html", all_products = products)
    
@products_blueprint.route("/products/new", methods =['GET'])
def new_products():
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/new.html", all_manufacturers = manufacturers)

@products_blueprint.route("/products/new", methods=['POST'])
def create_product():
    name = request.form['name']
    description = request.form['description']
    stock_quantity  = request.form['stock_quantity']
    buying_cost  = request.form['buying_cost']
    selling_price = request.form['selling_cost']
    manufacturer_id = request.form["manufacturer_id"]
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, stock_quantity, buying_cost, selling_price, manufacturer)
    product_repository.save(product)
    return redirect('/products')


# SHOW
# GET '/products/<id>'
@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/show.html', product = product)

# EDIT
# GET '/products/<id>/edit'
@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('products/edit.html', product = product, all_manufacturers = manufacturers)

# UPDATE
# PUT '/products/<id>'
@products_blueprint.route("/products/<id>/edit", methods=['POST'])
def update_product(id):
    name = request.form['name']
    description = request.form['description']
    stock_quantity  = request.form['stock_quantity']
    buying_cost  = request.form['buying_cost']
    selling_price = request.form['selling_price']
    manufacturer = manufacturer_repository.select(request.form['manufacturer_id'])
    print(manufacturer.id)
    product = Product(name, description, stock_quantity, buying_cost, selling_price, manufacturer, id)
    product_repository.update(product)
    return redirect('/products')

# DELETE
# DELETE '/products/<id>'
@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')
