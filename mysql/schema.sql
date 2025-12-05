--CREATE DATABASE studentsdb;
--USE studentsdb;
--
--CREATE TABLE major (
--    id INT AUTO_INCREMENT PRIMARY KEY,
--    name VARCHAR(50) NOT NULL
--);

--CREATE TABLE country (
--    id INT AUTO_INCREMENT PRIMARY KEY,
--    code VARCHAR(3) NOT NULL
--);

--CREATE TABLE students (
--    id INT AUTO_INCREMENT PRIMARY KEY,
--    name VARCHAR(100) NOT NULL,
--    major_id INT NOT NULL,
--    country_id INT NOT NULL,
--    phone VARCHAR(100) NOT NULL,
--    email VARCHAR(100) NOT NULL,
--    FOREIGN KEY (major_id) REFERENCES major(id),
--    FOREIGN KEY (country_id) REFERENCES country(id)
--);

--INSERT INTO major (name) VALUES ('Computer Science'), ('Mathematics'), ('Business');
--INSERT INTO country (code) VALUES ('MX'), ('USA'), ('CAN');
