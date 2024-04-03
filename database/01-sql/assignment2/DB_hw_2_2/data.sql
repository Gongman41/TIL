CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE,
  total_amount FLOAT
  );

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  phone VARCHAR(50) NOT NULL
  );


INSERT INTO
  orders (order_date,total_amount)
VALUES
  ('2023-07-15','50.99'),
  ('2023-07-16','75.5'),
  ('2023-07-17','30.25');

INSERT INTO
  customers (name, email, phone)
VALUES
  ('허균','email1','010-2980-5986'),
  ('김영희','email2','010-6633-7462'),
  ('이철수','email3','010-2204-8051');

DELETE FROM orders
WHERE order_id = 3;

UPDATE customers
SET  name = '홍길동'
WHERE customer_id = 1;

SELECT *
FROM orders;

SELECT *
FROM customers;


