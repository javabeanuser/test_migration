CREATE SCHEMA g_supermarket;
CREATE TABLE g_items.drivers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);
INSERT INTO g_items.drivers (name, license_number)
VALUES
  ('Lemon'),
  ('Apple');