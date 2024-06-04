import pandas as pd
import mysql.connector

# Connect to MySQL database
cnx = mysql.connector.connect(user='root', password='nats',
                              host='localhost',
                              database='flix')

def precompute_and_save():
    print("Reading ratings and movie titles data...")
    df_ratings = pd.read_csv('./data/ratings.csv', sep=',', usecols=['userId', 'movieId', 'rating'])
    df_titles = pd.read_csv("./data/movies.csv", sep=',', usecols=['movieId', 'title'])
    print("Done reading.")

    print("Merging dataframes...")
    df = pd.merge(df_ratings, df_titles, on='movieId')

    # Calculate number of ratings per movie
    print("Calculating ratings per movie...")
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())

    min_reviews_movie = 15
    min_reviews_user = 150

    # Filter movies with at least 'x' reviews
    print("Filtering movies...")
    popular_movies = df['title'].value_counts()
    top_movies = popular_movies[popular_movies >= min_reviews_movie].index
    df_filtered_movies = df[df['title'].isin(top_movies)]

    print("Saving popular movies data...")
    movie_titles = df_filtered_movies[['movieId', 'title']]

    # Write data to MySQL table
    movie_titles.to_sql(name='movie', con=cnx, if_exists='replace', index=False)

    print("Preprocessing complete!")

precompute_and_save()