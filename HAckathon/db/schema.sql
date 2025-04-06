-- SQLite schema for inventory
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL
);
