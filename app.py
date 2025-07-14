# app.py
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database configuration - using MySQL as backend
db_config = {
    'host': 'mysql-service',  # Kubernetes service name for MySQL
    'user': 'root',
    'password': 'password',
    'database': 'shopping_db'
}

def get_db_connection():
    """Establish connection to MySQL database"""
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    """Home page displaying all products"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    """Add new product to database"""
    name = request.form['name']
    price = request.form['price']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price) VALUES (%s, %s)', (name, price))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Initialize database tables if they don't exist
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price DECIMAL(10, 2) NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()
    
    # Run Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)