import mysql.connector
from mysql.connector import Error
import csv

hostname = "piv.h.filess.io"
database = "MoviematchDB_leadershoe"
port = 3307
username = "MoviematchDB_leadershoe"
password = "322edb042e477bde5d56251c41b82fec35f4d5fb"

csv_file_path = '../data/movie_titles.csv'

try:
    connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  
            for row in csv_reader:
                print(row)
                movie_data = row[0].split('\t')
                MovieId = movie_data[0]
                Title = movie_data[1]
                insert_query = "INSERT INTO movie (MovieId, Title) VALUES (%s, %s)"
                cursor.execute(insert_query, (MovieId, Title))
            connection.commit()
            print("Data inserted successfully.")

except Error as e:
    print("Error while connecting to MySQL or inserting data:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
