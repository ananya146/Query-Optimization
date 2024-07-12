import csv
import random
import time

# Generate 100 SQL queries and their optimized versions
queries_and_optimizations = [
    ("SELECT * FROM employees WHERE department = 'Sales';", "SELECT * FROM employees WHERE department = 'Sales' AND status = 'active';"),
    ("SELECT COUNT(*) FROM orders WHERE order_date > '2020-01-01';", "SELECT COUNT(1) FROM orders WHERE order_date > '2020-01-01';"),
    ("SELECT * FROM products WHERE price > 1000;", "SELECT * FROM products WHERE price > 1000 AND status = 'available';"),
    ("SELECT name FROM customers WHERE city = 'New York';", "SELECT name FROM customers WHERE city = 'New York' AND active = 1;"),
    ("SELECT order_id, total FROM orders;", "SELECT order_id, total FROM orders WHERE status = 'completed';"),
    ("SELECT * FROM sales WHERE region = 'West';", "SELECT * FROM sales WHERE region = 'West' AND year = 2023;"),
    ("SELECT * FROM users WHERE signup_date < '2021-01-01';", "SELECT * FROM users WHERE signup_date < '2021-01-01' AND active = 1;"),
    ("SELECT * FROM invoices WHERE amount > 1000;", "SELECT * FROM invoices WHERE amount > 1000 AND paid = 1;"),
    ("SELECT * FROM inventory WHERE stock < 50;", "SELECT * FROM inventory WHERE stock < 50 AND reorder = 1;"),
    ("SELECT * FROM employees WHERE age > 30;", "SELECT * FROM employees WHERE age > 30 AND status = 'active';"),
    ("SELECT * FROM orders WHERE customer_id = 1;", "SELECT * FROM orders WHERE customer_id = 1 AND status = 'delivered';"),
    ("SELECT * FROM products WHERE category = 'Electronics';", "SELECT * FROM products WHERE category = 'Electronics' AND stock > 0;"),
    ("SELECT * FROM employees WHERE hire_date < '2020-01-01';", "SELECT * FROM employees WHERE hire_date < '2020-01-01' AND active = 1;"),
    ("SELECT * FROM users WHERE email LIKE '%@gmail.com';", "SELECT * FROM users WHERE email LIKE '%@gmail.com' AND active = 1;"),
    ("SELECT * FROM orders WHERE total > 500;", "SELECT * FROM orders WHERE total > 500 AND status = 'completed';"),
    ("SELECT * FROM sales WHERE date > '2022-01-01';", "SELECT * FROM sales WHERE date > '2022-01-01' AND region = 'North';"),
    ("SELECT * FROM employees WHERE salary > 100000;", "SELECT * FROM employees WHERE salary > 100000 AND status = 'active';"),
    ("SELECT * FROM products WHERE discount > 20;", "SELECT * FROM products WHERE discount > 20 AND available = 1;"),
    ("SELECT * FROM customers WHERE join_date < '2021-01-01';", "SELECT * FROM customers WHERE join_date < '2021-01-01' AND active = 1;"),
    ("SELECT * FROM invoices WHERE due_date < '2023-01-01';", "SELECT * FROM invoices WHERE due_date < '2023-01-01' AND paid = 1;"),
    ("SELECT * FROM orders WHERE order_date < '2020-01-01';", "SELECT * FROM orders WHERE order_date < '2020-01-01' AND status = 'completed';"),
    ("SELECT * FROM products WHERE price < 50;", "SELECT * FROM products WHERE price < 50 AND available = 1;"),
    ("SELECT * FROM customers WHERE last_purchase > '2022-01-01';", "SELECT * FROM customers WHERE last_purchase > '2022-01-01' AND active = 1;"),
    ("SELECT * FROM invoices WHERE paid = 0;", "SELECT * FROM invoices WHERE paid = 0 AND amount > 100;"),
    ("SELECT * FROM employees WHERE department = 'IT';", "SELECT * FROM employees WHERE department = 'IT' AND status = 'active';"),
    ("SELECT * FROM sales WHERE amount < 500;", "SELECT * FROM sales WHERE amount < 500 AND region = 'East';"),
    ("SELECT * FROM orders WHERE quantity > 10;", "SELECT * FROM orders WHERE quantity > 10 AND status = 'shipped';"),
    ("SELECT * FROM products WHERE category = 'Clothing';", "SELECT * FROM products WHERE category = 'Clothing' AND stock > 0;"),
    ("SELECT * FROM customers WHERE city = 'Los Angeles';", "SELECT * FROM customers WHERE city = 'Los Angeles' AND active = 1;"),
    ("SELECT * FROM employees WHERE position = 'Manager';", "SELECT * FROM employees WHERE position = 'Manager' AND status = 'active';"),
    ("SELECT * FROM orders WHERE payment_method = 'Credit Card';", "SELECT * FROM orders WHERE payment_method = 'Credit Card' AND status = 'completed';"),
    ("SELECT * FROM products WHERE supplier_id = 2;", "SELECT * FROM products WHERE supplier_id = 2 AND available = 1;"),
    ("SELECT * FROM customers WHERE country = 'USA';", "SELECT * FROM customers WHERE country = 'USA' AND active = 1;"),
    ("SELECT * FROM invoices WHERE amount > 500;", "SELECT * FROM invoices WHERE amount > 500 AND paid = 1;"),
    ("SELECT * FROM employees WHERE years_experience > 5;", "SELECT * FROM employees WHERE years_experience > 5 AND status = 'active';"),
    ("SELECT * FROM sales WHERE product_id = 3;", "SELECT * FROM sales WHERE product_id = 3 AND region = 'West';"),
    ("SELECT * FROM orders WHERE shipping_date > '2022-01-01';", "SELECT * FROM orders WHERE shipping_date > '2022-01-01' AND status = 'shipped';"),
    ("SELECT * FROM products WHERE name LIKE 'A%';", "SELECT * FROM products WHERE name LIKE 'A%' AND available = 1;"),
    ("SELECT * FROM customers WHERE phone IS NOT NULL;", "SELECT * FROM customers WHERE phone IS NOT NULL AND active = 1;"),
    ("SELECT * FROM employees WHERE performance_rating > 4;", "SELECT * FROM employees WHERE performance_rating > 4 AND status = 'active';"),
    ("SELECT * FROM orders WHERE customer_id IN (SELECT customer_id FROM customers WHERE country = 'Canada');", "SELECT * FROM orders WHERE customer_id IN (SELECT customer_id FROM customers WHERE country = 'Canada') AND status = 'delivered';"),
    ("SELECT * FROM products WHERE supplier_id = 5;", "SELECT * FROM products WHERE supplier_id = 5 AND available = 1;"),
    ("SELECT * FROM customers WHERE last_purchase < '2020-01-01';", "SELECT * FROM customers WHERE last_purchase < '2020-01-01' AND active = 1;"),
    ("SELECT * FROM invoices WHERE due_date > '2021-01-01';", "SELECT * FROM invoices WHERE due_date > '2021-01-01' AND paid = 1;"),
    ("SELECT * FROM employees WHERE department = 'HR';", "SELECT * FROM employees WHERE department = 'HR' AND status = 'active';"),
    ("SELECT * FROM sales WHERE product_id = 1;", "SELECT * FROM sales WHERE product_id = 1 AND region = 'South';"),
    ("SELECT * FROM orders WHERE payment_method = 'PayPal';", "SELECT * FROM orders WHERE payment_method = 'PayPal' AND status = 'completed';"),
    ("SELECT * FROM products WHERE name LIKE 'B%';", "SELECT * FROM products WHERE name LIKE 'B%' AND available = 1;"),
    ("SELECT * FROM customers WHERE email IS NOT NULL;", "SELECT * FROM customers WHERE email IS NOT NULL AND active = 1;"),
    ("SELECT * FROM employees WHERE performance_rating > 3;", "SELECT * FROM employees WHERE performance_rating > 3 AND status = 'active';")
]



# Specify the file name
csv_filename = 'sql_queries.csv'

# Open the CSV file for writing
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL, escapechar='\\')
    # Write the header
    writer.writerow(['Original_Query', 'Optimized_Query'])
    # Write each row of data
    for original_query, optimized_query in queries_and_optimizations:
        # Write queries ensuring they are properly enclosed in double quotes
        writer.writerow([original_query, f'"{optimized_query}"'])

print(f'{csv_filename} has been created successfully.')