from contextlib import asynccontextmanager
from fastapi import FastAPI
import pandas as pd

# Define the FastAPI app
app = FastAPI()

# Function to perform setup tasks and store data in the app object
def setup_data():
    global app
    print("Reading ratings and movie titles data...")
    df_ratings = pd.read_csv('./ratings.csv', sep=',', usecols=['userId', 'movieId', 'rating'])
    df_titles = pd.read_csv("./movies.csv", sep=',', usecols=['movieId', 'title'])
    print("Done reading.")

    print("Merging dataframes...")
    df = pd.merge(df_ratings, df_titles, on='movieId')

    # Calculate number of ratings per movie
    print("Calculating ratings per movie...")
    ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
    ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())

    min_reviews_movie = 5
    min_reviews_user = 200

    # Filter movies with at least 'x' reviews
    print("Filtering movies...")
    popular_movies = df['title'].value_counts()
    top_movies = popular_movies[popular_movies >= min_reviews_movie].index
    df_filtered_movies = df[df['title'].isin(top_movies)]

    # Filter users with at least 'x' reviews
    print("Filtering users...")
    users_with_enough_reviews = df_filtered_movies['userId'].value_counts()
    active_users = users_with_enough_reviews[users_with_enough_reviews >= min_reviews_user].index
    df_filtered_users = df_filtered_movies[df_filtered_movies['userId'].isin(active_users)]

    # Create the pivot table
    print("Creating pivot table...")
    moviemat_filtered = df_filtered_users.pivot_table(index='userId', columns='title', values='rating')
    print("Setup complete.")

    # Calculate the correlation matrix between movies
    print("Calculating correlation matrix...")
    corr_matrix = moviemat_filtered.corr(method='pearson')
    print("Correlation matrix calculation complete.")

    # Store data in the app object
    app.ratings = ratings
    app.moviemat = moviemat_filtered
    app.corr_matrix = corr_matrix

# Define lifespan context manager to perform setup tasks
@asynccontextmanager
async def lifespan(app):
    setup_data()
    yield

# Set up the lifespan context manager
app.router.lifespan_context = lifespan

# Define the GET endpoint
@app.get("/usage/")
async def get_usage(movie_title: str):
    corr_movie = app.corr_matrix[movie_title]
    corr_movie = pd.DataFrame(corr_movie, columns=['Correlation'])
    corr_movie.dropna(inplace=True)
    corr_movie = corr_movie.join(app.ratings['num of ratings'])
    return corr_movie[corr_movie['num of ratings'] > 10000].sort_values('Correlation', ascending=False).head()
