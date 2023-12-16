/* schema.sql */

DROP TABLE IF EXISTS users;

CREATE TABLE users (
	user_id	INTEGER PRIMARY KEY AUTOINCREMENT,
	user_name	TEXT,
	contact	TEXT
);

