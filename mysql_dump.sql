CREATE DATABASE company;

USE company;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary INT
);

INSERT INTO employees VALUES
(1, 'Rahul', 'IT', 50000),
(2, 'Priya', 'HR', 40000),
(3, 'Amit', 'Finance', 45000);
