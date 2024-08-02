SHOW DATABASES;
USE bookmate;

CREATE TABLE top_books (
    `User-ID` INT,
    ISBN TEXT,
    `Book-Rating` DOUBLE,
    `Book-Title` TEXT,
    `Book-Author` TEXT,
    `Year-Of-Publication` TEXT,
    Publisher TEXT,
    `Image-URL-S` TEXT,
    `Image-URL-M` TEXT,
    `Image-URL-L` TEXT,
    PRIMARY KEY (ISBN)
);

DROP TABLE top_books;

SELECT COUNT(*) FROM top_books;
CREATE INDEX titles ON top_books (`Book-Title`(255));
ALTER TABLE top_books ADD FULLTEXT INDEX title_index (`Book-Title`);

SELECT * FROM top_books WHERE `Book-Title` LIKE '%harry potter%';

SELECT * FROM top_books WHERE `ISBN` = 0439064864;

SELECT 'User-ID', 'ISBN', 'Book-Rating', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-S', 'Image-URL-M', 'Image-URL-L'
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/top_books_with_headers.csv'
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n';

SELECT `User-ID`, ISBN, `Book-Rating`, `Book-Title`, `Book-Author`, `Year-Of-Publication`, Publisher, `Image-URL-S`, `Image-URL-M`, `Image-URL-L`
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/top_books_data.csv'
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
FROM top_books;

LOAD DATA LOCAL INFILE'~/apps/top_books_data.csv'
INTO TABLE top_books
FIELDS TERMINATED BY '\t' 
LINES TERMINATED BY '\n'
;


DESC top_books;
   
