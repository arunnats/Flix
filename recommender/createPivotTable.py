import pickle
import pandas as pd

# Read the ratings and movie titles data
df_ratings = pd.read_csv('./ratings.csv', sep=',', usecols=['userId', 'movieId', 'rating'])
df_titles = pd.read_csv("./movies.csv", sep=',', usecols=['movieId', 'title'])

# Merge the dataframes on 'movieId'
df = pd.merge(df_ratings, df_titles, on='movieId')

min_reviews_movie = 5
min_reviews_user = 200

# Filter movies with at least 'x' reviews
popular_movies = df['title'].value_counts()
top_movies = popular_movies[popular_movies >= min_reviews_movie].index
df_filtered_movies = df[df['title'].isin(top_movies)]

# Filter users with at least 'x' reviews
users_with_enough_reviews = df_filtered_movies['userId'].value_counts()
active_users = users_with_enough_reviews[users_with_enough_reviews >= min_reviews_user].index
df_filtered_users = df_filtered_movies[df_filtered_movies['userId'].isin(active_users)]

# Create the pivot table
moviemat_filtered = df_filtered_users.pivot_table(index='userId', columns='title', values='rating')

# Save the pivot table as a pickle file
with open('moviemat_filtered.pkl', 'wb') as f:
    pickle.dump(moviemat_filtered, f)
