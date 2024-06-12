import sqlite3

def add_seasonal_flavors_offerings(name, ingredients):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO seasonal_flavors_offerings (name, ingredients) VALUES (?, ?)', (name, ingredients))
    conn.commit()
    conn.close()

def add_ingredient_inventory(name, quantity):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO ingredient_inventory_inventory (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    conn.close()

def add_customer_flavor_suggestion(flavor_name, suggested_by, allergens):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO customer_flavor_suggestions (flavor_name, suggested_by, allergens) VALUES (?, ?, ?)', (flavor_name, suggested_by, allergens))
    conn.commit()
    conn.close()

def add_allergen(name):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO allergens (name) VALUES (?)', (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Allergen '{name}' already exists.")
    conn.close()

def add_to_cart(product_id, product_name, quantity):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('INSERT INTO cart (product_id, product_name, quantity) VALUES (?, ?, ?)', (product_id, product_name, quantity))
    conn.commit()
    conn.close()

def search_flavors(keyword):
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('SELECT * FROM seasonal_flavors WHERE name LIKE ?', ('%' + keyword + '%',))
    results = c.fetchall()
    conn.close()
    return results

def view_cart():
    conn = sqlite3.connect('ice_cream_parlor.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cart')
    results = c.fetchall()
    conn.close()
    return results

# Example usage
if __name__ == "__main__":
    # Add sample data
    add_seasonal_flavor(' Banana Butterscotch', 'Milk, Sugar, Vanilla Extract')
    add_seasonal_flavor('Chocolate Heaven', 'Milk, Sugar, Cocoa Powder')
    add_ingredient('Milk', 50)
    add_ingredient('Sugar', 30)
    add_flavor_suggestion('Mango Tango', 'Sam', 'None')
    add_allergen('Peanuts')
    add_to_cart(1, 'Banana Butterscotch', 2)
    
    # Search flavors
    print(search_flavors('Butterscotch'))
    
    # View cart
    print(view_cart())
