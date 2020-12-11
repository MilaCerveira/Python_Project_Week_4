#Make product crud functions Create Read Update Delete
from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

# crud function to save a product into product database
def save(product):
    sql = "INSERT into products (name, description, stock_quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_price, product.manufacturer.id]
    results = run_sql(sql, values)
    id = results [0]['id']
    product.id = id 
    return product 

# crud function to select 
