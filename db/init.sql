-- Create database
CREATE DATABASE fooddb;

-- Use database
USE fooddb;

-- Create table
CREATE TABLE foods (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  price INT
);

-- Insert sample data
INSERT INTO foods (name, price) VALUES
('Burger', 100),
('Pizza', 200),
('Pasta', 150);
