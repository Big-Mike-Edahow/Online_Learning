/* schema.sql */

DROP TABLE IF EXISTS developers;

CREATE TABLE developers (
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        joining_date DATETIME,
                        salary REAL NOT NULL);

