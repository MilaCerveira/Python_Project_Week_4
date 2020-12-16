# Python_Project_Week_4
The Brief
Shop Inventory
Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

MVP
The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
The inventory should track manufacturers, including a name and any other appropriate details.
The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
Show an inventory page, listing all the details for all the products in stock in a single view.
As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.
Inspired by
eBay, Amazon (back end only), Magento
Build an app which allows a shopkeeper to track their shop's inventory.

Technology used:
Python
SQL
Html
CSS
PsychoPG
Flask

To Clone and Run this project:
1. Git pull
2. Open your terminal
3. Create a data base "store_manager" 
4. run "psql -d <database name> -f db/<filename.sql>" to drop and create the database do this twice to ensure exists.
5. run "python3 console.py" in console.py file to populate the data base.
6. run "flask run" and open a google chrome browser copy the local host into the browser eg. "http://127.0.0.1:5000/"
7. Hopefully it's working if not you'll find me crying somewhere
