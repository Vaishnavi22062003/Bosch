use Bosch;
show tables;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
show tables;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    department_id INT,
    job_title VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO employees VALUES
(1, 'Alice', 101, 'Engineer', 70000),
(2, 'Bob', 101, 'Engineer', 80000),
(3, 'Charlie', 102, 'Analyst', 65000),
(4, 'Daisy', 103, 'Manager', 90000),
(5, 'Ethan', 102, 'Analyst', 70000);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    product_id INT,
    category_id INT,
    sales_amount DECIMAL(10, 2),
    sale_date DATE
);

INSERT INTO sales VALUES
(1, 201, 10, 1000.00, '2024-01-01'),
(2, 202, 10, 1500.00, '2024-01-03'),
(3, 203, 11, 2000.00, '2024-01-04'),
(4, 201, 10, 500.00, '2024-01-05'),
(5, 203, 11, 1000.00, '2024-01-06');

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    region VARCHAR(50),
    status VARCHAR(20),
    sales_amount DECIMAL(10, 2)
);

INSERT INTO orders VALUES
(1001, 301, 201, '2024-02-01', 'North', 'Shipped', 500.00),
(1002, 302, 202, '2024-02-01', 'North', 'Pending', 600.00),
(1003, 303, 203, '2024-02-02', 'South', 'Shipped', 800.00),
(1004, 301, 202, '2024-02-03', 'North', 'Shipped', 900.00),
(1005, 304, 203, '2024-02-03', 'South', 'Cancelled', 750.00),
(1006, 302, 201, '2024-02-04', 'North', 'Pending', 300.00);


CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category_id INT,
    price DECIMAL(10, 2)
);

INSERT INTO products VALUES
(201, 'Widget', 10, 25.00),
(202, 'Gadget', 10, 40.00),
(203, 'Thingamajig', 11, 100.00),
(204, 'Doohickey', 12, 10.00);

SELECT
    category_id,
    product_id,
    product_name,
    total_sales
FROM (
    SELECT
        s.category_id,
        s.product_id,
        p.product_name,
        SUM(s.sales_amount) AS total_sales,
        RANK() OVER (PARTITION BY s.category_id ORDER BY SUM(s.sales_amount) DESC) AS sales_rank
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
    GROUP BY s.category_id, s.product_id, p.product_name
) ranked_sales
WHERE sales_rank = 1;

SELECT Department_ID, AVG(Salary) AS AvgSalary
FROM employees
GROUP BY Department_ID
ORDER BY AvgSalary DESC
LIMIT 1;

SELECT e.Employee_ID,
       e.Name,
       e.Department_ID,
       e.Salary
FROM employees e
WHERE e.Salary > (
    SELECT AVG(e2.Salary)
    FROM employees e2
    WHERE e2.Department_ID = e.Department_ID
);

SELECT o.region,
       o.Customer_ID,
       COUNT(o.Order_ID) AS TotalOrders
FROM orders o
GROUP BY o.region, o.Customer_ID
HAVING COUNT(o.Order_ID) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(o2.Order_ID) AS cnt
        FROM orders o2
        WHERE o2.region = o.region
        GROUP BY o2.Customer_ID
    ) AS region_counts
);


SELECT p.Category_ID,
       AVG(p.Price) AS AvgCategoryPrice
FROM products p
GROUP BY p.Category_ID
HAVING AVG(p.Price) > (
    SELECT AVG(Price) 
    FROM products
);

SELECT p.Product_ID,
       p.Product_Name
FROM products p
LEFT JOIN orders o
    ON p.Product_ID = o.Product_ID
WHERE o.Product_ID IS NULL;
   