from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturer", __name__)


@manufacturers_blueprint.route("/manufacturers", methods=['GET'])
def manufacturers():
    manufacturers = manufacturer_repository.select_all() # NEW
    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)
    
@manufacturers_blueprint.route("/manufacturers/new", methods =['GET'])
def new_manufacturers():
    return render_template("manufacturers/new.html")

@manufacturers_blueprint.route("/manufacturers/new", methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    phone = request.form['phone']
    website = request.form['website']
    email  = request.form['email']
    manufacturer = Manufacturer(name, phone, website, email)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')


# SHOW
# GET '/manufacturers/<id>'
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/show.html', manufacturer = manufacturer)

# EDIT
# GET '/products/<id>/edit'
@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/edit.html', manufacturer = manufacturer)

# UPDATE
# PUT '/manufacturers/<id>'
@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['POST'])
def update_manufacturer(id):
    name = request.form['name']
    phone = request.form['phone']
    website  = request.form['website']
    email  = request.form['email']
    manufacturer = Manufacturer(name, phone, website, email, id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')

# DELETE
# DELETE '/manufacturer/<id>'
@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')
