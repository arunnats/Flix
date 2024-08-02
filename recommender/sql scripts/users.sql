SHOW DATABASES;
USE bookmate;

CREATE TABLE users (
	id VARCHAR(255) PRIMARY KEY, 
    LibID VARCHAR(25) UNIQUE,
    BookmateID VARCHAR(255) UNIQUE,
    email VARCHAR(255),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    nickname VARCHAR(100),
    phone_num VARCHAR(10),
    instagram VARCHAR(255),
    picture_url VARCHAR(255),
    instagram_public BOOLEAN DEFAULT TRUE,
    phone_public BOOLEAN DEFAULT TRUE,
    email_public BOOLEAN DEFAULT TRUE,
    opted_in BOOLEAN DEFAULT FALSE,
    profile_done BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (BookmateID) REFERENCES users(id)
);

SELECT profile_done FROM users LIMIT 10;
SELECT COUNT(*) FROM users WHERE opted_in = TRUE;
SELECT * FROM users;


DROP TABLE users;