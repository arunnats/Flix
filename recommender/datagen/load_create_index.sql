CREATE DATABASE flix;

USE flix;

DROP TABLE movie;
CREATE TABLE movie(MovieId VARCHAR(255), Title VARCHAR(255) );

LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\movie_titles.csv'
    INTO TABLE movie
    FIELDS TERMINATED BY '\t'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (MovieId, Title);
    
SELECT * FROM movie book LIMIT 10;

CREATE INDEX titles ON movie (Title(255));

ALTER TABLE movie ADD FULLTEXT INDEX title_index (title);

SELECT * FROM movie WHERE MATCH(title) AGAINST ('pu');

SELECT Title, MovieId 
FROM movie
WHERE MATCH(Title) AGAINST('p' IN NATURAL LANGUAGE MODE)
LIMIT 15;


