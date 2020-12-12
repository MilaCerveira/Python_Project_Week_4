#Make manufacturer crud functions Create Read Update Delete
from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product 

#Make crud function to add a manufacturer to database table manufacturer
def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, phone, website, email) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.phone, manufacturer.website, manufacturer.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id 
    return manufacturer

#Make crud function to select all manufacturers from database manufacturer table
def select_all():
    manufacturer = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql) 

    for row in results:
        manufacturer = Manufacturer(row['name'], row['phone'], row['website'], row['email'])
    return manufacturer

#Make crud function that selects by id?
def select(id):
    manufacturer = None 
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(results['name'], ['phone'], ['website'], ['email'])
    return manufacturer

#Make crud function to delete all 
    def delete_all():
        sql = "DELETE FROM manfacturers"
        run_sql(sql)
#make crud function to delete by id?
    def delete(id):
        sql = "DELETE FROM manfacturers WHERE id = %"
        values = [id]
        run_sql(sql, values)
#make crud function to update manfacturers
    def update(manufacturer):
        sql = "UPDATE manufacturers SET (name, phone, website, email) = (%s, %s, %s, %s) WHERE id =%s"
        values = [manufacturer.name, manufacturer.phone, manufacturer.website, manufacturer.email, manufacturer.id]
        run_sql(sql, values)

