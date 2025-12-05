CREATE DATABASE IF NOT EXISTS students;
FLUSH PRIVILEGES;
USE students;

CREATE TABLE dept (
    major_id INT AUTO_INCREMENT PRIMARY KEY,
    major VARCHAR(50) NOT NULL
);

CREATE TABLE origin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(3) NOT NULL
);

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    major_id INT NOT NULL,
    origin_id INT NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(100),
    FOREIGN KEY (major_id) REFERENCES dept(major_id),
    FOREIGN KEY (origin_id) REFERENCES origin(id)
);

INSERT INTO dept (major) VALUES 
('Engineering'),
('Administration'),
('Medicine'),
('Laws');

INSERT INTO origin (code) VALUES 
('MX'),
('USA'),
('FR'),
('CAN');

INSERT INTO students (name, major_id, origin_id, phone, email) VALUES 
('Juan Pérez', 1, 1, '7711234032', 'asterix@outlook.com'),
('María García', 2, 2, '5512345678', 'sisiphos@outloook.com'),
('Carlos López', 3, 1, '3319876543', 'jester@outlook.com'),
('Luisa Fernández', 4, 3, '6623456789', 'jr12hipp@outlook.com');