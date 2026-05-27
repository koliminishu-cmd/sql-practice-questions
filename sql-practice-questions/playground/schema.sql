DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS logins;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS product_prices;
DROP TABLE IF EXISTS exchange_rates;
DROP TABLE IF EXISTS job_runs;
DROP TABLE IF EXISTS customer_dim;

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY,
  customer_name TEXT NOT NULL,
  country TEXT NOT NULL,
  signup_date TEXT NOT NULL,
  acquisition_channel TEXT NOT NULL
);

CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  order_date TEXT NOT NULL,
  status TEXT NOT NULL,
  amount REAL NOT NULL,
  currency TEXT NOT NULL,
  promised_delivery_date TEXT,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
  product_id INTEGER PRIMARY KEY,
  product_name TEXT NOT NULL,
  category TEXT NOT NULL
);

CREATE TABLE order_items (
  order_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  price REAL NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE payments (
  payment_id INTEGER PRIMARY KEY,
  order_id INTEGER NOT NULL,
  status TEXT NOT NULL,
  paid_at TEXT,
  amount REAL NOT NULL,
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE logins (
  user_id INTEGER NOT NULL,
  login_time TEXT NOT NULL
);

CREATE TABLE events (
  user_id INTEGER NOT NULL,
  event_name TEXT NOT NULL,
  event_time TEXT NOT NULL
);

CREATE TABLE subscriptions (
  user_id INTEGER NOT NULL,
  start_date TEXT NOT NULL,
  end_date TEXT,
  plan_id TEXT NOT NULL,
  monthly_price REAL NOT NULL
);

CREATE TABLE inventory (
  product_id INTEGER NOT NULL,
  snapshot_date TEXT NOT NULL,
  quantity INTEGER NOT NULL,
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE product_prices (
  product_id INTEGER NOT NULL,
  price REAL NOT NULL,
  effective_date TEXT NOT NULL,
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE exchange_rates (
  currency TEXT NOT NULL,
  rate_date TEXT NOT NULL,
  usd_rate REAL NOT NULL
);

CREATE TABLE job_runs (
  job_id TEXT NOT NULL,
  run_id INTEGER NOT NULL,
  started_at TEXT NOT NULL,
  finished_at TEXT,
  status TEXT NOT NULL
);

CREATE TABLE customer_dim (
  customer_key INTEGER PRIMARY KEY,
  customer_id INTEGER NOT NULL,
  customer_name TEXT NOT NULL,
  country TEXT NOT NULL,
  effective_start TEXT NOT NULL,
  effective_end TEXT,
  is_current INTEGER NOT NULL
);

