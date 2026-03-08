CREATE DATABASE fooddb;

USE fooddb;

CREATE TABLE foods (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  price INT
);

INSERT INTO foods (name, price) VALUES
('Burger', 100),
('Pizza', 200),
('Pasta', 150);
