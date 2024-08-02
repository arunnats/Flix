SHOW DATABASES;
USE bookmate;

CREATE TABLE library (
    LibID VARCHAR(25) PRIMARY KEY,
    id VARCHAR(255) NOT NULL,
    Fave_Books TEXT,
    Wish_List TEXT,
    answers VARCHAR(255),
    FOREIGN KEY (id) REFERENCES users(id)
);

SELECT * FROM library LIMIT 10;

DROP TABLE library;