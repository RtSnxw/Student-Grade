CREATE DATABASE IF NOT EXISTS students;
CREATE USER IF NOT EXISTS 'user'@'%' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON students.* TO 'user'@'%';
FLUSH PRIVILEGES;
USE students;

-- 2) Create reference tables:
CREATE TABLE dept (
    major_id INT AUTO_INCREMENT PRIMARY KEY,
    major VARCHAR(50) NOT NULL
);

CREATE TABLE origin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(3) NOT NULL
);

-- 3) Create students table that references dept and origin:
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    major_id INT NOT NULL,
    origin_id INT NOT NULL,
    FOREIGN KEY (major_id) REFERENCES dept(major_id),
    FOREIGN KEY (origin_id) REFERENCES origin(id)
);

-- 4) Insert seed data:
INSERT INTO dept (major) VALUES 
('Engeneering'),
('Administration'),
('Medicine'),
('Laws');

INSERT INTO origin (code) VALUES 
('MX'),
('USA'),
('FR'),
('CAN');

INSERT INTO students (name, major_id, origin_id) VALUES 
('Juan Pérez', 1, 1),
('María García', 2, 2),
('Carlos López', 3, 1),
('Ana Martínez', 1, 3);