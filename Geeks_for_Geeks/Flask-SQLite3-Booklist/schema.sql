/* schema.sql */

DROP TABLE IF EXISTS booklist;

CREATE TABLE IF NOT EXISTS booklist
(
    bookname VARCHAR(50), author VARCHAR(25), genre VARCHAR(25)
);

