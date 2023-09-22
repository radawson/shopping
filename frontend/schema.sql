DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    item TEXT NOT NULL,
    description TEXT NOT NULL,
    upc TEXT,
    price REAL,
    quantity INTEGER NOT NULL DEFAULT 1,
    image TEXT NOT NULL DEFAULT 'https://via.placeholder.com/150'
);