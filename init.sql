-- init.sql
CREATE DATABASE IF NOT EXISTS shoppping_db;
USE shoppping_db;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Sample data
INSERT INTO products (name, price) VALUES ('Apple', 1.99);
INSERT INTO products (name, price) VALUES ('Bread', 2.49);
INSERT INTO products (name, price) VALUES ('Milk', 3.19);