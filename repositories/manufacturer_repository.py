#Make manufacturer crud functions Create Read Update Delete
from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product 

#Make crud function to add a manufacturer to database table manufacturer
def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, phone, website, email) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.phone, manufacturer.website, manufacturer.email]
    results = run_sql(sql, values)
    print(results)
    id = results[0]['id']
    manufacturer.id = id 
    return manufacturer

#Make crud function to select all manufacturers from database manufacturer table
def select_all():
    manufacturer = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql) 
    print(results)
    for row in results:
        manufacturer.append(Manufacturer(row[1], row[2], row[3], row[4], row[0]))
    return manufacturer

#Make crud function that selects by id?
def select(id):
    print(id)
    manufacturer = None 
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    print("Manufacturer:", result)
    if result is not None:
        manufacturer = Manufacturer(result[1], result[2], result[3], result[4], result[0])
    return manufacturer

#Make crud function to delete all 
def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)
#make crud function to delete by id?
def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    print(result)
#make crud function to update manfacturers
def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, phone, website, email) = (%s, %s, %s, %s) WHERE id =%s"
    values = [manufacturer.name, manufacturer.phone, manufacturer.website, manufacturer.email, manufacturer.id]
    run_sql(sql, values)

