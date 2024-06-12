import sqlite3

def create_tables():
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    
    # Create table for seasonal flavors offering
    c.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors_offering (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ingredients TEXT NOT NULL
        )
    ''')
    
    # Create table for ingredient inventory
    c.execute('''
        CREATE TABLE IF NOT EXISTS ingredient_inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    
    # Create table for customer flavor suggestions
    c.execute('''
        CREATE TABLE IF NOT EXISTS customer_flavor_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_name TEXT NOT NULL,
            suggested_by TEXT NOT NULL,
            allergens TEXT
        )
    ''')
    
    # Create table for allergens
    c.execute('''
        CREATE TABLE IF NOT EXISTS allergens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    
    # Create table for cart
    c.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (product_id) REFERENCES seasonal_flavors(id)
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
