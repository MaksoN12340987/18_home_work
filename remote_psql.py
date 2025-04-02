import csv

with open("data/customers_data.csv", newline="") as file:
    customers_data = [row for row in csv.reader(file) if "customer_id" not in row]

with open("data/employees_data.csv", newline="") as file:
    employees_data = [row for row in csv.reader(file) if "first_name" not in row]

with open("data/orders_data.csv", newline="") as file:
    orders_data = [row for row in csv.reader(file) if "order_id" not in row]

# Импортируйте библиотеку psycopg2
import psycopg2

# Создайте подключение к базе данных
conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="pi")

# Открытие курсора
cur = conn.cursor()

# Не меняйте и не удаляйте эти строки - они нужны для проверки
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS customers")
cur.execute("DROP TABLE IF EXISTS employees")


# Ниже напишите код запросов для создания таблиц
cur.execute(
    "CREATE TABLE customers (customer_id char(5) PRIMARY KEY, company_name text NOT NULL, contact_name text NOT NULL)"
)

cur.execute(
    "CREATE TABLE employees (employee_id serial PRIMARY KEY, first_name text NOT NULL, last_name text NOT NULL, title text NOT NULL, birth_date date NOT NULL, notes text);"
)

cur.execute(
    "CREATE TABLE orders (order_id integer PRIMARY KEY, customer_id char(5) REFERENCES customers(customer_id) NOT NULL, employee_id integer REFERENCES employees(employee_id) NOT NULL, order_date date NOT NULL, ship_city text NOT NULL)"
)

# Зафиксируйте изменения в базе данных
conn.commit()

# Теперь приступаем к операциям вставок данных
for row in customers_data:
    query = f'INSERT INTO customers ("customer_id", "company_name", "contact_name") VALUES ({", ".join(["%s"] * len(row))}) RETURNING "customer_id", "company_name", "contact_name"'
    print(row)
    cur.execute(query, row)

conn.commit()
print(cur.fetchone())

for row in employees_data:
    query = f'INSERT INTO employees ("first_name", "last_name", "title", "birth_date", "notes") VALUES ({", ".join(["%s"] * len(row))}) RETURNING *'
    cur.execute(query, row)

conn.commit()
res_employees = cur.fetchone()


for row in orders_data:
    query = f'INSERT INTO orders ("order_id", "customer_id", "employee_id", "order_date", "ship_city") VALUES ({", ".join(["%s"] * len(row))}) RETURNING *'
    cur.execute(query, row)


conn.commit()
res_orders = cur.fetchall()

# Закрытие курсора
cur.close()

# Закрытие соединения
conn.close()

print(res_employees)
print(res_orders)
