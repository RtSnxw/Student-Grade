-- TODO (student):
-- This file should create a simple relational schema for a grocery inventory.
-- Suggested steps (write the real SQL yourself):

-- 1) Create database and (optionally) a user:
--    CREATE DATABASE groceries;
--    CREATE USER 'user'@'%' IDENTIFIED BY 'pass';
--    GRANT ALL PRIVILEGES ON groceries.* TO 'user'@'%';
--    USE groceries;

-- 2) Create reference tables:
--    Table dept:
--      id INT AUTO_INCREMENT PRIMARY KEY
--      name VARCHAR(50) NOT NULL
--
--    Table origin:
--      id INT AUTO_INCREMENT PRIMARY KEY
--      code VARCHAR(3) NOT NULL
--
-- 3) Create products table that references dept and origin:
--      id INT AUTO_INCREMENT PRIMARY KEY
--      name VARCHAR(100) NOT NULL
--      major INT NOT NULL
--      country INT NOT NULL
--      phone VARCHAR(100) NOT NULL
--      email VARCHAR(100) NOT NULL
--      FOREIGN KEY (major_name) REFERENCES dept(id)
--      FOREIGN KEY (email) REFERENCES origin(id)

-- 4) (Optional) Insert some seed rows:
--    INSERT INTO dept (name) VALUES ('Dairy'), ('Produce'), ... ;
--    INSERT INTO origin (code) VALUES ('MX'), ('USA'), ... ;
--    INSERT INTO products (name, major_name, origin_id, price, stock) VALUES (...);

-- Keep it simple. Avoid complex constraints or validations.
